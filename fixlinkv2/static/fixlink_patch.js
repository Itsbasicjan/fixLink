/** fixlinkv2/static/fixlink_patch.js
 *  Entfernt leere 'link'‑Strings aus allen REST‑Bodies (XHR + fetch)
 *  Wird einmalig von der UI geladen – danach global aktiv.
 */
function sanitizeBody(body) {
    if (typeof body !== 'string') {           // FormData, Blob, null …
      return body;
    }
    try {
      const json = JSON.parse(body);
      if (json && json.link === '') {
        delete json.link;                     // "" → Feld komplett entfernen
        return JSON.stringify(json);
      }
    } catch (_) {/* Body war kein JSON – ignorieren */}
    return body;
  }
  
  /* ---------- XMLHttpRequest ---------- */
  const _send = XMLHttpRequest.prototype.send;
  XMLHttpRequest.prototype.send = function (body) {
    return _send.call(this, sanitizeBody(body));
  };
  
  /* ---------- WHATWG Fetch ---------- */
  const _fetch = window.fetch;
  window.fetch = function (input, init = {}) {
    if (init.body) {
      init = { ...init, body: sanitizeBody(init.body) };
    }
    return _fetch(input, init);
  };
  
  /* Standard‑Hook für das UI‑Mixin */
  export function initPatch() {
    /* Nichts zu tun – Patch ist schon oben installiert */
    return null;
  }
  