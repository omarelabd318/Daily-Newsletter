// The opening screen shown when the Daily Newsletter or the Markets Desk is launched from the home screen.
// Loaded in <head> of the start page with data-app ("news" or "desk"), data-look (1, 2 or 3) and data-ready (a CSS
// selector that has content once the page is ready):
//   <script src="/splash.js" data-app="news" data-look="2" data-ready="#content > *"></script>
// - Shown only when the app opens from the home screen (standalone), once per launch; links and browser tabs go
//   straight to the page.
// - Leaves as soon as the page is ready, but stays at least MIN ms so it never just flashes, and never more than MAX.
//   Exception: on a phone (the newsletter and the desk alike) it stays up; once the page is ready a "Tap to open"
//   line appears, and a tap anywhere on the screen brings up the page.
// - On a computer (a mouse, and a window 900px or wider) it is shown too: when the start page is opened from a
//   bookmark, the address bar or another site (once per tab; moving between the site's own pages skips it), in a wide
//   layout of its own. It leaves by itself; a click or any key brings up the page sooner.
// - Preview in any browser: ?splash=1|2|3 shows that look; add &hold to keep it up.
(function () {
  var me = document.currentScript, d = document, root = d.documentElement;
  var app = me.dataset.app, q = new URLSearchParams(location.search), pv = q.get('splash');
  var look = +(pv || me.dataset.look || 1), hold = q.has('hold');
  var standalone = (window.matchMedia && matchMedia('(display-mode: standalone)').matches) || navigator.standalone === true;
  var seen = false; try { seen = sessionStorage.getItem('splash-' + app) === '1'; sessionStorage.setItem('splash-' + app, '1'); } catch (e) {}
  var phone = window.matchMedia && matchMedia('(pointer: coarse) and (hover: none)').matches;
  // a computer: a mouse and a wide window (a narrow desktop window keeps the phone-sized layout)
  var wide = !phone && Math.min(window.innerWidth, (screen && screen.width) || 1e4) >= 900;
  var fromSite = false; try { fromSite = !!d.referrer && new URL(d.referrer).origin === location.origin; } catch (e) {}
  if (!pv && (seen || !(standalone || (wide && !fromSite)))) return;
  // a computer's opening screen carries the day's stories, so it stays a little longer (a click or a key skips it)
  var MIN = wide ? 4500 : 2200, MAX = wide ? 6500 : 3500, t0 = Date.now();
  var still = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var tapOpen = phone;

  // colours follow the page's own setting (the newsletter: paper unless dark; the desk: dark unless light)
  var dark = root.getAttribute('data-theme') === 'dark';
  var C = app === 'desk'
    ? (dark ? { bg: '#0e1216', ink: '#eef2f4', mute: '#949ca4', line: '#232b33', acc: '#52d6b5', up: '#5fd08a', down: '#e8605a', tile: '#151b21' }
            : { bg: '#faf8f3', ink: '#16181a', mute: '#5b6168', line: '#e6e1d5', acc: '#1a9e7f', up: '#1d7a3a', down: '#b3261e', tile: '#ffffff' })
    : (dark ? { bg: '#0e1216', ink: '#eef2f4', mute: '#a9b4be', line: '#2a333b', acc: '#52d6b5', paper: '#f4f1ea' }
            : { bg: '#faf8f3', ink: '#16181a', mute: '#5b6168', line: '#16181a', acc: '#8a1c1c', paper: '#faf8f3' });
  if (app === 'news' && look === 2) { C.bg = '#0e1216'; C.mute = '#a9b4be'; } // the sheet on the icon's dark ground, whatever the theme

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
    '#splash .wcol{display:grid;gap:7px;align-content:start}#splash .wcol i{display:block;height:4px;background:#16181a;opacity:.85}' +
    '@media (max-height:820px){#splash [data-w=stories]>:nth-child(n+4){display:none}}' +
    '@media (max-height:720px){#splash [data-w=watch]{display:none}}@media (max-height:600px){#splash [data-w=quote]{display:none}}' +
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

  // wide layouts for a computer screen (the same looks, laid out across the screen)
  // wide layouts for a computer screen: the same looks, with room for the day's actual stories and numbers.
  // Until they arrive (or if they cannot be fetched) the slots keep grey text lines, as on a printed proof.
  var bars = function (ws) { return '<div class="wcol">' + ws.map(function (w) { return '<i style="width:' + w + '%"></i>'; }).join('') + '</div>'; };
  var kick = 'font:700 10.5px/1.2 Inter,system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#5b6168';
  var rule = '1px solid rgba(22,24,26,.3)';
  var NW = {
    // 2. Front page: a broadsheet front page. The nameplate, a dateline (the edition's number, the date, Cairo), the
    // Big Story across two columns with the start of its report set in two justified columns, the number of the day
    // as a black panel and the quote of the day beside it, six more stories in ruled columns, and what to watch today
    // along the foot. Black and white only.
    2: '<div style="width:100%;max-width:1040px;max-height:calc(100vh - 96px);overflow:hidden;padding:clamp(24px,4vh,36px) 44px clamp(20px,3.4vh,30px);background:' + C.paper + ';color:#16181a;border-radius:6px;box-shadow:0 40px 120px rgba(0,0,0,.5);' +
       'transform-origin:center;animation:sp-grow .6s cubic-bezier(.2,.8,.2,1) both;text-align:left">' +
       '<div style="text-align:center;font:700 min(8vw,10vh,96px)/1 UnifrakturCook,\'Old English Text MT\',serif">Daily Newsletter</div>' +
       '<div style="margin-top:clamp(10px,1.8vh,16px);height:6px;border-top:2px solid #16181a;border-bottom:1px solid #16181a"></div>' +
       '<div class="in d2" style="display:grid;grid-template-columns:1fr auto 1fr;gap:20px;align-items:center;padding:9px 0;font:600 11px/1.3 Inter,system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase;white-space:nowrap">' +
       '<span data-k="no">No.</span><span data-k="date" style="text-align:center">&nbsp;</span><span style="text-align:right">Cairo</span></div>' +
       '<div style="height:8px;background:#16181a"></div>' +
       // the lead and the right-hand column
       '<div style="display:grid;grid-template-columns:2fr 1fr;margin-top:clamp(14px,2.4vh,22px)">' +
       '<div style="padding-right:26px;border-right:' + rule + ';display:flex;flex-direction:column"><div class="in d2" style="' + kick + '" data-w="lead-kick">The Big Story</div>' +
       '<p class="late" data-w="lead" style="min-height:2.24em;margin-top:7px;font:900 clamp(26px,min(3vw,4.4vh),38px)/1.12 \'Playfair Display\',Georgia,serif;text-wrap:pretty"></p>' +
       '<div class="in d3" data-w="body" style="margin-top:12px;flex:1 1 0;min-height:min(105px,12vh);overflow:hidden;columns:2;column-fill:auto;column-gap:26px;column-rule:' + rule + '">' + bars([100, 96, 100, 88, 100, 94, 100, 70]) + '</div></div>' +
       '<div class="in d3" style="padding-left:26px;display:flex;flex-direction:column;gap:14px">' +
       '<div data-w="number" style="padding:16px 18px;background:#16181a;color:' + C.paper + '"><div style="' + kick + ';color:#c9c6bd">Number of the day</div><div style="margin-top:10px;height:30px"></div></div>' +
       '<div data-w="quote">' + bars([100, 84, 92, 50]) + '</div></div></div>' +
       // six more stories in ruled columns
       '<div class="in d4" data-w="stories" style="display:grid;grid-template-columns:repeat(3,1fr);margin-top:clamp(14px,2.4vh,22px);border-top:2px solid #16181a">' +
       [0, 1, 2, 3, 4, 5].map(function (i) { return '<div>' + bars([40, 100, 80 - i * 5]) + '</div>'; }).join('') + '</div>' +
       // what to watch today
       '<div class="in d4" data-w="watch" style="margin-top:14px;padding-top:10px;border-top:1px solid #16181a;font:500 12.5px/1.4 Inter,system-ui,sans-serif;white-space:nowrap;overflow:hidden;text-overflow:ellipsis"></div>' +
       '</div>'
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
  // the morning board under the EGX30 (look 1): a smaller tile, value and day change on one line
  var mini = function (k, name) {
    return '<div style="padding:10px 12px;background:' + C.tile + ';border:1px solid ' + C.line + ';border-radius:8px;text-align:left">' +
      '<div style="font:600 10px/1 Inter,system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:' + C.mute + '">' + name + '</div>' +
      '<div class="late" data-k="' + k + '" style="margin-top:7px;font:600 16px/1.1 Inter,system-ui,sans-serif;font-variant-numeric:tabular-nums;letter-spacing:-.01em">&nbsp;</div>' +
      '<div class="late" data-k="' + k + '-chg" style="margin-top:3px;font:600 11.5px/1 Inter,system-ui,sans-serif;font-variant-numeric:tabular-nums">&nbsp;</div></div>';
  };
  var DW = {
    // 1. The number: the EGX30 on the left, the board of six on the right
    1: '<div style="width:100%;max-width:1000px;display:grid;grid-template-columns:1fr 1px 1.4fr;gap:clamp(28px,3.6vw,52px);align-items:center;text-align:left">' +
       '<div>' + mark(92) +
       '<div class="in d2" style="margin-top:30px;' + lab + '">EGX30 · last close</div>' +
       '<div class="late" data-k="egx30" style="margin-top:12px;font:600 clamp(56px,6.4vw,80px)/1 Inter,system-ui,sans-serif;font-variant-numeric:tabular-nums;letter-spacing:-.03em">&nbsp;</div>' +
       '<div class="late" data-k="egx30-chg" style="margin-top:12px;font:600 20px/1 Inter,system-ui,sans-serif;font-variant-numeric:tabular-nums">&nbsp;</div>' +
       '<div class="in d3" style="margin-top:34px;font:500 14px/1.4 Inter,system-ui,sans-serif;color:' + C.mute + '"><b style="color:' + C.ink + ';font-weight:600">Markets Desk</b> · <span data-k="date"></span></div></div>' +
       '<i class="in d2" style="align-self:stretch;background:' + C.line + '"></i>' +
       '<div><div class="in d3" style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px">' +
       tile('egx70', 'EGX70') + tile('usd_egp', 'Dollar · market') + tile('gold24_egp', 'Gold 24k · EGP') +
       tile('brent', 'Brent') + tile('sp500', 'S&amp;P 500') + tile('btc', 'Bitcoin') + '</div>' +
       '<div class="in d4" style="margin-top:26px;' + lab + ';color:' + C.acc + '">The desk\'s finding</div>' +
       '<p class="late" data-k="finding" style="margin-top:10px;font:400 18px/1.45 \'Source Serif 4\',Georgia,serif;text-wrap:pretty;display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:5;overflow:hidden;min-height:2.9em">&nbsp;</p>' +
       '<p class="late" data-k="next" style="margin-top:14px;padding-top:12px;border-top:1px solid ' + C.line + ';font:500 13.5px/1.45 Inter,system-ui,sans-serif;color:' + C.mute + '">&nbsp;</p></div></div>'
  };
  var D = {
    // 1. The number: the mark draws itself, then the EGX30's last close and its day change, and a board of six more
    1: '<div style="width:100%;max-width:360px;display:flex;flex-direction:column;align-items:center">' + mark(84) +
       '<div class="in d2" style="margin-top:26px;' + lab + '">EGX30 · last close</div>' +
       '<div class="late" data-k="egx30" style="margin-top:10px;font:600 clamp(44px,13vw,56px)/1 Inter,system-ui,sans-serif;font-variant-numeric:tabular-nums;letter-spacing:-.03em">&nbsp;</div>' +
       '<div class="late" data-k="egx30-chg" style="margin-top:10px;font:600 17px/1 Inter,system-ui,sans-serif;font-variant-numeric:tabular-nums">&nbsp;</div>' +
       '<div class="in d3" style="display:grid;grid-template-columns:1fr 1fr;gap:8px;width:100%;margin-top:26px">' +
       mini('egx70', 'EGX70') + mini('usd_egp', 'Dollar · market') + mini('gold24_egp', 'Gold 24k · EGP') +
       mini('brent', 'Brent') + mini('sp500', 'S&amp;P 500') + mini('btc', 'Bitcoin') + '</div>' +
       '<div class="in d3" style="margin-top:26px;font:500 13px/1.4 Inter,system-ui,sans-serif;color:' + C.mute + '"><b style="color:' + C.ink + ';font-weight:600">Markets Desk</b> · <span data-k="date"></span></div></div>',
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
  var looks = app === 'desk' ? D : N, wideLook = wide && (app === 'desk' ? DW : NW)[look];
  el.innerHTML = '<style>' + css + '</style>' + (wideLook || looks[look] || looks[1]) +
    (tapOpen ? '<div class="late tap-hint">Tap to open</div>' : wide ? '<div class="late tap-hint" style="margin-top:18px">Click or press any key to open</div>' : '');
  if (d.body) d.body.appendChild(el); else { root.appendChild(el); d.addEventListener('DOMContentLoaded', function () { d.body.appendChild(el); }); }

  // ---- fill in the day's details
  var set = function (k, html, color) {
    el.querySelectorAll('[data-k="' + k + '"]').forEach(function (n) { n.innerHTML = html; if (color) n.style.color = color; n.classList.add('on'); });
  };
  var longDate = function (s) {
    var p = s.split('-'), dt = new Date(Date.UTC(+p[0], +p[1] - 1, +p[2]));
    return dt.toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' }).replace(',', '');
  };
  var esc = function (t) { return String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); };
  // markdown inline to plain text: links keep their words, emphasis marks go
  var plain = function (t) { return t.replace(/\[([^\]]+)\]\([^)]*\)/g, '$1').replace(/\*\*|__|\*/g, '').replace(/\s+/g, ' ').trim(); };
  var clamp = function (n) { return 'display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:' + n + ';overflow:hidden'; };
  var put = function (k, html) { var n = el.querySelector('[data-w="' + k + '"]'); if (!n) return; n.innerHTML = html; n.classList.add('late'); requestAnimationFrame(function () { n.classList.add('on'); }); };
  // the wide front page: fill it from the day's edition
  var slug = function (t) { return t.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, ''); };
  // the wide front page: fill it from the day's edition
  var front = function (md, e) {
    var g = [], watch = '', hits = {}, para = {};
    md.split('\n').forEach(function (l) {
      var m;
      if ((m = l.match(/^\d+\.\s+\*\*(.+?):\*\*\s*(.+)$/))) { var a = m[2].match(/\(#story-([^)]+)\)/); g.push({ k: plain(m[1]), t: plain(m[2]), a: a ? a[1] : '' }); }
      else if ((m = l.match(/^\*\*What to watch today:\*\*\s*(.+)$/))) watch = plain(m[1]);
      else if ((m = l.match(/^- \*\*(.+?):\*\*\s*(.+)$/))) hits[m[1].toLowerCase()] = plain(m[2]);
      else if ((m = l.match(/^\*\*(.+?):\*\*\s*(.+)$/))) { var k = slug(plain(m[1])); if (!para[k]) para[k] = plain(m[2]); }
    });
    if (!g.length) { put('lead', esc(e.summary || '')); return; }
    var lead = g[0];
    put('lead-kick', esc(lead.k)); put('lead', esc(lead.t));
    var body = para[lead.a];
    if (body) {
      put('body', '<p style="font:400 14.5px/21px Newsreader,Georgia,serif;text-align:justify;hyphens:auto">' + esc(body.replace(/\s*Why it matters:.*$/, '')) + '</p>');
      // end each column on a whole line: the box takes the space the right-hand column leaves, rounded down to lines
      var bx = el.querySelector('[data-w="body"]'), col = bx.parentNode, row = col.parentNode;
      var fit = function () {
        bx.style.height = '21px';
        var room = row.getBoundingClientRect().bottom - bx.getBoundingClientRect().top;
        bx.style.height = Math.max(21 * 3, Math.floor(room / 21) * 21) + 'px';
      };
      bx.style.flex = 'none'; fit();
      if (window.ResizeObserver) new ResizeObserver(fit).observe(row.lastChild);
      if (d.fonts && d.fonts.ready) d.fonts.ready.then(fit);
    }
    var num = hits['number of the day'];
    if (num) {
      var cut = num.search(/\.\s/), fig = cut > 0 && cut < 24 ? num.slice(0, cut) : '', rest = fig ? num.slice(cut + 1).trim() : num;
      put('number', '<div style="' + kick + ';color:#c9c6bd">Number of the day</div>' + (fig ? '<div style="margin-top:8px;font:900 32px/1.05 \'Playfair Display\',Georgia,serif">' + esc(fig) + '</div>' : '') +
        '<p style="margin-top:8px;font:400 14px/1.4 Newsreader,Georgia,serif;color:#e6e2d8;' + clamp(4) + '">' + esc(rest) + '</p>');
    }
    var qt = hits['quote of the day'];
    if (qt) {
      var qm = qt.match(/^["“](.+?)["”]\s*(.*)$/);
      put('quote', '<div style="' + kick + '">Quote of the day</div><p style="margin-top:7px;font:italic 700 16px/1.3 \'Playfair Display\',Georgia,serif;' + clamp(4) + '">“' + esc(qm ? qm[1] : qt) + '”</p>' +
        (qm && qm[2] ? '<div style="margin-top:6px;font:500 12px/1.35 Inter,system-ui,sans-serif;color:#5b6168;' + clamp(2) + '">' + esc(qm[2]) + '</div>' : ''));
    }
    var more = g.slice(1, 7);
    if (more.length) put('stories', more.map(function (s, i) {
      return '<div style="padding:12px ' + (i % 3 === 2 ? '0' : '20px') + ' 12px ' + (i % 3 === 0 ? '0' : '20px') + ';' + (i % 3 ? 'border-left:' + rule + ';' : '') + (i >= 3 ? 'border-top:' + rule + ';' : '') + '">' +
        '<div style="' + kick + '">' + esc(s.k) + '</div><div style="margin-top:5px;font:700 16px/1.25 \'Playfair Display\',Georgia,serif;text-wrap:pretty;' + clamp(2) + '">' + esc(s.t) + '</div></div>';
    }).join(''));
    if (watch) put('watch', '<b style="font:700 10.5px/1 Inter,system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase;margin-right:10px">What to watch today</b>' +
      watch.split(/;\s*/).filter(Boolean).map(function (x) { return esc(x.replace(/\.$/, '')); }).join('<span style="margin:0 9px;color:#8a8e93">·</span>'));
  };
  var newest = function (list) { return list.slice().sort(function (a, b) { return (b.id || b.date) < (a.id || a.date) ? -1 : 1; })[0]; };
  var json = function (u) {
    if (app === 'desk') { var M = window.__deskGet || (window.__deskGet = {}); return M[u] || (M[u] = fetch(u, { cache: 'no-cache' }).then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; })); }
    return fetch(u, { cache: 'no-cache' }).then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; });
  };
  if (app === 'news') {
    json('/editions/index.json').then(function (x) {
      var e = x && x.editions && x.editions.length && newest(x.editions); if (!e) return;
      set('date', longDate(e.date)); set('year', e.date.slice(0, 4)); set('summary', esc(e.summary || ''));
      // the edition's number, counted as the paper's own dateline counts it
      set('no', 'No. ' + x.editions.filter(function (y) { return !y.id && y.date <= e.date; }).length);
      if (wideLook) fetch('/editions/' + e.date + '.md', { cache: 'no-cache' }).then(function (r) { return r.ok ? r.text() : ''; }).catch(function () { return ''; })
        .then(function (md) { front(md, e); });
    });
  } else {
    json('/desk/index.json').then(function (x) {
      var e = x && x.desks && x.desks.length && newest(x.desks); if (!e) return;
      set('date', longDate(e.date)); set('summary', esc(e.summary || ''));
      // the wide board also carries the desk's finding for Egypt and what comes next
      if (wideLook) json('/desk/days/' + e.date + '.json').then(function (y) {
        var g = y && y.egypt; if (!g) return;
        if (g.finding) set('finding', esc(g.finding));
        if (g.next) set('next', '<b style="color:' + C.ink + ';font-weight:600">Next</b> · ' + esc(g.next));
      });
    });
    if (look !== 3) json('/data/markets-recent.json').then(function (x) {
      var days = x && x.days; if (!days) return;
      var fmt = { egx30: [1, ''], egx70: [1, ''], usd_egp: [2, ''], gold24_egp: [0, ''], sp500: [2, ''], brent: [2, '$'], btc: [0, '$'] };
      Object.keys(fmt).forEach(function (k) {
        var v = [];
        for (var i = days.length - 1; i >= 0 && v.length < 2; i--) if (days[i][k] != null && (!v.length || days[i][k] !== v[0])) v.push(days[i][k]);
        if (!v.length) return;
        set(k, fmt[k][1] + v[0].toLocaleString('en-US', { minimumFractionDigits: fmt[k][0], maximumFractionDigits: fmt[k][0] }));
        if (v.length < 2) return;
        var c = (v[0] / v[1] - 1) * 100, s = Math.abs(c) < 0.005 ? '0.00%' : (c > 0 ? '▲ +' : '▼ −') + Math.abs(c).toFixed(2) + '%';
        var g = k === 'usd_egp' ? -c : c; // the dollar in pounds: up is the pound weaker, so red
        set(k + '-chg', s, g > 0 ? C.up : g < 0 ? C.down : C.mute);
        if (k === 'egx30' && Math.abs(c) >= 0.005) el.querySelectorAll('.mk-line').forEach(function (n) { n.setAttribute('stroke', c > 0 ? C.up : C.down); });
      });
    });
  }

  // ---- leave once the page is ready (MIN to MAX after launch); on a phone it waits for a tap instead
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
  if (!tapOpen && !hold) {
    if (wide) setTimeout(function () { var h = el.querySelector('.tap-hint'); if (h) h.classList.add('on'); }, 900);
    el.addEventListener('click', go);
    d.addEventListener('keydown', function k() { d.removeEventListener('keydown', k); go(); });
  }
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
