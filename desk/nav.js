// The desk's masthead and menu, the same on every page (the dashboards included): "Markets Desk", the page and
// date, search, light/dark and the newsletter link, then two rows: the markets and the record (Egypt, United States,
// Global | Views, The week, Runs), and under a market its pages (Egypt: Dashboard, EGP, EGX, Stocks; United States:
// Dashboard, Wall Street, Stocks). A stock page sits under its own market.
(function () {
  const TOP = [['egypt', 'Egypt', '/desk/egypt/'], ['us', 'United States', '/desk/usa/'], ['global', 'Global', '/desk/global/'], null,
    ['views', 'Views', '/desk/views/'], ['week', 'The week', '/desk/week/'], ['runs', 'Runs', '/desk/runs/']];
  const SUB = {
    egypt: [['Dashboard', '/desk/egypt/'], ['EGP', '/desk/egp/'], ['EGX', '/desk/egx/'], ['Stocks', '/desk/stocks/egypt/']],
    us: [['Dashboard', '/desk/usa/'], ['Wall Street', '/desk/us/'], ['Stocks', '/desk/stocks/us/']],
  };
  // which market and page a path belongs to, and the masthead's label
  function where(path, egxStock) {
    const p = path.replace(/index\.html$/, '');
    for (const [k, list] of Object.entries(SUB)) for (const [n, h] of list) if (p === h) return { top: k, sub: h, label: k === 'egypt' ? (n === 'Dashboard' ? 'Egypt' : n === 'Stocks' ? 'EGX stocks' : n) : (n === 'Dashboard' ? 'United States' : n === 'Stocks' ? 'Wall Street stocks' : n) };
    if (p === '/desk/stock/') return egxStock ? { top: 'egypt', sub: '/desk/stocks/egypt/', label: 'Egypt · Stocks' } : { top: 'us', sub: '/desk/stocks/us/', label: 'United States · Stocks' };
    for (const x of TOP) if (x && p === x[2]) return { top: x[0], sub: null, label: x[1] };
    return { top: null, sub: null, label: '' };
  }
  const esc = (s) => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;');
  const SEARCH = '<div class="dsearch" role="search"><svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="7" cy="7" r="4.5"/><path d="M10.5 10.5L14 14"/></svg><input type="search" placeholder="Find a stock" aria-label="Find a stock" autocomplete="off" spellcheck="false"><div class="dsr" role="listbox" hidden></div></div>';
  const CSS = `
.dmast{margin:0 auto;max-width:1440px;padding:0 48px}
.dm-top{display:flex;align-items:baseline;gap:18px;padding:18px 0 10px;border-bottom:3px double var(--text)}
.dm-name{font:700 27px/1.1 var(--serif);letter-spacing:-.01em;color:var(--text);text-decoration:none;white-space:nowrap}
.dm-label{font-size:11px;line-height:16px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.dm-tools{margin-left:auto;display:flex;align-items:center;gap:16px;font-size:12px;color:var(--muted);align-self:center}
.dm-tools .dsearch{margin:0;width:190px;height:32px;border-radius:0;background:transparent}
.dm-tools a,.dm-tools button{color:var(--muted);text-decoration:none;background:none;border:0;padding:0;cursor:pointer;font:inherit;white-space:nowrap}
.dm-tools a:hover,.dm-tools button:hover{color:var(--text)}
.dm-n1,.dm-n2{display:flex;align-items:stretch;gap:26px;border-bottom:1px solid var(--border);overflow-x:auto;scrollbar-width:none}
.dm-n1::-webkit-scrollbar,.dm-n2::-webkit-scrollbar{display:none}
.dm-n1 a{padding:12px 0 9px;font-size:12px;line-height:16px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);text-decoration:none;white-space:nowrap;border-bottom:2px solid transparent}
.dm-n1 a[aria-current]{color:var(--text);font-weight:600;border-bottom-color:var(--text)}
.dm-n1 .dm-sep{width:1px;margin:11px 0;background:var(--border);flex:none}
.dm-n2 a{padding:10px 0 8px;font-size:13px;line-height:18px;color:var(--muted);text-decoration:none;white-space:nowrap;border-bottom:2px solid transparent}
.dm-n2 a[aria-current]{color:var(--accent);font-weight:600;border-bottom-color:var(--accent)}
.dm-n1 a:hover,.dm-n2 a:hover{color:var(--text)}
.dm-n2{align-items:center} .dm-stamp{margin-left:auto;padding-left:24px;font-size:11px;line-height:16px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);white-space:nowrap}
.dm-n1 .dm-runs{margin-left:auto}
.dm-fig{margin-left:7px;font-size:11.5px;font-weight:500;letter-spacing:0;font-variant-numeric:tabular-nums;color:var(--muted)}
.dm-fig.up{color:var(--positive)} .dm-fig.down{color:var(--negative)}
.dm-phone{display:none}
@media (max-width:860px){
  .dmast{padding:0 16px}
  .dm-phone{display:flex;align-items:center;gap:10px;padding:10px 0 0}
  .dm-phone .dsearch{flex:1;margin:0;height:34px;border-radius:0;background:transparent}
  .dm-phone a{font-size:12px;color:var(--muted);text-decoration:none;white-space:nowrap}
  .dm-top{display:block;padding:10px 0 8px}
  .dm-name{font-size:23px}
  .dm-label{display:block;margin-top:3px;font-size:10px}
  .dm-tools{display:none}
  .dm-n1{gap:18px} .dm-n1 a{font-size:11px;padding:11px 0 8px}
  .dm-n2{gap:20px} .dm-stamp{display:none} .dm-fig{display:none}
}`;
  function mount(path, NAMES, GROUP) {
    if (document.querySelector('.dmast')) return;
    const t = new URLSearchParams(location.search).get('t'), egxStock = !!(t && GROUP && GROUP.egx.includes(t));
    const w = where(path, egxStock);
    const st = document.createElement('style'); st.textContent = CSS; document.head.appendChild(st);
    const dark = document.documentElement.getAttribute('data-theme') === 'dark';
    // Runs (how the daily runs went) is about the site, not the markets: it sits apart, at the right of the row
    const top = TOP.map((x) => x ? `<a href="${x[2]}"${x[0] === w.top ? ' aria-current="page"' : ''}${x[0] === 'runs' ? ' class="dm-runs"' : ''}>${x[1]}</a>` : '<span class="dm-sep" aria-hidden="true"></span>').join('');
    const sub = w.top && SUB[w.top] ? `<nav class="dm-n2" aria-label="${w.top === 'egypt' ? 'Egypt' : 'United States'}">${SUB[w.top].map(([n, h]) => `<a href="${h}"${h === w.sub ? ' aria-current="page"' : ''}>${n}</a>`).join('')}</nav>` : '';
    const hd = document.createElement('header'); hd.className = 'dmast';
    hd.innerHTML = `<div class="dm-phone">${SEARCH}<a href="/">Newsletter →</a></div>
      <div class="dm-top"><a class="dm-name" href="/desk/">Markets Desk</a><span class="dm-label" id="dm-label">${esc(w.label)}</span>
      <div class="dm-tools">${SEARCH}<button type="button" class="dm-theme">${dark ? 'Light' : 'Dark'}</button><a href="/">Newsletter →</a></div></div>
      <nav class="dm-n1" aria-label="Markets Desk">${top}</nav>${sub}`;
    document.body.prepend(hd);
    hd.querySelector('.dm-theme').addEventListener('click', () => {
      const d = document.documentElement.getAttribute('data-theme') !== 'dark';
      if (d) document.documentElement.setAttribute('data-theme', 'dark'); else document.documentElement.setAttribute('data-theme', 'light');
      try { localStorage.setItem('theme', d ? 'dark' : 'light'); } catch (e) {}
      location.reload();
    });
    const go = (f) => hd.querySelectorAll('.dsearch').forEach((x) => f(x, NAMES, GROUP));
    if (window.DeskSearch) go(window.DeskSearch);
    else { const sc = document.createElement('script'); sc.src = '/desk/search.js'; sc.onload = () => go(window.DeskSearch); document.head.appendChild(sc); }
    figures(hd);
    // the current tab stays in view on a phone
    hd.querySelectorAll('[aria-current]').forEach((a) => { const n = a.parentElement; n.scrollLeft = Math.max(0, a.offsetLeft - 16); });
  }
  // the day's headline figure beside a market's name and pages (laptop only): the EGX30's and S&P 500's day change and
  // the central bank's dollar rate, from the data log; a day the market was shut repeats the last close, so the change
  // is measured from the last different one
  function figures(hd) {
    fetch('/data/markets-recent.json').then((r) => r.json()).then((L) => {
      const days = L.days || [];
      const chg = (k) => { const v = days.map((e) => e[k]).filter((x) => typeof x === 'number'); if (v.length < 2) return null; const now = v[v.length - 1]; let i = v.length - 2; while (i > 0 && v[i] === now) i--; return v[i] === now ? null : (now / v[i] - 1) * 100; };
      const pct = (c) => c == null ? null : [(c >= 0 ? '+' : '\u2212') + Math.abs(c).toFixed(2) + '%', c >= 0 ? 'up' : 'down'];
      const usd = days.map((e) => e.usd_egp).filter((x) => typeof x === 'number').pop();
      const F = { '/desk/egypt/': pct(chg('egx30')), '/desk/egx/': pct(chg('egx30')), '/desk/usa/': pct(chg('sp500')), '/desk/us/': pct(chg('sp500')), '/desk/egp/': usd ? [usd.toFixed(2), ''] : null };
      hd.querySelectorAll('.dm-n1 a, .dm-n2 a').forEach((a) => {
        const f = F[a.getAttribute('href')]; if (!f || a.querySelector('.dm-fig')) return;
        if (a.closest('.dm-n2') && /^\/desk\/(egypt|usa)\/$/.test(a.getAttribute('href'))) return;   // the Dashboard tab carries no figure: its market's name above does
        const sp = document.createElement('span'); sp.className = 'dm-fig ' + f[1]; sp.textContent = f[0]; a.appendChild(sp);
      });
    }).catch(() => {});
  }
  // the desk's date beside the name (a dateline), once the day's desk is known; the page's own name is its title
  function label(text) { const el = document.getElementById('dm-label'); if (el) el.textContent = text; }
  // how current the page's figures are (the dashboards' closes and fetch time), on the right of the market's row
  function stamp(text) { const n2 = document.querySelector('.dm-n2'); if (!n2) return false; let el = n2.querySelector('.dm-stamp'); if (!el) { el = document.createElement('span'); el.className = 'dm-stamp'; n2.appendChild(el); } el.textContent = text; return true; }
  window.DeskNav = { mount, label, stamp };
})();
