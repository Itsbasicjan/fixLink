/* fixlinkv2/static/fixlink_patch.js
 * Entfernt leere 'link'-Strings aus allen REST‑Requests
 * (XMLHttpRequest, fetch und fetch(Request‑Objekt))
 * ------------------------------------------------------------------ */

/* Hilfs­funktion: Body prüfen und ggf. das leere link‑Feld löschen */
function sanitize(data) {
    if (!data) return data;
  
    // Falls ein String übergeben wurde → versuchen, JSON zu parsen
    if (typeof data === 'string') {
      try { data = JSON.parse(data); } catch { return data; }
    }
  
    // Objekt: leeres link‑Feld entfernen
    if (typeof data === 'object' && data.link === '') {
      delete data.link;
    }
  
    // Wenn wir ursprünglich einen String hatten, wieder stringifizieren
    return typeof data === 'string' ? JSON.stringify(data) : data;
  }
  
  /* --------------------- XMLHttpRequest ---------------------------- */
  const _send = XMLHttpRequest.prototype.send;
  XMLHttpRequest.prototype.send = function (body) {
    return _send.call(this, sanitize(body));
  };
  
  /* ------------------------- fetch --------------------------------- */
  const _fetch = window.fetch;
  window.fetch = async function (resource, init = {}) {
    // Variante fetch(url, { body: … })
    if (init.body !== undefined) {
      init = { ...init, body: sanitize(init.body) };
  
    // Variante fetch(new Request(..))
    } else if (resource instanceof Request) {
      const bodyText = await resource.clone().text();
      resource = new Request(resource, { body: sanitize(bodyText) });
    }
  
    return _fetch(resource, init);
  };
  
  /* --------------------------------------------------------------- */
  /* InvenTree‑Entry‑Point: wird vom UI‑Hook aufgerufen */
  export function initPatch() {
    // Der eigentliche Patch ist schon oben installiert – hier nichts zu tun.
  }
  