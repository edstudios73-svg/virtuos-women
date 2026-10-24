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

// hero slideshow: one panel on phones, three on wide screens, always showing different photos
if (hero) {
  const cols = [...hero.querySelectorAll('.col')];
  const total = cols[0].children.length;
  const num = hero.querySelector('.num');
  const prog = hero.querySelector('.progress b');
  const wide = matchMedia('(min-width: 901px)');
  const shown = cols.map((_, c) => c % total);
  const paint = c => [...cols[c].children].forEach((img, k) => img.classList.toggle('active', k === shown[c]));
  const restartBar = () => { prog.classList.remove('run'); void prog.offsetWidth; prog.classList.add('run'); };
  cols.forEach((_, c) => paint(c));
  restartBar();
  let turn = 0;
  setInterval(() => {
    if (wide.matches) {
      // swap one panel at a time to the photo that isn't on screen
      const c = turn++ % cols.length;
      const free = [...Array(total).keys()].filter(k => !shown.includes(k));
      shown[c] = free.length ? free[0] : (shown[c] + 1) % total;
      paint(c);
    } else {
      shown[0] = (shown[0] + 1) % total;
      paint(0);
      num.textContent = String(shown[0] + 1).padStart(2, '0');
      restartBar();
    }
  }, 2500);
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
