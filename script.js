// until the real photos are in assets/, fall back to a stand-in (and drop captions that name a person)
document.querySelectorAll('img[data-fallback]').forEach(img => {
  const swap = () => {
    img.src = img.dataset.fallback;
    img.removeAttribute('data-fallback');
    img.alt = '';
    img.closest('figure')?.querySelector('figcaption')?.remove();
  };
  if (img.complete && !img.naturalWidth) swap(); else img.addEventListener('error', swap, { once: true });
});

// menu
const btn = document.querySelector('.menu-btn');
const label = btn.querySelector('.txt');
const setMenu = open => {
  document.body.classList.toggle('menu-open', open);
  btn.setAttribute('aria-expanded', open);
  label.textContent = open ? 'Close' : 'Menu';
};
btn.addEventListener('click', () => setMenu(!document.body.classList.contains('menu-open')));
document.addEventListener('keydown', e => { if (e.key === 'Escape') setMenu(false); });

// header colour over the hero
const bar = document.querySelector('.bar');
const hero = document.querySelector('.hero');
const onScroll = () => {
  const past = window.scrollY > (hero ? hero.offsetHeight - 80 : 40);
  bar.classList.toggle('solid', past);
  bar.classList.toggle('on-dark', !!hero && !past);
};
onScroll();
addEventListener('scroll', onScroll, { passive: true });

// hero slideshow
if (hero) {
  const imgs = [...hero.querySelectorAll('.slides img')];
  const num = hero.querySelector('.num');
  const bar = hero.querySelector('.progress b');
  let i = 0;
  const show = n => {
    imgs.forEach((img, k) => img.classList.toggle('active', k === n));
    num.textContent = String(n + 1).padStart(2, '0');
    bar.classList.remove('run'); void bar.offsetWidth; bar.classList.add('run');
  };
  show(0);
  hero.classList.add('loaded');
  const wide = matchMedia('(min-width: 901px)');
  if (imgs.length > 1) setInterval(() => { if (wide.matches) return; i = (i + 1) % imgs.length; show(i); }, 6000);
}

// reveal
const io = new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
}), { threshold: .15 });
document.querySelectorAll('.rv').forEach(el => io.observe(el));

// gallery
const tiles = document.querySelectorAll('.masonry button');
document.querySelectorAll('.filters button').forEach(f => f.addEventListener('click', () => {
  document.querySelectorAll('.filters button').forEach(b => b.classList.toggle('on', b === f));
  tiles.forEach(t => t.classList.toggle('hide', f.dataset.f !== 'all' && t.dataset.c !== f.dataset.f));
}));
const lb = document.querySelector('.lightbox');
if (lb) {
  const big = lb.querySelector('img'), cap = lb.querySelector('p');
  tiles.forEach(t => t.addEventListener('click', () => {
    const img = t.querySelector('img');
    big.src = img.src.replace(/w=\d+/, 'w=1600'); big.alt = img.alt; cap.textContent = img.alt;
    lb.hidden = false;
  }));
  lb.addEventListener('click', e => { if (e.target.tagName !== 'IMG') lb.hidden = true; });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') lb.hidden = true; });
}

// contact form opens WhatsApp
const form = document.querySelector('#note');
if (form) form.addEventListener('submit', e => {
  e.preventDefault();
  const d = new FormData(form);
  const text = `Hello, my name is ${d.get('name')}.\n\n${d.get('topic')}\n\n${d.get('message')}`;
  window.open('https://wa.me/233546878015?text=' + encodeURIComponent(text), '_blank', 'noopener');
});

document.querySelectorAll('.yr').forEach(y => y.textContent = new Date().getFullYear());
