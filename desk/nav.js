// The desk's masthead and menu, the same on every page (the dashboards included): "Markets Desk", the page and
// date, search, light/dark and the newsletter link, then two rows: the markets and the record (Egypt, United States,
// Global | Views, The week, Runs), and under a market its pages (Egypt: Dashboard, EGP, EGX, Stocks; United States:
// Dashboard, Wall Street, Stocks). A stock page sits under its own market.
(function () {
  const TOP = [['egypt', 'Egypt', '/desk/egypt/'], ['us', 'United States', '/desk/usa/'], ['global', 'Global', '/desk/global/'], null,
    ['views', 'Views', '/desk/views/'], ['week', 'The week', '/desk/week/'], ['runs', 'Runs', '/desk/runs/']];
  const SUB = {
    egypt: [['Dashboard', '/desk/egypt/'], ['EGP', '/desk/egp/'], ['EGX', '/desk/egx/'], ['Stocks', '/desk/stocks/egypt/'], ['Sectors', '/desk/sectors/'], ['Fair value', '/desk/fairvalue/']],
    us: [['Dashboard', '/desk/usa/'], ['Wall Street', '/desk/us/'], ['Stocks', '/desk/stocks/us/'], ['Fair value', '/desk/fairvalue/?m=us']],
  };
  // which market and page a path belongs to, and the masthead's label
  function where(path, egxStock) {
    const p = path.replace(/index\.html$/, '');
    if (p === '/desk/fairvalue/') return /[?&]m=us/.test(location.search) ? { top: 'us', sub: '/desk/fairvalue/?m=us', label: 'Wall Street fair value' } : { top: 'egypt', sub: '/desk/fairvalue/', label: 'EGX fair value' };
    for (const [k, list] of Object.entries(SUB)) for (const [n, h] of list) if (p === h) return { top: k, sub: h, label: k === 'egypt' ? (n === 'Dashboard' ? 'Egypt' : n === 'Stocks' ? 'EGX stocks' : n === 'Sectors' ? 'EGX sectors' : n) : (n === 'Dashboard' ? 'United States' : n === 'Stocks' ? 'Wall Street stocks' : n) };
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
.dm-n1{position:relative}
.dm-n1 .dm-listen{padding:12px 0 9px;border:0;border-bottom:2px solid transparent;background:none;font:inherit;font-size:12px;line-height:16px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);white-space:nowrap;cursor:pointer}
.dm-n1 .dm-listen:hover,.dm-n1 .dm-listen.on{color:var(--text)}
.dm-n1 .dm-rate{display:none;padding:12px 0 9px;border:0;background:none;font:inherit;font-size:12px;line-height:16px;letter-spacing:.06em;color:var(--muted);cursor:pointer}
.dm-n1.playing .dm-rate{display:inline}
.dm-pbar{position:absolute;left:0;right:0;bottom:-1px;height:3px;display:none;cursor:pointer}
.dm-n1.playing .dm-pbar{display:block}
.dm-pbar i{display:block;height:100%;width:0;background:var(--text)}
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
}
/* phones (640px and narrower): a compact header that stays at the top (Egypt, US and Global as a switch, the market's
   pages as chips), search and light/dark as icons, and a tab bar at the bottom; built by phone() below */
.dp-tabs,.dp-ib,.dp-sheet,.dp-short{display:none}
/* the bottom bar's space below: the home bar's inset, and in the home-screen app a little more, clear of the home bar */
:root{--dp-safe:env(safe-area-inset-bottom,0px)}
@media (display-mode:standalone){:root{--dp-safe:calc(env(safe-area-inset-bottom,0px) + 8px)}}
@media (max-width:640px){
  .dmast{position:sticky;top:0;z-index:40;background:var(--ground);padding:env(safe-area-inset-top) 16px 0;transition:box-shadow .2s}
  .dmast.dp-stuck{box-shadow:0 1px 0 var(--border),0 6px 18px rgba(0,0,0,.06)}
  .dm-phone{display:none;padding:0 0 10px}
  .dmast.dp-find .dm-phone{display:flex}
  .dm-phone > a{display:none}
  .dm-phone .dsearch{height:44px}
  .dm-phone .dsearch input{font-size:16px}
  .dm-top{display:grid;grid-template-columns:minmax(0,1fr) auto auto;align-items:center;column-gap:4px;padding:8px 0;border-bottom:0}
  .dm-top .dm-name{grid-column:1;grid-row:1} .dm-top .dm-label{grid-column:1;grid-row:2;margin-top:2px} .dm-top .dp-ib{grid-row:1 / 3}
  .dm-name{font-size:22px}
  .dm-n1 a .dp-full{display:none} .dm-n1 a .dp-short{display:inline}
  .dp-ib{display:grid;place-items:center;flex:none;width:44px;height:44px;padding:0;border:0;background:none;color:var(--text);cursor:pointer}
  .dp-ib svg{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
  .dm-n1{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:2px;padding:3px;margin:0 0 2px;border:1px solid var(--border);background:var(--raised);overflow:visible}
  .dm-n1 a{display:none;padding:0;min-height:38px;align-items:center;justify-content:center;border:0;font-size:12px;letter-spacing:.08em}
  .dm-n1 a[data-k="egypt"],.dm-n1 a[data-k="us"],.dm-n1 a[data-k="global"]{display:flex}
  .dm-n1 a[aria-current]{background:var(--surface);box-shadow:0 1px 2px rgba(0,0,0,.08);border:0}
  .dm-n1 .dm-sep,.dm-n1 .dm-listen,.dm-n1 .dm-rate{display:none!important}
  .dm-n1 .dm-pbar{bottom:-3px}
  .dm-n1.dp-other{display:none}
  .dm-n2{gap:8px;padding:8px 16px;margin:0 -16px;border-bottom:1px solid var(--border)}
  .dm-n2 a{display:inline-flex;align-items:center;min-height:34px;padding:0 13px;border:1px solid var(--border);border-radius:999px;font-size:13px;color:var(--text)}
  .dm-n2 a[aria-current]{background:var(--text);border-color:var(--text);color:var(--ground);font-weight:600}
  body{padding-bottom:calc(60px + var(--dp-safe))}
  .dp-tabs{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));position:fixed;left:0;right:0;bottom:0;z-index:45;padding:0 4px var(--dp-safe);background:var(--ground);border-top:1px solid var(--text)}
  .dp-tabs a,.dp-tabs button{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;height:58px;padding:0;border:0;background:none;color:var(--muted);font:600 10.5px/1 var(--font);text-decoration:none;cursor:pointer;-webkit-tap-highlight-color:transparent;position:relative}
  .dp-tabs svg{width:23px;height:23px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
  .dp-tabs [aria-current],.dp-tabs .on{color:var(--accent)}
  .dp-tabs [aria-current] svg,.dp-tabs .on svg{stroke-width:2.2}
  .dp-tabs .dp-ring{position:absolute;left:12%;right:12%;top:0;height:2px;background:var(--accent);transform-origin:0 50%;transform:scaleX(var(--p,0))}
  .dp-sheet{display:block;position:fixed;inset:0;z-index:60;visibility:hidden}
  .dp-sheet.on{visibility:visible}
  .dp-scrim{position:absolute;inset:0;background:rgba(0,0,0,.4);opacity:0;transition:opacity .25s}
  .dp-sheet.on .dp-scrim{opacity:1}
  .dp-panel{position:absolute;left:0;right:0;bottom:0;max-height:80vh;overflow-y:auto;background:var(--ground);border-top:3px double var(--text);border-radius:14px 14px 0 0;padding:6px 16px calc(16px + var(--dp-safe));transform:translateY(100%);transition:transform .3s cubic-bezier(.2,.7,.2,1)}
  .dp-sheet.on .dp-panel{transform:none}
  .dp-grab{width:40px;height:5px;margin:2px auto 8px;border-radius:3px;background:var(--border)}
  .dp-h{margin:14px 0 4px;font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
  .dp-list a{display:flex;justify-content:space-between;align-items:center;min-height:50px;border-bottom:1px solid var(--border);color:var(--text);text-decoration:none;font:500 17px/1.25 var(--serif)}
  .dp-list a::after{content:"\\203A";color:var(--muted);font:400 22px var(--font)}
  .dp-list a[aria-current]{font-weight:700}
  .dp-seg{display:grid;grid-template-columns:1fr 1fr;border:1px solid var(--text);margin-top:8px}
  .dp-seg button{min-height:42px;border:0;background:none;color:var(--text);font:600 12px var(--font);letter-spacing:.08em;text-transform:uppercase;cursor:pointer}
  .dp-seg button + button{border-left:1px solid var(--text)}
  .dp-seg button[aria-pressed="true"]{background:var(--text);color:var(--ground)}
  .dp-save{display:block;width:100%;margin-top:8px;padding:12px 14px;border:1px solid var(--text);background:none;color:var(--text);text-align:left;font:inherit;cursor:pointer}
  .dp-save b{display:block;font:600 12px var(--font);letter-spacing:.08em;text-transform:uppercase}
  .dp-save small{display:block;margin-top:4px;font-size:13px;opacity:.75}
  .dp-save:disabled{opacity:.6;cursor:progress}
}
@media (max-width:640px) and (prefers-reduced-motion:reduce){.dp-panel,.dp-scrim,.dm-top{transition:none}}
@media print{.dp-tabs,.dp-sheet,.dp-ib{display:none!important}}`;
  function mount(path, NAMES, GROUP) {
    if (document.querySelector('.dmast')) return;
    const t = new URLSearchParams(location.search).get('t'), egxStock = !!(t && GROUP && GROUP.egx.includes(t));
    const w = where(path, egxStock);
    const st = document.createElement('style'); st.textContent = CSS; document.head.appendChild(st);
    const dark = document.documentElement.getAttribute('data-theme') === 'dark';
    // Runs (how the daily runs went) is about the site, not the markets: it sits apart, at the right of the row
    const top = TOP.map((x) => x ? `<a data-k="${x[0]}" href="${x[2]}"${x[0] === w.top ? ' aria-current="page"' : ''}${x[0] === 'runs' ? ' class="dm-runs"' : ''}>${x[1]}</a>` : '<span class="dm-sep" aria-hidden="true"></span>').join('');
    const sub = w.top && SUB[w.top] ? `<nav class="dm-n2" aria-label="${w.top === 'egypt' ? 'Egypt' : 'United States'}">${SUB[w.top].map(([n, h]) => `<a href="${h}"${h === w.sub ? ' aria-current="page"' : ''}>${n}</a>`).join('')}</nav>` : '';
    const hd = document.createElement('header'); hd.className = 'dmast';
    hd.innerHTML = `<div class="dm-phone">${SEARCH}<a href="/">Newsletter →</a></div>
      <div class="dm-top"><a class="dm-name" href="/desk/">Markets Desk</a><span class="dm-label" id="dm-label">${esc(w.label)}</span>
      <div class="dm-tools">${SEARCH}<button type="button" class="dm-theme">${dark ? 'Light' : 'Dark'}</button><a href="/">Newsletter →</a></div></div>
      <nav class="dm-n1" aria-label="Markets Desk">${top}</nav>${sub}`;
    document.body.prepend(hd);
    // light and dark switch in place: the colours are the stylesheet's, and the charts redraw themselves on the
    // 'deskthemechange' event (charts.js), so the page does not reload
    const tbtn = hd.querySelector('.dm-theme');
    const setTheme = (d) => {
      document.documentElement.setAttribute('data-theme', d ? 'dark' : 'light');
      tbtn.textContent = d ? 'Light' : 'Dark';
      window.dispatchEvent(new Event('deskthemechange'));
    };
    tbtn.addEventListener('click', () => {
      const d = document.documentElement.getAttribute('data-theme') !== 'dark';
      try { localStorage.setItem('deskTheme', d ? 'dark' : 'light'); } catch (e) {}
      const go = () => setTheme(d);
      if (document.startViewTransition) document.startViewTransition(go); else go();
    });
    // a page loaded ahead in the background (see speculate below), or one brought back from the browser's cache, takes
    // the theme chosen since
    const resync = () => { let t = null; try { t = localStorage.getItem('deskTheme'); } catch (e) {} const d = t ? t === 'dark' : document.documentElement.getAttribute('data-theme') === 'dark'; if (d !== (document.documentElement.getAttribute('data-theme') === 'dark')) setTheme(d); };
    document.addEventListener('prerenderingchange', resync);
    addEventListener('pageshow', (e) => { if (e.persisted) resync(); });
    speculate();
    const go = (f) => hd.querySelectorAll('.dsearch').forEach((x) => f(x, NAMES, GROUP));
    if (window.DeskSearch) go(window.DeskSearch);
    else { const sc = document.createElement('script'); sc.src = '/desk/search.js'; sc.onload = () => go(window.DeskSearch); document.head.appendChild(sc); }
    figures(hd);
    listen(hd);
    // the current tab stays in view on a phone
    hd.querySelectorAll('[aria-current]').forEach((a) => { const n = a.parentElement; n.scrollLeft = Math.max(0, a.offsetLeft - 16); });
    offline(null);
    phone(hd, w);
  }
  // the phone layout's parts: search and light/dark as icons in the name row, a tab bar (the market's dashboard, its
  // stocks, the views, the day read aloud, and More), a More sheet, and the header that tucks its name row away once
  // you scroll. CSS above; nothing shows wider than 640px.
  function phone(hd, w) {
    const ico = (d) => `<svg viewBox="0 0 24 24" aria-hidden="true">${d}</svg>`;
    const I = {
      find: '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
      moon: '<path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/>',
      today: '<rect x="3" y="3" width="8" height="8"/><rect x="13" y="3" width="8" height="5"/><rect x="13" y="10" width="8" height="11"/><rect x="3" y="13" width="8" height="8"/>',
      stocks: '<path d="M4 17l5-5 4 3 7-8"/><path d="M15 7h5v5"/>',
      views: '<path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
      listen: '<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="14" width="4" height="6" rx="1.5"/><rect x="17" y="14" width="4" height="6" rx="1.5"/>',
      pause: '<path d="M8 5v14M16 5v14"/>',
      more: '<path d="M4 6h16M4 12h16M4 18h16"/>',
    };
    const topRow = hd.querySelector('.dm-top');
    const find = document.createElement('button'); find.type = 'button'; find.className = 'dp-ib'; find.setAttribute('aria-label', 'Find a stock'); find.innerHTML = ico(I.find);
    const moon = document.createElement('button'); moon.type = 'button'; moon.className = 'dp-ib'; moon.setAttribute('aria-label', 'Light or dark'); moon.innerHTML = ico(I.moon);
    const tools = topRow.querySelector('.dm-tools'); topRow.insertBefore(find, tools); topRow.insertBefore(moon, tools);
    find.addEventListener('click', () => { const on = hd.classList.toggle('dp-find'); if (on) { const i = hd.querySelector('.dm-phone input'); if (i) i.focus(); } });
    moon.addEventListener('click', () => hd.querySelector('.dm-theme').click());
    // a page outside the three markets (Views, The week, Runs) has no market switch: its name says where you are
    if (!['egypt', 'us', 'global'].includes(w.top)) hd.querySelector('.dm-n1').classList.add('dp-other');
    const mk = w.top === 'us' ? 'us' : w.top === 'global' ? 'global' : 'egypt';
    const dash = { egypt: '/desk/egypt/', us: '/desk/usa/', global: '/desk/global/' }[mk];
    const stocks = mk === 'us' ? '/desk/stocks/us/' : '/desk/stocks/egypt/';
    const p = location.pathname;
    const tabs = document.createElement('nav'); tabs.className = 'dp-tabs'; tabs.setAttribute('aria-label', 'Desk');
    tabs.innerHTML = `<a href="${dash}"${p === dash ? ' aria-current="page"' : ''}>${ico(I.today)}Today</a>`
      + `<a href="${stocks}"${/^\/desk\/(stocks|stock)\//.test(p) ? ' aria-current="page"' : ''}>${ico(I.stocks)}Stocks</a>`
      + `<a href="/desk/views/"${p === '/desk/views/' ? ' aria-current="page"' : ''}>${ico(I.views)}Views</a>`
      + `<button type="button" class="dp-listen" aria-label="Listen to the day">${ico(I.listen)}<span>Listen</span><i class="dp-ring"></i></button>`
      + `<button type="button" class="dp-more">${ico(I.more)}More</button>`;
    document.body.appendChild(tabs);
    // Listen plays the desk's audio through the header's own player (made by listen() once the day's file is found)
    const lt = tabs.querySelector('.dp-listen');
    lt.addEventListener('click', () => {
      const b = hd.querySelector('.dm-listen');
      if (!b) { lt.querySelector('span').textContent = 'No audio'; setTimeout(() => { lt.querySelector('span').textContent = 'Listen'; }, 1800); return; }
      b.click();
    });
    new MutationObserver(() => {
      const n1 = hd.querySelector('.dm-n1'), playing = n1.classList.contains('playing'), on = !!hd.querySelector('.dm-listen.on');
      lt.classList.toggle('on', playing);
      lt.firstElementChild.innerHTML = on ? I.pause : I.listen;
      lt.querySelector('span').textContent = on ? 'Pause' : playing ? 'Resume' : 'Listen';
      const i = n1.querySelector('.dm-pbar i'); if (i) lt.querySelector('.dp-ring').style.setProperty('--p', (parseFloat(i.style.width) || 0) / 100);
    }).observe(hd.querySelector('.dm-n1'), { subtree: true, attributes: true, childList: true, characterData: true });
    // More: every page of the desk, light or dark, and the newsletter
    const sheet = document.createElement('div'); sheet.className = 'dp-sheet';
    const link = (h, n) => `<a href="${h}"${(p + location.search) === h || p === h ? ' aria-current="page"' : ''}>${n}</a>`;
    const egx = SUB.egypt.map(([n, h]) => link(h, n === 'Dashboard' ? 'Egypt dashboard' : n === 'Stocks' ? 'EGX stocks' : n)).join('');
    const us = SUB.us.map(([n, h]) => link(h, n === 'Dashboard' ? 'United States dashboard' : n === 'Stocks' ? 'Wall Street stocks' : n === 'Fair value' ? 'Wall Street fair value' : n)).join('');
    sheet.innerHTML = `<div class="dp-scrim"></div><div class="dp-panel" role="dialog" aria-modal="true" aria-label="More"><div class="dp-grab"></div>`
      + `<p class="dp-h">Egypt</p><div class="dp-list">${egx}</div>`
      + `<p class="dp-h">United States</p><div class="dp-list">${us}</div>`
      + `<p class="dp-h">The desk</p><div class="dp-list">${link('/desk/global/', 'Global')}${link('/desk/views/', 'Views')}${link('/desk/week/', 'The week')}${link('/desk/runs/', 'Runs')}<a href="/">Daily Newsletter</a></div>`
      + `<p class="dp-h">Look</p><div class="dp-seg"><button type="button" data-d="0">Light</button><button type="button" data-d="1">Dark</button></div>`
      + `<p class="dp-h">Offline</p><button type="button" class="dp-save"><b>Save the desk to this phone</b><small></small></button></div>`;
    document.body.appendChild(sheet);
    const segSync = () => { const d = document.documentElement.getAttribute('data-theme') === 'dark'; sheet.querySelectorAll('.dp-seg button').forEach((b) => b.setAttribute('aria-pressed', String((b.dataset.d === '1') === d))); };
    sheet.querySelector('.dp-seg').addEventListener('click', (e) => { const b = e.target.closest('button'); if (!b) return; if ((b.dataset.d === '1') !== (document.documentElement.getAttribute('data-theme') === 'dark')) hd.querySelector('.dm-theme').click(); segSync(); });
    offline(sheet.querySelector('.dp-save'));
    const open = (on) => { sheet.classList.toggle('on', on); document.body.style.overflow = on ? 'hidden' : ''; if (on) segSync(); };
    tabs.querySelector('.dp-more').addEventListener('click', () => open(true));
    sheet.querySelector('.dp-scrim').addEventListener('click', () => open(false));
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') open(false); });
    const pnl = sheet.querySelector('.dp-panel'); let y0 = null, dy = 0;
    pnl.addEventListener('touchstart', (e) => { if (pnl.scrollTop > 0) return; y0 = e.touches[0].clientY; dy = 0; }, { passive: true });
    pnl.addEventListener('touchmove', (e) => { if (y0 === null) return; dy = Math.max(0, e.touches[0].clientY - y0); if (dy > 4) { pnl.style.transition = 'none'; pnl.style.transform = `translateY(${dy}px)`; } }, { passive: true });
    pnl.addEventListener('touchend', () => { if (y0 === null) return; pnl.style.transition = ''; pnl.style.transform = ''; if (dy > 90) open(false); y0 = null; });
    // the name row scrolls away with the page and the market switch and the page chips stay at the top: the header
    // sticks that far above the screen's top edge (all of it shows while the search field is open)
    const usTab = hd.querySelector('.dm-n1 a[data-k="us"]'); if (usTab) usTab.innerHTML = '<span class="dp-full">United States</span><span class="dp-short">US</span>' + usTab.innerHTML.replace('United States', '');
    const fit = () => { hd.style.top = (!matchMedia('(max-width:640px)').matches || hd.classList.contains('dp-find')) ? '' : -(topRow.offsetHeight + (parseFloat(getComputedStyle(hd).paddingTop) || 0)) + 'px'; };
    fit(); addEventListener('resize', fit); find.addEventListener('click', fit);
    let tk = false;
    addEventListener('scroll', () => { if (tk) return; tk = true; requestAnimationFrame(() => { tk = false; hd.classList.toggle('dp-stuck', scrollY > topRow.offsetHeight); }); }, { passive: true });
  }
  // pages change without a blank reload: the browser loads a desk page in the background as soon as the pointer rests on
  // its link (Chrome and Edge, through speculation rules), and desk.css and dash.css cross-fade one page into the next
  function speculate() {
    if (document.querySelector('script[type=speculationrules]') || !(HTMLScriptElement.supports && HTMLScriptElement.supports('speculationrules'))) return;
    const sr = document.createElement('script'); sr.type = 'speculationrules';
    const rules = [{ where: { and: [{ href_matches: '/desk/*' }, { not: { href_matches: '/desk/*.json' } }, { not: { selector_matches: '[download]' } }] }, eagerness: 'moderate' }];
    // the pages of the market being read are the likely next clicks: they load straight away (at most four, and not on
    // a slow or data-saving connection); the rest load when the pointer rests on their link
    const c = navigator.connection || {};
    const top = where(location.pathname, false).top;
    const phone = matchMedia('(pointer: coarse)').matches;
    if (top && SUB[top] && !phone && !c.saveData && !/(^|-)2g|3g/.test(c.effectiveType || '')) {
      const here = location.pathname + location.search;
      const urls = SUB[top].map(([, h]) => h).filter((h) => h !== here && h !== location.pathname).slice(0, 4);
      if (urls.length) rules.unshift({ source: 'list', urls, eagerness: 'immediate' });
    }
    sr.textContent = JSON.stringify({ prerender: rules });
    document.head.appendChild(sr);
  }
  // the desk read aloud (desk_audio.py): "Listen to the day" at the right of the top row, after Runs, on every desk page;
  // while it plays a thin bar along the row shows how far it has got (a click on the bar jumps there)
  function listen(hd) {
    const n1 = hd.querySelector('.dm-n1'); if (!n1) return;
    fetch('/desk/index.json', { cache: 'no-cache' }).then((r) => r.json()).then((ix) => {
      const ds = (ix.desks || []).map((d) => d.date).sort(); const date = ds[ds.length - 1];
      return date ? fetch('/data/audio/desk-' + date + '.json', { cache: 'no-cache' }).then((r) => r.ok ? r.json() : null) : null;
    }).then((m) => {
      const v = m && m.voices && m.voices[0]; if (!v || !v.url) return;
      const url = /^https?:/.test(v.url) ? v.url : '/' + v.url.replace(/^\//, '');
      const b = document.createElement('button'); b.type = 'button'; b.className = 'dm-listen'; b.textContent = 'Listen to the day';
      const rt = document.createElement('button'); rt.type = 'button'; rt.className = 'dm-rate'; rt.textContent = '1×'; rt.setAttribute('aria-label', 'Playback speed');
      const bar = document.createElement('span'); bar.className = 'dm-pbar'; bar.innerHTML = '<i></i>';
      n1.append(b, rt, bar);
      const au = new Audio(); au.preload = 'none';
      const fmt = (t) => Math.floor(t / 60) + ':' + ('0' + Math.floor(t % 60)).slice(-2);
      const RATES = [1, 1.25, 1.5, 0.85];
      b.addEventListener('click', () => { if (!au.src) au.src = url; if (au.paused) au.play().catch(() => {}); else au.pause(); });
      au.addEventListener('play', () => { n1.classList.add('playing'); b.classList.add('on'); });
      au.addEventListener('pause', () => { b.classList.remove('on'); if (!au.ended) b.textContent = 'Resume · ' + fmt(au.currentTime) + ' / ' + fmt(au.duration || v.duration || 0); });
      au.addEventListener('timeupdate', () => { if (!au.duration) return; bar.firstChild.style.width = (au.currentTime / au.duration * 100) + '%'; if (!au.paused) b.textContent = 'Pause · ' + fmt(au.currentTime) + ' / ' + fmt(au.duration); });
      au.addEventListener('ended', () => { n1.classList.remove('playing'); b.classList.remove('on'); b.textContent = 'Listen to the day'; bar.firstChild.style.width = '0'; });
      rt.addEventListener('click', () => { const r = RATES[(RATES.indexOf(au.playbackRate) + 1) % RATES.length]; au.playbackRate = r; rt.textContent = r + '×'; });
      bar.addEventListener('click', (e) => { if (!au.duration) return; const r = bar.getBoundingClientRect(); au.currentTime = (e.clientX - r.left) / r.width * au.duration; });
    }).catch(() => {});
  }
  // the desk's offline copy (desk/sw.js): pages open from it at once and refresh in the background; the More menu's
  // button saves every page and data file, so the whole desk reads without a connection
  function offline(btn) {
    if (!('serviceWorker' in navigator)) { if (btn) btn.hidden = true; return; }
    const sw = navigator.serviceWorker;
    sw.register('/desk/sw.js', { scope: '/desk/' }).catch(() => {});
    if (!btn) return;
    const sm = btn.querySelector('small');
    const when = (iso) => new Date(iso).toLocaleString('en-US', { weekday: 'short', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' });
    let last = null; try { last = localStorage.getItem('deskSaved'); } catch (e) {}
    sm.textContent = last ? 'Saved ' + when(last) + '. Tap to update.' : 'Every page and figure, for reading without a connection.';
    sw.addEventListener('message', (e) => {
      const m = e.data || {}; if (m.total == null) return;
      if (!m.finished) { sm.textContent = `Saving… ${m.saved} of ${m.total}`; return; }
      btn.disabled = false;
      if (m.failed) { sm.textContent = `Saved ${m.total - m.failed} of ${m.total}; tap to try again.`; return; }
      try { localStorage.setItem('deskSaved', m.at); } catch (e) {}
      sm.textContent = 'Saved ' + when(m.at) + '. Tap to update.';
    });
    btn.addEventListener('click', async () => {
      btn.disabled = true; sm.textContent = 'Saving…';
      try { const r = await sw.ready; (r.active || sw.controller).postMessage({ save: true }); } catch (e) { btn.disabled = false; sm.textContent = 'Could not save: try again.'; }
    });
  }
  // the day's headline figure beside a market's name and pages (laptop only): the EGX30's and S&P 500's day change and
  // the central bank's dollar rate, from the data log; a day the market was shut repeats the last close, so the change
  // is measured from the last different one
  function figures(hd) {
    ((window.__deskGet && window.__deskGet['/data/markets-recent.json']) || fetch('/data/markets-recent.json').then((r) => r.json())).then((L) => {
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
