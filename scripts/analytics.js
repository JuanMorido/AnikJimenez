const GTM_ID = 'GTM-PQPWLM58';

window.dataLayer = window.dataLayer || [];
function gtag() { dataLayer.push(arguments); }
window.gtag = gtag;
gtag('js', new Date());

(function (w, d, s, l, i) {
  w[l] = w[l] || [];
  w[l].push({ 'gtm.start': new Date().getTime(), event: 'gtm.js' });
  const primero = d.getElementsByTagName(s)[0];
  const etiqueta = d.createElement(s);
  const capa = l !== 'dataLayer' ? '&l=' + l : '';
  etiqueta.async = true;
  etiqueta.src = 'https://www.googletagmanager.com/gtm.js?id=' + i + capa;
  primero.parentNode.insertBefore(etiqueta, primero);
})(window, document, 'script', 'dataLayer', GTM_ID);
