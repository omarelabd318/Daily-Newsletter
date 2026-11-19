// Renders the iPhone startup images in icons/startup/: what an iPhone shows while a home-screen app starts, before the
// page has loaded. Each is the first frame of that app's opening screen (splash.js), so the screen carries straight on:
// the Newsletter's sheet before it grows, the Desk's chart mark already drawn.
// Run from the repo root with the site served locally:
//   python3 -m http.server 8765 --bind 127.0.0.1   then   node icons/make_startup.js
// It also prints the <link> tags for index.html and desk/egypt/index.html.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

// iPhone screens in CSS pixels and their pixel ratio (portrait)
const PHONES = [
  [440, 956, 3], // 16 Pro Max, 17 Pro Max
  [420, 912, 3], // Air
  [402, 874, 3], // 16 Pro, 17, 17 Pro
  [430, 932, 3], // 14 Pro Max, 15 Plus, 15 Pro Max, 16 Plus
  [393, 852, 3], // 14 Pro, 15, 15 Pro, 16, 16e
  [428, 926, 3], // 12 Pro Max, 13 Pro Max, 14 Plus
  [390, 844, 3], // 12, 12 Pro, 13, 13 Pro, 14
  [414, 896, 3], // XS Max, 11 Pro Max
  [414, 896, 2], // XR, 11
  [375, 812, 3], // X, XS, 11 Pro, 12 mini, 13 mini
  [375, 667, 2], // SE (2nd and 3rd), 8
];
const APPS = {
  // the sheet at the size it starts from, with nothing on it yet but the nameplate and rules
  news: { url: '/?splash=2&hold', theme: { theme: 'paper' }, css: '', rewind: true },
  // the mark drawn, the rest of the screen still empty
  desk: { url: '/desk/egypt/?splash=1&hold', theme: { deskTheme: 'dark' },
    css: '#splash *{animation:none!important} #splash .in,#splash .late{opacity:0!important} #splash .mk-line{stroke-dashoffset:0!important}' },
};

(async () => {
  const out = path.join(__dirname, 'startup');
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const tags = { news: [], desk: [] };
  for (const [app, A] of Object.entries(APPS)) {
    for (const [w, h, r] of PHONES) {
      const ctx = await b.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: r });
      await ctx.addInitScript((t) => { for (const k in t) localStorage.setItem(k, t[k]); }, A.theme);
      const p = await ctx.newPage();
      // no data: the first frame is drawn before the day's details arrive
      await p.route(/editions\/index\.json|desk\/index\.json|markets-recent\.json/, (rt) => rt.abort());
      await p.goto('http://127.0.0.1:8765' + A.url, { waitUntil: 'networkidle' });
      if (A.css) await p.addStyleTag({ content: A.css });
      // back to the opening frame: every animation paused at its start
      if (A.rewind) await p.evaluate(() => document.getAnimations().forEach((a) => { a.pause(); a.currentTime = 0; }));
      await p.evaluate(() => document.fonts.ready);
      await p.waitForTimeout(150);
      const name = `${app}-${w * r}x${h * r}.png`;
      await p.locator('#splash').screenshot({ path: path.join(out, name) });
      tags[app].push(`<link rel="apple-touch-startup-image" media="screen and (device-width: ${w}px) and (device-height: ${h}px) and (-webkit-device-pixel-ratio: ${r}) and (orientation: portrait)" href="/icons/startup/${name}">`);
      await ctx.close();
    }
  }
  await b.close();
  for (const app of Object.keys(tags)) console.log(`\n<!-- ${app} -->\n` + tags[app].join('\n'));
})();
