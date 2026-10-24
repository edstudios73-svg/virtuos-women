// "Find us" map: dark monochrome tiles, a custom pulsing pin, and a slow fly-in from all of Accra
(() => {
  const el = document.getElementById('map');
  if (!el || !window.L) return;

  const pin = [5.6359, -0.1498]; // Jungle Avenue, East Legon
  const map = L.map(el, {
    center: [5.60, -0.19],
    zoom: 12,
    zoomControl: false,
    attributionControl: true,
    scrollWheelZoom: false,
    dragging: !L.Browser.mobile,
    tap: false,
  });

  // standard OpenStreetMap tiles, turned into a dark monochrome map by CSS (see .leaflet-tile-pane)
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
  }).addTo(map);

  L.control.zoom({ position: 'topright' }).addTo(map);

  const icon = L.divIcon({
    className: 'pin',
    html: '<span class="pin-ring"></span><span class="pin-ring r2"></span><span class="pin-dot"></span><span class="pin-label">We meet here</span>',
    iconSize: [24, 24],
    iconAnchor: [12, 12],
  });
  L.marker(pin, { icon, keyboard: false }).addTo(map);

  // fly in the first time the map scrolls into view
  let flown = false;
  const fly = () => {
    if (flown) return;
    flown = true;
    const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
    reduce ? map.setView(pin, 16) : map.flyTo(pin, 16, { duration: 2.4, easeLinearity: 0.2 });
  };
  new IntersectionObserver((entries, io) => {
    if (entries.some(e => e.isIntersecting)) { fly(); io.disconnect(); }
  }, { threshold: 0.35 }).observe(el);
})();
