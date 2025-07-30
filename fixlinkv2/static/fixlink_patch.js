/** Wird von InvenTree einmal beim ersten UI‑Aufruf geladen
 *  und patcht danach alle XMLHttpRequest‑Aufrufe global. */
export function initPatch() {
    // Patch global XMLHttpRequest.send so, dass leere link‑Strings entfernt werden
    (function () {
      const oldSend = XMLHttpRequest.prototype.send;
  
      XMLHttpRequest.prototype.send = function (body) {
        try {
          const json = JSON.parse(body);
          if (json && json.link === '') {
            delete json.link;          // leerer String → Feld entfernen
            body = JSON.stringify(json);
          }
        } catch (e) {
          // body war kein JSON – ignorieren
        }
        return oldSend.call(this, body);
      };
    })();
  }