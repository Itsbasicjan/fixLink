// fixlinkv2/static/fixlink_patch.js
(function () {
    const oldSend = XMLHttpRequest.prototype.send;
  
    XMLHttpRequest.prototype.send = function (body) {
      try {
        const json = JSON.parse(body);
        if (json && json.link === '') {
          delete json.link;
          body = JSON.stringify(json);
        }
      } catch (e) { /* body war kein JSON */ }
  
      return oldSend.call(this, body);
    };
  })();
  export function initPatch() {}   // <- leerer Export als Entry‑Point
  