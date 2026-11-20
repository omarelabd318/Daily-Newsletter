// The opening screen shown when the Daily Newsletter or the Markets Desk is launched from the home screen.
// Loaded in <head> of the start page with data-app ("news" or "desk"), data-look (1, 2 or 3) and data-ready (a CSS
// selector that has content once the page is ready):
//   <script src="/splash.js" data-app="news" data-look="2" data-ready="#content > *"></script>
// - Shown only when the app opens from the home screen (standalone), once per launch; links and browser tabs go
//   straight to the page.
// - Leaves as soon as the page is ready, but stays at least MIN ms so it never just flashes, and never more than MAX.
//   Exception: the newsletter on a phone stays up; once the page is ready a "Tap to open" line appears, and a tap
//   anywhere on the screen brings up the newsletter.
// - Preview in any browser: ?splash=1|2|3 shows that look; add &hold to keep it up.
(function () {
  var me = document.currentScript, d = document, root = d.documentElement;
  var app = me.dataset.app, q = new URLSearchParams(location.search), pv = q.get('splash');
  var look = +(pv || me.dataset.look || 1), hold = q.has('hold');
  var standalone = (window.matchMedia && matchMedia('(display-mode: standalone)').matches) || navigator.standalone === true;
  var seen = false; try { seen = sessionStorage.getItem('splash-' + app) === '1'; sessionStorage.setItem('splash-' + app, '1'); } catch (e) {}
  if (!pv && (!standalone || seen)) return;
  var MIN = 2200, MAX = 3500, t0 = Date.now();
  var still = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var phone = window.matchMedia && matchMedia('(pointer: coarse) and (hover: none)').matches;
  var tapOpen = app === 'news' && phone;

  // colours follow the page's own setting (the newsletter: paper unless dark; the desk: dark unless light)
  var dark = root.getAttribute('data-theme') === 'dark';
  var C = app === 'desk'
    ? (dark ? { bg: '#0e1216', ink: '#eef2f4', mute: '#949ca4', line: '#232b33', acc: '#52d6b5', up: '#5fd08a', down: '#e8605a', tile: '#151b21' }
            : { bg: '#faf8f3', ink: '#16181a', mute: '#5b6168', line: '#e6e1d5', acc: '#1a9e7f', up: '#1d7a3a', down: '#b3261e', tile: '#ffffff' })
    : (dark ? { bg: '#0e1216', ink: '#eef2f4', mute: '#a9b4be', line: '#2a333b', acc: '#52d6b5', paper: '#f4f1ea' }
            : { bg: '#faf8f3', ink: '#16181a', mute: '#5b6168', line: '#16181a', acc: '#8a1c1c', paper: '#faf8f3' });
  if (app === 'news' && look === 2) C.bg = '#0e1216'; // the sheet on the icon's dark ground, whatever the theme

  var css = '#splash{position:fixed;inset:0;z-index:2147483000;display:flex;flex-direction:column;align-items:center;justify-content:center;' +
    'padding:max(24px,env(safe-area-inset-top)) 28px max(24px,env(safe-area-inset-bottom));background:' + C.bg + ';color:' + C.ink + ';' +
    'text-align:center;-webkit-font-smoothing:antialiased;transition:opacity .32s cubic-bezier(.2,.7,.2,1),transform .32s cubic-bezier(.2,.7,.2,1)}' +
    '#splash.out{opacity:0;transform:scale(1.02);pointer-events:none}' +
    '#splash *{box-sizing:border-box;margin:0}' +
    '#splash .in{opacity:0;transform:translateY(6px);animation:sp-in .5s cubic-bezier(.2,.7,.2,1) forwards}' +
    '#splash .d1{animation-delay:.08s}#splash .d2{animation-delay:.18s}#splash .d3{animation-delay:.3s}#splash .d4{animation-delay:.42s}' +
    '#splash .late{opacity:0;transition:opacity .35s ease}#splash .late.on{opacity:1}' +
    '#splash.tap{cursor:pointer;-webkit-tap-highlight-color:transparent}' +
    '#splash .tap-hint{margin-top:26px;font:600 11px/1 Inter,system-ui,sans-serif;letter-spacing:.2em;text-transform:uppercase;color:' + C.mute + '}' +
    '#splash .tap-hint.on{animation:sp-pulse 2.2s ease-in-out .4s infinite}' +
    '@keyframes sp-pulse{0%,100%{opacity:1}50%{opacity:.45}}' +
    '@keyframes sp-in{to{opacity:1;transform:none}}' +
    '@keyframes sp-rule{from{transform:scaleX(0)}to{transform:scaleX(1)}}' +
    '@keyframes sp-draw{to{stroke-dashoffset:0}}' +
    '@keyframes sp-grow{from{transform:scale(.42);border-radius:22px}to{transform:none}}' +
    '@keyframes sp-tick{from{transform:translateX(-100%)}to{transform:translateX(250%)}}' +
    '#splash .tick{position:relative;overflow:hidden;width:56px;height:2px;background:' + C.line + '}' +
    '#splash .tick::after{content:"";position:absolute;inset:0;width:40%;background:' + C.acc + ';animation:sp-tick 1.1s ease-in-out infinite}' +
    (still ? '#splash *,#splash *::after{animation:none!important;opacity:1!important;transform:none!important;stroke-dashoffset:0!important}' : '');

  var N = {
    // 1. Masthead: the front page's nameplate, the date line and the day's summary as its deck
    1: '<div style="width:100%;max-width:420px">' +
       '<div class="in" style="font:600 11px/1 Inter,system-ui,sans-serif;letter-spacing:.2em;text-transform:uppercase;color:' + C.mute + '">Cairo · <span data-k="year"></span></div>' +
       '<h1 class="in d1" style="margin-top:14px;font:700 clamp(46px,14vw,64px)/1 UnifrakturCook,\'Old English Text MT\',serif;letter-spacing:-.01em">Daily Newsletter</h1>' +
       '<div style="margin-top:18px;height:4px;border-top:1px solid ' + C.line + ';border-bottom:1px solid ' + C.line + ';transform-origin:center;animation:sp-rule .6s .15s cubic-bezier(.2,.7,.2,1) both"></div>' +
       '<div class="in d2" style="padding:9px 0;font:600 11px/1.3 Inter,system-ui,sans-serif;letter-spacing:.16em;text-transform:uppercase;color:' + C.ink + '" data-k="date">&nbsp;</div>' +
       '<div style="height:1px;background:' + C.line + ';transform-origin:center;animation:sp-rule .6s .25s cubic-bezier(.2,.7,.2,1) both"></div>' +
       '<p class="late" data-k="summary" style="margin-top:22px;font:italic 700 clamp(19px,5.4vw,23px)/1.3 \'Playfair Display\',Georgia,serif;text-wrap:balance;color:' + C.ink + '"></p>' +
       '</div>',
    // 2. Front page: the paper sheet on the app icon grows into today's front page
    2: '<div style="width:100%;max-width:380px;padding:30px 24px 26px;background:' + C.paper + ';color:#16181a;border-radius:6px;box-shadow:0 30px 80px rgba(0,0,0,.45);' +
       'transform-origin:center;animation:sp-grow .55s cubic-bezier(.2,.8,.2,1) both">' +
       '<div style="font:700 clamp(54px,17vw,72px)/1 UnifrakturCook,\'Old English Text MT\',serif">Daily</div>' +
       '<div style="margin-top:14px;height:5px;border-top:2px solid #16181a;border-bottom:1px solid #16181a"></div>' +
       '<div class="in d2" style="padding:8px 0;font:600 10.5px/1.3 Inter,system-ui,sans-serif;letter-spacing:.16em;text-transform:uppercase" data-k="date">&nbsp;</div>' +
       '<div style="height:7px;background:#16181a"></div>' +
       '<p class="late" data-k="summary" style="margin-top:18px;text-align:left;font:900 clamp(21px,6vw,26px)/1.18 \'Playfair Display\',Georgia,serif;text-wrap:pretty"></p>' +
       '<div class="in d4" style="display:grid;grid-template-columns:1fr 92px;gap:14px;margin-top:20px;text-align:left">' +
       '<div style="display:grid;gap:8px;align-content:start"><i style="height:5px;background:#16181a"></i><i style="height:5px;background:#16181a;width:80%"></i><i style="height:5px;background:#16181a;width:90%"></i><i style="height:5px;background:#16181a;width:60%"></i></div>' +
       '<i style="height:62px;background:#3a3d40"></i></div>' +
       '</div>',
    // 3. Quiet: the icon, the name and the date, nothing else
    3: '<img class="in" src="/icons/newsletter-192.png" alt="" width="88" height="88" style="border-radius:20px;box-shadow:0 10px 30px rgba(0,0,0,' + (dark ? '.5' : '.18') + ')">' +
       '<h1 class="in d1" style="margin-top:22px;font:600 26px/1.15 Newsreader,Georgia,serif;letter-spacing:-.01em">Daily Newsletter</h1>' +
       '<div class="in d2" style="margin-top:8px;font:500 13px/1.4 Inter,system-ui,sans-serif;color:' + C.mute + '" data-k="date">&nbsp;</div>' +
       '<div class="in d3 tick" style="margin-top:26px"></div>'
  };

  // the desk's mark: the chart line draws itself, then takes the day's colour (green up, red down) once the EGX30 is in.
  // On an iPhone the startup image (icons/startup/) already shows the mark drawn, so it is not drawn again there.
  var drawn = navigator.standalone === true && !pv;
  var mark = function (w) {
    return '<svg width="' + w + '" height="' + w + '" viewBox="0 0 192 192" aria-hidden="true" style="display:block">' +
      '<path class="mk-line" d="M40 132L76 96l25 22 52-66" fill="none" stroke="' + C.acc + '" stroke-width="18" stroke-linecap="round" stroke-linejoin="round" pathLength="1" ' +
      'style="transition:stroke .4s ease;stroke-dasharray:1;' + (drawn ? '' : 'stroke-dashoffset:1;animation:sp-draw .7s .05s cubic-bezier(.5,0,.2,1) forwards') + '"/>' +
      '<path class="mk-base" d="M40 156h113" stroke="' + C.ink + '" stroke-width="4" style="transform-origin:96px 156px;' + (drawn ? '' : 'animation:sp-rule .5s cubic-bezier(.2,.7,.2,1) both') + '"/></svg>';
  };
  var lab = 'font:600 11px/1 Inter,system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:' + C.mute;
  var tile = function (k, name) {
    return '<div style="padding:14px 14px 13px;background:' + C.tile + ';border:1px solid ' + C.line + ';border-radius:8px;text-align:left">' +
      '<div style="' + lab + '">' + name + '</div>' +
      '<div class="late" data-k="' + k + '" style="margin-top:8px;font:600 20px/1.1 Inter,system-ui,sans-serif;font-variant-numeric:tabular-nums;letter-spacing:-.01em">&nbsp;</div>' +
      '<div class="late" data-k="' + k + '-chg" style="margin-top:4px;font:600 13px/1 Inter,system-ui,sans-serif;font-variant-numeric:tabular-nums">&nbsp;</div></div>';
  };
  var D = {
    // 1. The number: the mark draws itself, then the EGX30's last close and its day change
    1: '<div style="width:100%;max-width:360px;display:flex;flex-direction:column;align-items:center">' + mark(84) +
       '<div class="in d2" style="margin-top:26px;' + lab + '">EGX30 · last close</div>' +
       '<div class="late" data-k="egx30" style="margin-top:10px;font:600 clamp(44px,13vw,56px)/1 Inter,system-ui,sans-serif;font-variant-numeric:tabular-nums;letter-spacing:-.03em">&nbsp;</div>' +
       '<div class="late" data-k="egx30-chg" style="margin-top:10px;font:600 17px/1 Inter,system-ui,sans-serif;font-variant-numeric:tabular-nums">&nbsp;</div>' +
       '<div class="in d3" style="margin-top:34px;font:500 13px/1.4 Inter,system-ui,sans-serif;color:' + C.mute + '"><b style="color:' + C.ink + ';font-weight:600">Markets Desk</b> · <span data-k="date"></span></div></div>',
    // 2. Board: four numbers that set the morning
    2: '<div style="width:100%;max-width:380px">' +
       '<div style="display:flex;align-items:center;gap:12px">' + mark(40) +
       '<div class="in d1" style="text-align:left"><div style="font:600 17px/1.2 Inter,system-ui,sans-serif">Markets Desk</div><div style="margin-top:2px;font:500 13px/1.3 Inter,system-ui,sans-serif;color:' + C.mute + '" data-k="date"></div></div></div>' +
       '<div class="in d2" style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:24px">' +
       tile('egx30', 'EGX30') + tile('usd_egp', 'Dollar · EGP') + tile('sp500', 'S&amp;P 500') + tile('brent', 'Brent') + '</div>' +
       '<div class="in d3 tick" style="margin:26px auto 0"></div></div>',
    // 3. Headline: the mark and the desk's one-line finding for the day
    3: '<div style="width:100%;max-width:400px;text-align:left">' + mark(56) +
       '<div class="in d1" style="margin-top:26px;' + lab + '"><span style="color:' + C.acc + '">Markets Desk</span> · <span data-k="date"></span></div>' +
       '<p class="late" data-k="summary" style="margin-top:14px;font:600 clamp(23px,6.6vw,28px)/1.25 \'Source Serif 4\',Georgia,serif;letter-spacing:-.01em;text-wrap:pretty"></p>' +
       '<div class="in d3 tick" style="margin-top:28px"></div></div>'
  };

  var el = d.createElement('div');
  el.id = 'splash'; el.setAttribute('aria-hidden', 'true');
  el.innerHTML = '<style>' + css + '</style>' + ((app === 'desk' ? D : N)[look] || (app === 'desk' ? D : N)[1]) +
    (tapOpen ? '<div class="late tap-hint">Tap to open</div>' : '');
  if (d.body) d.body.appendChild(el); else { root.appendChild(el); d.addEventListener('DOMContentLoaded', function () { d.body.appendChild(el); }); }

  // ---- fill in the day's details
  var set = function (k, html, color) {
    el.querySelectorAll('[data-k="' + k + '"]').forEach(function (n) { n.innerHTML = html; if (color) n.style.color = color; n.classList.add('on'); });
  };
  var longDate = function (s) {
    var p = s.split('-'), dt = new Date(Date.UTC(+p[0], +p[1] - 1, +p[2]));
    return dt.toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' }).replace(',', '');
  };
  var newest = function (list) { return list.slice().sort(function (a, b) { return (b.id || b.date) < (a.id || a.date) ? -1 : 1; })[0]; };
  var json = function (u) {
    if (app === 'desk') { var M = window.__deskGet || (window.__deskGet = {}); return M[u] || (M[u] = fetch(u, { cache: 'no-cache' }).then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; })); }
    return fetch(u, { cache: 'no-cache' }).then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; });
  };
  if (app === 'news') {
    json('/editions/index.json').then(function (x) {
      var e = x && x.editions && x.editions.length && newest(x.editions); if (!e) return;
      set('date', longDate(e.date)); set('year', e.date.slice(0, 4)); set('summary', (e.summary || '').replace(/&/g, '&amp;').replace(/</g, '&lt;'));
    });
  } else {
    json('/desk/index.json').then(function (x) {
      var e = x && x.desks && x.desks.length && newest(x.desks); if (!e) return;
      set('date', longDate(e.date)); set('summary', (e.summary || '').replace(/&/g, '&amp;').replace(/</g, '&lt;'));
    });
    if (look !== 3) json('/data/markets-recent.json').then(function (x) {
      var days = x && x.days; if (!days) return;
      var fmt = { egx30: [1, ''], usd_egp: [2, ''], sp500: [2, ''], brent: [2, '$'] };
      Object.keys(fmt).forEach(function (k) {
        var v = [];
        for (var i = days.length - 1; i >= 0 && v.length < 2; i--) if (days[i][k] != null && (!v.length || days[i][k] !== v[0])) v.push(days[i][k]);
        if (!v.length) return;
        set(k, fmt[k][1] + v[0].toLocaleString('en-US', { minimumFractionDigits: fmt[k][0], maximumFractionDigits: fmt[k][0] }));
        if (v.length < 2) return;
        var c = (v[0] / v[1] - 1) * 100, s = Math.abs(c) < 0.005 ? '0.00%' : (c > 0 ? '▲ +' : '▼ −') + Math.abs(c).toFixed(2) + '%';
        set(k + '-chg', s, c > 0 ? C.up : c < 0 ? C.down : C.mute);
        if (k === 'egx30' && Math.abs(c) >= 0.005) el.querySelectorAll('.mk-line').forEach(function (n) { n.setAttribute('stroke', c > 0 ? C.up : C.down); });
      });
    });
  }

  // ---- leave once the page is ready (MIN to MAX after launch); on a phone the newsletter waits for a tap instead
  var gone = false, armed = false;
  var go = function () { if (gone) return; gone = true; el.classList.add('out'); setTimeout(function () { el.remove(); }, 400); };
  var leave = function () {
    if (armed || hold) return; armed = true;
    setTimeout(function () {
      if (!tapOpen) return go();
      el.classList.add('tap');
      var h = el.querySelector('.tap-hint'); if (h) h.classList.add('on');
      el.addEventListener('click', go);
      d.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ' || e.key === 'Escape') go(); });
    }, Math.max(0, MIN - (Date.now() - t0)));
  };
  var sel = me.dataset.ready;
  var check = function () { if (sel && d.querySelector(sel)) { leave(); return true; } };
  d.addEventListener('DOMContentLoaded', function () {
    if (check()) return;
    var mo = new MutationObserver(function () { if (check()) mo.disconnect(); });
    mo.observe(d.body, { childList: true, subtree: true, characterData: true });
  });
  if (!sel) window.addEventListener('load', leave);
  setTimeout(leave, MAX);
})();
