/* Entfernt leere 'link'‑Strings aus allen REST‑Bodies (XHR + fetch + Request‑Objekte)
 * Wird einmal beim UI‑Bootstrap geladen und patcht danach global.
 */
function sanitize(data) {
    if (!data) return data;
  
    // String » JSON?
    if (typeof data === 'string') {
      try { data = JSON.parse(data); } catch { return data; }
    }
  
    // Objekt direkt prüfen
    if (typeof data === 'object' && data.link === '') {
      delete data.link;
    }
  
    return typeof data === 'string' ? JSON.stringify(data) : data;
  }
  
  /* ---------- XMLHttpRequest ---------- */
  const send0 = XMLHttpRequest.prototype.send;
  XMLHttpRequest.prototype.send = function (body) {
    return send0.call(this, sanitize(body));
  };
  
  /* ---------- WHATWG Fetch ---------- */
  const fetch0 = window.fetch;
  window.fetch = async function (resource, init = {}) {
  
    // 1) fetch(url, {body: ...})
    if (init.body !== undefined) {
      init = { ...init, body: sanitize(init.body) };
  
    // 2) fetch(new Request(...))
    } else if (resource instanceof Request) {
      const bodyText = await resource.clone().text();
      resource = new Request(resource, { body: sanitize(bodyText) });
    }
  
    return fetch0(resource, init);
  };
  
  /* Einstiegspunkt für das UI‑Mixin – muss exportiert sein */
  export function initPatch() { /* Patch ist bereits aktiv */ }
  