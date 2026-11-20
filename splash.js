// The opening screen shown when the Daily Newsletter or the Markets Desk is launched from the home screen.
// Loaded in <head> of the start page with data-app ("news" or "desk"), data-look (1, 2 or 3) and data-ready (a CSS
// selector that has content once the page is ready):
//   <script src="/splash.js" data-app="news" data-look="2" data-ready="#content > *"></script>
// - Shown only when the app opens from the home screen (standalone), once per launch; links and browser tabs go
//   straight to the page.
// - Leaves as soon as the page is ready, but stays at least MIN ms so it never just flashes, and never more than MAX.
//   Exception: on a phone (the newsletter and the desk alike) it stays up; once the page is ready a "Tap to open"
//   line appears, and a tap anywhere on the screen brings up the page. The newsletter's phone front page (look 2) writes
//   its headline out letter by letter from the start.
// - On a computer (a mouse, and a window 900px or wider) it is shown too: when the start page is opened from a
//   bookmark, the address bar or another site (once per tab; moving between the site's own pages skips it), in a wide
//   layout of its own, and it waits for a click ("Click to open").
// - A refresh brings it up again. The "Tap / Click to open" line sits at the very bottom and does not pulse.
// - Preview in any browser: ?splash=1|2|3 shows that look; add &hold to keep it up.
// - The computer's front page can write itself out too: it starts with only the nameplate and the dateline, then
//   each block is typed in turn, and the dividers all come up together once the page is written.
//   data-wide-type="1" on the <script> tag turns it on; ?typewide previews it.
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
  // a refresh brings it up again
  var reload = false; try { var nv = performance.getEntriesByType('navigation')[0]; reload = nv ? nv.type === 'reload' : performance.navigation.type === 1; } catch (e) {}
  if (!pv && ((seen && !reload) || !(standalone || (wide && (reload || !fromSite))))) return;
  var MIN = 2200, MAX = 3500, t0 = Date.now();
  var still = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var tapOpen = phone || wide; // on a phone and on a computer it waits to be opened

  // colours follow the page's own setting (the newsletter: paper unless dark; the desk: dark unless light)
  var dark = root.getAttribute('data-theme') === 'dark';
  var C = app === 'desk'
    ? (dark ? { bg: '#0e1216', ink: '#eef2f4', mute: '#949ca4', line: '#232b33', acc: '#52d6b5', up: '#5fd08a', down: '#e8605a', tile: '#151b21' }
            : { bg: '#faf8f3', ink: '#16181a', mute: '#5b6168', line: '#e6e1d5', acc: '#1a9e7f', up: '#1d7a3a', down: '#b3261e', tile: '#ffffff' })
    : (dark ? { bg: '#0e1216', ink: '#eef2f4', mute: '#a9b4be', line: '#2a333b', acc: '#52d6b5', paper: '#f4f1ea' }
            : { bg: '#faf8f3', ink: '#16181a', mute: '#5b6168', line: '#16181a', acc: '#8a1c1c', paper: '#faf8f3' });
  // the newsletter's front page (look 2, on a phone and on a computer) takes the newsletter's own colours: paper (the
  // default), light or dark, the sheet on its ground as on the app icon
  var th = root.getAttribute('data-theme');
  var P = th === 'dark' ? { bg: '#080b0e', sheet: '#0e1216', ink: '#eef2f4', ink2: '#a9b4be', rule: 'rgba(238,242,244,.22)', body: 'Newsreader', dots: 'rgba(255,255,255,.03)', shadow: '.6' }
        : th === 'paper' ? { bg: '#cfc9ba', sheet: '#e8e3d6', ink: '#14110d', ink2: '#4f4a40', rule: 'rgba(20,17,13,.28)', body: '\'Old Standard TT\'', dots: 'rgba(60,50,30,.05)', shadow: '.22' }
        : { bg: '#f0ebe0', sheet: '#faf8f3', ink: '#16181a', ink2: '#5b6168', rule: 'rgba(22,24,26,.28)', body: 'Newsreader', dots: 'rgba(60,50,30,.03)', shadow: '.18' };
  if (app === 'news' && (wide ? +(pv || me.dataset.wideLook || look) : look) === 2) { C.bg = P.bg; C.mute = P.ink2; }

  var css = '#splash{position:fixed;inset:0;z-index:2147483000;display:flex;flex-direction:column;align-items:center;justify-content:center;' +
    'padding:max(24px,env(safe-area-inset-top)) 28px max(24px,env(safe-area-inset-bottom));background:' + C.bg + ';color:' + C.ink + ';' +
    'text-align:center;-webkit-font-smoothing:antialiased;transition:opacity .32s cubic-bezier(.2,.7,.2,1),transform .32s cubic-bezier(.2,.7,.2,1)}' +
    '#splash.out{opacity:0;transform:scale(1.02);pointer-events:none}' +
    '#splash *{box-sizing:border-box;margin:0}' +
    '#splash .in{opacity:0;transform:translateY(6px);animation:sp-in .5s cubic-bezier(.2,.7,.2,1) forwards}' +
    '#splash .d1{animation-delay:.08s}#splash .d2{animation-delay:.18s}#splash .d3{animation-delay:.3s}#splash .d4{animation-delay:.42s}' +
    '#splash .late{opacity:0;transition:opacity .35s ease}#splash .late.on{opacity:1}' +
    '#splash.tap{cursor:pointer;-webkit-tap-highlight-color:transparent}' +
    '#splash .tap-hint{position:absolute;left:0;right:0;bottom:max(18px,calc(env(safe-area-inset-bottom) + 8px));font:600 11px/1 Inter,system-ui,sans-serif;letter-spacing:.2em;text-transform:uppercase;color:' + C.mute + '}' +
    '#splash .wcol{display:grid;gap:7px;align-content:start}#splash .wcol i{display:block;height:4px;background:' + P.ink + ';opacity:.85}' +
    '@media (max-height:820px){#splash [data-w=stories]>:nth-child(n+4){display:none}}' +
    
    '@keyframes sp-in{to{opacity:1;transform:none}}' +
    '@keyframes sp-rule{from{transform:scaleX(0)}to{transform:scaleX(1)}}' +
    '@keyframes sp-draw{to{stroke-dashoffset:0}}' +
    '@keyframes sp-grow{from{transform:scale(.42);border-radius:22px}to{transform:none}}' +
    '@keyframes sp-tick{from{transform:translateX(-100%)}to{transform:translateX(250%)}}' +
    '#splash .tick{position:relative;overflow:hidden;width:56px;height:2px;background:' + C.line + '}' +
    '#splash .tick::after{content:"";position:absolute;inset:0;width:40%;background:' + C.acc + ';animation:sp-tick 1.1s ease-in-out infinite}' +
    '#splash .mk-line.down{transform:scaleX(-1)}' +
    (still ? '#splash *,#splash *::after{animation:none!important;opacity:1!important;transform:none!important;stroke-dashoffset:0!important}#splash .mk-line.down{transform:scaleX(-1)!important}' : '');

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
    2: '<div style="width:100%;max-width:380px;padding:30px 24px 26px;background:' + P.sheet + ';background-image:radial-gradient(' + P.dots + ' 1px,transparent 1px);background-size:3px 3px;color:' + P.ink + ';border-radius:4px;box-shadow:0 24px 70px rgba(0,0,0,' + P.shadow + ');' +
       'transform-origin:center;animation:sp-grow .55s cubic-bezier(.2,.8,.2,1) both">' +
       '<div style="font:700 clamp(54px,17vw,72px)/1 UnifrakturCook,\'Old English Text MT\',serif">Daily</div>' +
       '<div style="margin-top:14px;height:5px;border-top:2px solid ' + P.ink + ';border-bottom:1px solid ' + P.ink + '"></div>' +
       '<div class="in d2" style="padding:8px 0;font:600 10.5px/1.3 Inter,system-ui,sans-serif;letter-spacing:.16em;text-transform:uppercase" data-k="date">&nbsp;</div>' +
       '<div style="height:7px;background:' + P.ink + '"></div>' +
       '<p class="late" data-k="summary" style="margin-top:18px;text-align:left;font:900 clamp(21px,6vw,26px)/1.18 \'Playfair Display\',Georgia,serif;text-wrap:pretty"></p>' +
       '<div class="in d4" style="display:grid;grid-template-columns:1fr 92px;gap:14px;margin-top:20px;text-align:left">' +
       '<div style="display:grid;gap:8px;align-content:start"><i style="height:5px;background:' + P.ink + '"></i><i style="height:5px;background:' + P.ink + ';width:80%"></i><i style="height:5px;background:' + P.ink + ';width:90%"></i><i style="height:5px;background:' + P.ink + ';width:60%"></i></div>' +
       '<i style="height:62px;background:' + P.ink + ';opacity:.8"></i></div>' +
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
  var kick = 'font:700 10.5px/1.2 Inter,system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:' + P.ink2;
  var rule = '1px solid ' + P.rule;
  var NW = {
    // 2. Front page: a broadsheet front page. The nameplate, a dateline (the edition's number, the date, Cairo), the
    // Big Story across two columns with the start of its report set in two justified columns, the number of the day
    // as a black panel and the quote of the day beside it, six more stories in ruled columns, and what to watch today
    // along the foot. In the newsletter's own colours.
    2: '<div style="width:100%;max-width:1040px;max-height:calc(100vh - 110px);overflow:hidden;padding:clamp(24px,4vh,36px) 44px clamp(20px,3.4vh,30px);background:' + P.sheet + ';background-image:radial-gradient(' + P.dots + ' 1px,transparent 1px);background-size:3px 3px;color:' + P.ink + ';border-radius:4px;box-shadow:0 30px 90px rgba(0,0,0,' + P.shadow + ');' +
       'transform-origin:center;animation:sp-grow .6s cubic-bezier(.2,.8,.2,1) both;text-align:left">' +
       '<div style="text-align:center;font:700 min(8vw,10vh,96px)/1 UnifrakturCook,\'Old English Text MT\',serif">Daily Newsletter</div>' +
       '<div style="margin-top:clamp(10px,1.8vh,16px);height:6px;border-top:2px solid ' + P.ink + ';border-bottom:1px solid ' + P.ink + '"></div>' +
       '<div class="in d2" style="display:grid;grid-template-columns:1fr auto 1fr;gap:20px;align-items:center;padding:9px 0;font:600 11px/1.3 Inter,system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase;white-space:nowrap">' +
       '<span data-k="no">No.</span><span data-k="date" style="text-align:center">&nbsp;</span><span style="text-align:right">Cairo</span></div>' +
       '<div style="height:8px;background:' + P.ink + '"></div>' +
       // the lead and the right-hand column
       '<div style="display:grid;grid-template-columns:2fr 1fr;margin-top:clamp(14px,2.4vh,22px)">' +
       '<div data-r="lead" style="padding-right:26px;border-right:' + rule + ';display:flex;flex-direction:column"><div class="in d2" style="' + kick + '" data-w="lead-kick">The Big Story</div>' +
       '<p class="late" data-w="lead" style="min-height:2.24em;margin-top:7px;font:900 clamp(26px,min(3vw,4.4vh),38px)/1.12 \'Playfair Display\',Georgia,serif;text-wrap:pretty"></p>' +
       '<div class="in d3" data-w="body" style="margin-top:12px;flex:1 1 0;min-height:min(105px,12vh);overflow:hidden;columns:2;column-fill:balance;column-gap:26px;column-rule:' + rule + '">' + bars([100, 96, 100, 88, 100, 94, 100, 70]) + '</div></div>' +
       '<div class="in d3" style="padding-left:26px;display:flex;flex-direction:column;gap:14px">' +
       '<div data-w="number" style="padding:16px 18px;background:' + P.ink + ';color:' + P.sheet + '"><div style="' + kick + ';color:' + P.sheet + ';opacity:.7">Number of the day</div><div style="margin-top:10px;height:30px"></div></div>' +
       '<div data-w="quote">' + bars([100, 84, 92, 50]) + '</div></div></div>' +
       // six more stories in ruled columns
       '<div class="in d4" data-w="stories" style="display:grid;grid-template-columns:repeat(3,1fr);margin-top:clamp(14px,2.4vh,22px);border-top:2px solid ' + P.ink + '">' +
       [0, 1, 2, 3, 4, 5].map(function (i) { return '<div>' + bars([40, 100, 80 - i * 5]) + '</div>'; }).join('') + '</div>' +
       // what to watch today
       '<div class="in d4" data-w="watch" style="margin-top:14px;padding-top:10px;border-top:1px solid ' + P.ink + '"></div>' +
       '</div>'
  };

  // the desk's mark: the chart line draws itself, then takes the day's colour once the EGX30 is in: green and rising on
  // an up day, red and turned to fall (mirrored) on a down day.
  // On an iPhone the startup image (icons/startup/) already shows the mark drawn, so it is not drawn again there.
  var drawn = navigator.standalone === true && !pv;
  var mark = function (w) {
    return '<svg width="' + w + '" height="' + w + '" viewBox="0 0 192 192" aria-hidden="true" style="display:block">' +
      '<path class="mk-line" d="M40 132L76 96l25 22 52-66" fill="none" stroke="' + C.acc + '" stroke-width="18" stroke-linecap="round" stroke-linejoin="round" pathLength="1" ' +
      'style="transition:stroke .4s ease,transform .5s cubic-bezier(.2,.7,.2,1);transform-box:view-box;transform-origin:96.5px 96px;stroke-dasharray:1;' + (drawn ? '' : 'stroke-dashoffset:1;animation:sp-draw .7s .05s cubic-bezier(.5,0,.2,1) forwards') + '"/>' +
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
  // sparklines: filled in from the market history once it arrives (k: the series, n: how many sessions)
  var spark = function (k, n, h, area) {
    return '<svg data-sp="' + k + '" data-n="' + n + '"' + (area ? ' data-area="1"' : '') + ' viewBox="0 0 100 ' + h + '" preserveAspectRatio="none" aria-hidden="true" style="display:block;width:100%;height:' + h + 'px;overflow:visible"></svg>';
  };
  var num = function (k, size) { return '<div class="late" data-k="' + k + '" style="font:600 ' + size + '/1 Inter,system-ui,sans-serif;font-variant-numeric:tabular-nums;letter-spacing:-.03em">&nbsp;</div>'; };
  var chg = function (k, size) { return '<span class="late" data-k="' + k + '-chg" style="white-space:nowrap;font:600 ' + size + '/1 Inter,system-ui,sans-serif;font-variant-numeric:tabular-nums">&nbsp;</span>'; };
  var head = function (w) {
    return '<div style="display:flex;align-items:center;gap:12px">' + mark(w) +
      '<div class="in d1" style="text-align:left"><div style="font:600 16px/1.2 Inter,system-ui,sans-serif">Markets Desk</div><div style="margin-top:2px;font:500 13px/1.3 Inter,system-ui,sans-serif;color:' + C.mute + '" data-k="date"></div></div></div>';
  };
  // a tile with its own three-month line
  var stile = function (k, name) {
    return '<div style="padding:13px 14px 12px;background:' + C.tile + ';border:1px solid ' + C.line + ';border-radius:8px;text-align:left">' +
      '<div style="' + lab + '">' + name + '</div>' +
      '<div style="display:flex;align-items:baseline;justify-content:space-between;gap:8px;margin-top:8px">' + num(k, '19px') + chg(k, '12.5px') + '</div>' +
      '<div style="margin-top:10px">' + spark(k, 91, 30) + '</div></div>';
  };
  var finding = function (size, lines) {
    return '<p class="late" data-k="finding" style="font:400 ' + size + '/1.45 \'Source Serif 4\',Georgia,serif;text-wrap:pretty;display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:' + lines + ';overflow:hidden">&nbsp;</p>';
  };
  var next = '<p class="late" data-k="next" style="margin-top:14px;padding-top:12px;border-top:1px solid ' + C.line + ';font:500 13.5px/1.45 Inter,system-ui,sans-serif;color:' + C.mute + '">&nbsp;</p>';
  var DW = {
    // 1. Board: the EGX30 with its three months as an area chart on the left; six tiles with their own lines on the
    // right, and the desk's finding under them
    1: '<div style="width:100%;max-width:1120px;display:grid;grid-template-columns:1fr 1.35fr;gap:clamp(32px,4vw,56px);text-align:left">' +
       '<div style="display:flex;flex-direction:column">' + head(40) +
       '<div class="in d2" style="margin-top:34px;' + lab + '">EGX30 · last close</div>' +
       '<div style="margin-top:12px">' + num('egx30', 'clamp(52px,5.6vw,76px)') + '</div>' +
       '<div style="margin-top:12px;display:flex;gap:14px;align-items:baseline">' + chg('egx30', '19px') + '<span class="late" data-k="egx30-3m" style="font:500 13px/1 Inter,system-ui,sans-serif;color:' + C.mute + '">&nbsp;</span></div>' +
       '<div class="in d3" style="margin-top:auto;padding-top:26px">' + spark('egx30', 91, 150, true) + '</div></div>' +
       '<div><div class="in d3" style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px">' +
       stile('egx70', 'EGX70') + stile('usd_egp', 'Dollar · market') + stile('gold24_egp', 'Gold 24k · EGP') +
       stile('brent', 'Brent') + stile('sp500', 'S&amp;P 500') + stile('btc', 'Bitcoin') + '</div>' +
       '<div class="in d4" style="margin-top:24px;' + lab + ';color:' + C.acc + '">The desk\'s finding</div>' +
       '<div style="margin-top:10px">' + finding('17.5px', 4) + '</div>' + next + '</div></div>',
    // 2. Chart: the EGX30's six months across the screen with the last close over it, six tiles in a row beneath
    2: '<div style="width:100%;max-width:1160px;text-align:left">' +
       '<div style="display:flex;justify-content:space-between;align-items:center">' + head(40) +
       '<div class="in d2" style="' + lab + '">EGX30 · six months</div></div>' +
       '<div style="position:relative;margin-top:26px;padding-top:0">' +
       '<div style="position:absolute;top:0;left:0;z-index:1">' + num('egx30', 'clamp(56px,6vw,84px)') +
       '<div style="margin-top:12px;display:flex;gap:14px;align-items:baseline">' + chg('egx30', '19px') + '<span class="late" data-k="egx30-6m" style="font:500 13px/1 Inter,system-ui,sans-serif;color:' + C.mute + '">&nbsp;</span></div></div>' +
       '<div class="in d2" style="padding-top:70px">' + spark('egx30', 182, 250, true) + '</div></div>' +
       '<div class="in d3" style="display:grid;grid-template-columns:repeat(6,1fr);gap:10px;margin-top:26px">' +
       stile('egx70', 'EGX70') + stile('usd_egp', 'Dollar') + stile('gold24_egp', 'Gold 24k') +
       stile('brent', 'Brent') + stile('sp500', 'S&amp;P 500') + stile('btc', 'Bitcoin') + '</div>' +
       '<div class="in d4" style="margin-top:22px;max-width:900px">' + finding('16.5px', 2) + '</div></div>',
    // 3. Briefing: the desk's finding as the headline on the left; a quote board of seven on the right, each with its
    // three months, its last value and the day's change
    3: '<div style="width:100%;max-width:1120px;display:grid;grid-template-columns:1fr 1fr;gap:clamp(36px,5vw,72px);align-items:center;text-align:left">' +
       '<div>' + head(44) +
       '<div class="in d2" style="margin-top:34px;' + lab + ';color:' + C.acc + '">The desk\'s finding</div>' +
       '<div style="margin-top:12px">' + finding('clamp(21px,2vw,26px)', 7) + '</div>' + next + '</div>' +
       '<div class="in d3" style="border-top:1px solid ' + C.line + '">' +
       [['egx30', 'EGX30', 1], ['egx70', 'EGX70'], ['usd_egp', 'Dollar · market'], ['gold24_egp', 'Gold 24k · EGP'], ['brent', 'Brent'], ['sp500', 'S&amp;P 500'], ['btc', 'Bitcoin']].map(function (r) {
         return '<div style="display:grid;grid-template-columns:minmax(110px,1fr) 1fr 120px 84px;gap:18px;align-items:center;padding:' + (r[2] ? '16px' : '12px') + ' 0;border-bottom:1px solid ' + C.line + '">' +
           '<div style="' + lab + (r[2] ? ';color:' + C.ink : '') + '">' + r[1] + '</div>' + spark(r[0], 91, r[2] ? 34 : 24) +
           '<div style="text-align:right">' + num(r[0], r[2] ? '28px' : '18px') + '</div><div style="text-align:right">' + chg(r[0], r[2] ? '14px' : '12.5px') + '</div></div>';
       }).join('') + '</div></div>'
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
  // a computer can take a different look from the phone: data-wide-look on the <script> tag (?splash= previews both)
  var wl = +(pv || me.dataset.wideLook || look);
  var looks = app === 'desk' ? D : N, wideLook = wide && (app === 'desk' ? DW : NW)[wl];
  var tw = app === 'news' && wl === 2 && wideLook && !still && (q.has('typewide') || me.dataset.wideType === '1');
  if (tw) {
    el.className = 'tw';
    // until its turn each block is hidden; the rules of the stories' columns stay up as the empty page
    css += '#splash.tw .wcol,#splash.tw [data-w]:not(.tw-on){visibility:hidden}' +
      '#splash.tw [data-w=stories]:not(.tw-on){visibility:visible}#splash.tw [data-w=stories]>div:not(.tw-on)>*{visibility:hidden}' +
      // the dividers: none on the empty page; they all come up together once the whole page is written
      '#splash.tw [data-r],#splash.tw [data-w=body],#splash.tw [data-w=stories],#splash.tw [data-w=stories]>div,#splash.tw [data-w=watch]{transition:border-color .6s ease,column-rule-color .6s ease}' +
      '#splash.tw:not(.r-lead) [data-r=lead]{border-right-color:transparent!important}#splash.tw:not(.r-lead) [data-w=body]{column-rule-color:transparent!important}' +
      '#splash.tw:not(.r-stories) [data-w=stories],#splash.tw:not(.r-stories) [data-w=stories]>div{border-color:transparent!important}' +
      '#splash.tw:not(.r-watch) [data-w=watch]{border-top-color:transparent!important}';
  }
  el.innerHTML = '<style>' + css + '</style>' + (wideLook || looks[look] || looks[1]) +
    (tapOpen ? '<div class="late tap-hint">' + (phone ? 'Tap' : 'Click') + ' to open</div>' : '');
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
      put('body', '<p style="font:400 14.5px/21px ' + P.body + ',Georgia,serif;text-align:justify;hyphens:auto">' + esc(body.replace(/\s*Why it matters:.*$/, '')) + '</p>');
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
      put('number', '<div style="' + kick + ';color:' + P.sheet + ';opacity:.7">Number of the day</div>' + (fig ? '<div style="margin-top:8px;font:900 32px/1.05 \'Playfair Display\',Georgia,serif">' + esc(fig) + '</div>' : '') +
        '<p style="margin-top:8px;font:400 14px/1.4 ' + P.body + ',Georgia,serif;color:' + P.sheet + ';opacity:.88;' + clamp(4) + '">' + esc(rest) + '</p>');
    }
    var qt = hits['quote of the day'];
    if (qt) {
      var qm = qt.match(/^["“](.+?)["”]\s*(.*)$/);
      put('quote', '<div style="' + kick + '">Quote of the day</div><p style="margin-top:7px;font:italic 700 16px/1.3 \'Playfair Display\',Georgia,serif;' + clamp(4) + '">“' + esc(qm ? qm[1] : qt) + '”</p>' +
        (qm && qm[2] ? '<div style="margin-top:6px;font:500 12px/1.35 Inter,system-ui,sans-serif;color:' + P.ink2 + ';' + clamp(2) + '">' + esc(qm[2]) + '</div>' : ''));
    }
    var more = g.slice(1, 7);
    if (more.length) put('stories', more.map(function (s, i) {
      return '<div style="padding:12px ' + (i % 3 === 2 ? '0' : '20px') + ' 12px ' + (i % 3 === 0 ? '0' : '20px') + ';' + (i % 3 ? 'border-left:' + rule + ';' : '') + (i >= 3 ? 'border-top:' + rule + ';' : '') + '">' +
        '<div style="' + kick + '">' + esc(s.k) + '</div><div style="margin-top:5px;font:700 16px/1.25 \'Playfair Display\',Georgia,serif;text-wrap:pretty;' + clamp(2) + '">' + esc(s.t) + '</div></div>';
    }).join(''));
    // what to watch: its first three items in three columns under the stories' three, up to two lines each
    if (watch) put('watch', '<div style="' + kick + ';color:' + P.ink + '">What to watch today</div>' +
      '<div style="display:grid;grid-template-columns:repeat(3,1fr);margin-top:6px">' +
      watch.split(/;\s*/).filter(Boolean).slice(0, 3).map(function (x, i) {
        return '<div style="padding:0 ' + (i === 2 ? '0' : '20px') + ' 0 ' + (i === 0 ? '0' : '20px') + ';font:500 13px/1.4 Inter,system-ui,sans-serif;text-wrap:pretty;' + clamp(2) + '">' +
          esc(x.replace(/\.$/, '').replace(/^./, function (c) { return c.toUpperCase(); })) + '</div>';
      }).join('') + '</div>');
    fitSheet();
    if (window.ResizeObserver) new ResizeObserver(fitSheet).observe(el);
    if (d.fonts && d.fonts.ready) d.fonts.ready.then(fitSheet);
    if (tw) writeOut();
  };
  // on a shorter window the front page keeps what fits: first the second row of stories goes, then the quote, and what
  // to watch only last; nothing is left cut through at the foot of the sheet
  var fitSheet = function () {
    var sh = el.children[1], st = [].slice.call(el.querySelectorAll('[data-w="stories"] > div'));
    var groups = [st.slice(3), [el.querySelector('[data-w="quote"]')], [el.querySelector('[data-w="watch"]')]];
    groups.forEach(function (g) { g.forEach(function (n) { if (n) n.style.display = ''; }); });
    // the foot may run into half the sheet's bottom margin, never past it
    var room = sh.clientHeight + parseFloat(getComputedStyle(sh).paddingBottom) / 2;
    for (var i = 0; i < groups.length && sh.scrollHeight > room; i++)
      groups[i].forEach(function (n) { if (n) n.style.display = 'none'; });
  };
  // the typed front page on a computer: every block is laid out at once with its words see-through, then they are
  // written out one block after another (each block's own colours kept), so nothing on the sheet moves
  var prep = function (box) {
    var nodes = [], w = d.createTreeWalker(box, NodeFilter.SHOW_TEXT), t, n = 0;
    while ((t = w.nextNode())) if (t.nodeValue.trim()) nodes.push(t);
    var cols = nodes.map(function (t) { return getComputedStyle(t.parentNode).color; });
    var parts = nodes.map(function (t, i) {
      var par = t.parentNode, c = cols[i], a = d.createElement('span'), b = d.createElement('span');
      a.style.color = c; b.style.color = 'transparent'; b.textContent = t.nodeValue;
      par.insertBefore(a, t); par.insertBefore(b, t); par.removeChild(t);
      par.style.color = 'transparent'; // a line cut short shows its "…" only once written
      n += b.textContent.length;
      return { a: a, b: b, par: par, c: c, s: b.textContent };
    });
    return { box: box, parts: parts, len: n };
  };
  var write = function (job, ms, done) {
    // a few letters at a time on long blocks, so each block takes the time it is given (timers do not run under ~4ms)
    var step = Math.max(16, ms / (job.len || 1)), per = Math.max(1, Math.round(job.len * step / (ms || 1))), k = 0, p = 0;
    job.box.classList.add('tw-on');
    var tick = function () {
      for (var m = 0; m < per; m++) {
        var x = job.parts[k];
        if (!x) { job.parts.forEach(function (y) { y.par.style.color = y.c; }); return done(); }
        p++; x.a.textContent = x.s.slice(0, p); x.b.textContent = x.s.slice(p);
        if (p >= x.s.length) { k++; p = 0; }
      }
      setTimeout(tick, step);
    };
    tick();
  };
  var writeOut = function () {
    var q = el.querySelector.bind(el), jobs = [];
    var add = function (box, msPerChar, cap) { if (box && box.offsetParent !== null) { var j = prep(box); j.ms = Math.min(cap, j.len * msPerChar); jobs.push(j); return j; } };
    add(q('[data-w="lead-kick"]'), 28, 320);
    add(q('[data-w="lead"]'), 32, 2300);
    add(q('[data-w="body"]'), 4.5, 1600);
    add(q('[data-w="number"]'), 13, 1150);
    add(q('[data-w="quote"]'), 10, 1300);
    el.querySelectorAll('[data-w="stories"] > div').forEach(function (c) { add(c, 12, 800); });
    add(q('[data-w="watch"]'), 6, 1150);
    var run = function () {
      var j = jobs.shift();
      if (!j) { ['lead', 'stories', 'watch', 'done'].forEach(function (k) { el.classList.add('r-' + k); }); return; }
      write(j, j.ms, function () { setTimeout(run, 140); });
    };
    setTimeout(run, Math.max(0, 700 - (Date.now() - t0)));
  };
  // the phone's front page writes its headline out from the first letter, as if being typed. The whole line is laid out
  // at once (the part still to come is see-through), so the words never jump to a new line as they are written.
  var type = function (n, t) {
    if (!n) return;
    var i = 0, w = t.length, step = Math.max(14, Math.min(32, 2600 / (w || 1)));
    n.innerHTML = '<span></span><span style="color:transparent"></span>';
    var a = n.firstChild, b = n.lastChild;
    var tick = function () { a.textContent = t.slice(0, i); b.textContent = t.slice(i); if (i++ < w) setTimeout(tick, step); };
    n.classList.add('on'); n.style.transition = 'none';
    setTimeout(tick, Math.max(0, 600 - (Date.now() - t0)));
  };
  var newest = function (list) { return list.slice().sort(function (a, b) { return (b.id || b.date) < (a.id || a.date) ? -1 : 1; })[0]; };
  var json = function (u) {
    if (app === 'desk') { var M = window.__deskGet || (window.__deskGet = {}); return M[u] || (M[u] = fetch(u, { cache: 'no-cache' }).then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; })); }
    return fetch(u, { cache: 'no-cache' }).then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; });
  };
  if (app === 'news') {
    json('/editions/index.json').then(function (x) {
      var e = x && x.editions && x.editions.length && newest(x.editions); if (!e) return;
      set('date', longDate(e.date)); set('year', e.date.slice(0, 4));
      if (!wideLook && look === 2 && !still) type(el.querySelector('[data-k="summary"]'), e.summary || ''); else set('summary', esc(e.summary || ''));
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
    if (look !== 3 || wideLook) json('/data/markets-recent.json').then(function (x) {
      var days = x && x.days; if (!days) return;
      // the lines: the last n sessions of each series, the EGX30's in the day's colour with a soft fill under it
      // n: calendar days back from the newest day, so every line covers the same stretch of time
      var last = new Date(days[days.length - 1].date + 'T00:00:00Z').getTime();
      var series = function (k, n) { var v = [], from = new Date(last - n * 864e5).toISOString().slice(0, 10); days.forEach(function (r) { if (r[k] != null && r.date >= from) v.push(r[k]); }); return v; };
      var egx = series('egx30', 7).slice(-2), egxDay = egx.length > 1 ? egx[1] - egx[0] : 0;
      el.querySelectorAll('svg[data-sp]').forEach(function (sv, si) {
        var k = sv.getAttribute('data-sp'), v = series(k, +sv.getAttribute('data-n')); if (v.length < 2) return;
        var H = +sv.getAttribute('viewBox').split(' ')[3], lo = Math.min.apply(0, v), hi = Math.max.apply(0, v), r = hi - lo || 1;
        var pts = v.map(function (y, i) { return (i / (v.length - 1) * 100).toFixed(2) + ',' + (2 + (1 - (y - lo) / r) * (H - 4)).toFixed(2); });
        var big = sv.hasAttribute('data-area'), up = big ? egxDay >= 0 : v[v.length - 1] >= v[0];
        var col = big ? (egxDay > 0 ? C.up : egxDay < 0 ? C.down : C.acc) : C.mute;
        var id = 'spg' + si;
        sv.innerHTML = (big ? '<defs><linearGradient id="' + id + '" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="' + col + '" stop-opacity=".28"/><stop offset="1" stop-color="' + col + '" stop-opacity="0"/></linearGradient></defs>' +
          '<path d="M0,' + H + ' L' + pts.join(' L') + ' L100,' + H + 'Z" fill="url(#' + id + ')"/>' : '') +
          '<polyline points="' + pts.join(' ') + '" fill="none" stroke="' + col + '" stroke-width="' + (big ? 2 : 1.5) + '" vector-effect="non-scaling-stroke" stroke-linejoin="round" stroke-linecap="round"/>';
        sv.style.opacity = 0; sv.style.transition = 'opacity .5s ease'; requestAnimationFrame(function () { sv.style.opacity = 1; });
      });
      [['egx30-3m', 91, 'three months'], ['egx30-6m', 182, 'six months']].forEach(function (p) {
        var v = series('egx30', p[1]); if (v.length < 2) return;
        var c = (v[v.length - 1] / v[0] - 1) * 100;
        set(p[0], (c >= 0 ? '+' : '−') + Math.abs(c).toFixed(1) + '% in ' + p[2]);
      });
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
        if (k === 'egx30' && Math.abs(c) >= 0.005) el.querySelectorAll('.mk-line').forEach(function (n) { n.setAttribute('stroke', c > 0 ? C.up : C.down); if (c < 0) n.classList.add('down'); });
      });
    });
  }

  // ---- leave once the page is ready (MIN to MAX after launch); on a phone or a computer it waits for a tap or a click
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
