// mobile menu
const burger = document.getElementById('burger');
const links = document.getElementById('links');
burger.addEventListener('click', () => {
  const open = links.classList.toggle('open');
  burger.setAttribute('aria-expanded', open);
});
links.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
  links.classList.remove('open');
  burger.setAttribute('aria-expanded', false);
}));

// reveal on scroll
const io = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// gallery filter
const tiles = document.querySelectorAll('.g');
document.querySelectorAll('.filters button').forEach(btn => btn.addEventListener('click', () => {
  document.querySelectorAll('.filters button').forEach(b => b.classList.toggle('on', b === btn));
  const f = btn.dataset.f;
  tiles.forEach(t => t.classList.toggle('hide', f !== 'all' && t.dataset.c !== f));
}));

// lightbox
const lb = document.getElementById('lb');
const lbimg = document.getElementById('lbimg');
const lbcap = document.getElementById('lbcap');
const closeLb = () => { lb.hidden = true; };
tiles.forEach(t => t.addEventListener('click', () => {
  const img = t.querySelector('img');
  lbimg.src = img.src.replace(/w=\d+&h=\d+/, 'w=1600&h=1200');
  lbimg.alt = img.alt;
  lbcap.textContent = img.alt;
  lb.hidden = false;
}));
document.getElementById('lbx').addEventListener('click', closeLb);
lb.addEventListener('click', e => { if (e.target === lb) closeLb(); });
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeLb(); });

// contact form -> WhatsApp
document.getElementById('msg').addEventListener('submit', e => {
  e.preventDefault();
  const d = new FormData(e.target);
  const text = `Hello Virtuous Women of Destiny, my name is ${d.get('name')}.\n\n${d.get('topic')}\n\n${d.get('message')}`;
  window.open('https://wa.me/233546878015?text=' + encodeURIComponent(text), '_blank', 'noopener');
});

document.getElementById('yr').textContent = new Date().getFullYear();
