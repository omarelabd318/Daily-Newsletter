// Renders the home-screen icons in icons/, and the browser-tab icons (*-tab-*.png): the same art, shrunk. Run: node icons/make_icons.js [newsletter|desk]
// (needs Playwright + network for Google Fonts; with a name, only that app's icons are rendered)
const { chromium } = require('playwright');
const path = require('path');
const art = {
  // a front page in the newsletter's paper colours: the sheet on the paper's ground, blackletter "Daily" masthead,
  // double rule, headline bar, a column of text and a photo block
  newsletter: s => `<div style="width:100%;height:100%;background:#cfc9ba;display:grid;place-items:center">
    <svg style="transform:scale(${s})" width="240" height="240" viewBox="0 0 240 240">
      <defs><filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="5" stdDeviation="7" flood-color="#3c321e" flood-opacity=".28"/></filter></defs>
      <rect x="46" y="30" width="148" height="184" rx="3" fill="#e8e3d6" filter="url(#sh)"/>
      <text x="120" y="82" text-anchor="middle" style="font-family:'UnifrakturCook';font-weight:700;font-size:44px" fill="#14110d">Daily</text>
      <path d="M60 94h120" stroke="#14110d" stroke-width="4"/><path d="M60 101h120" stroke="#14110d" stroke-width="1.6"/>
      <rect x="60" y="113" width="120" height="14" fill="#14110d"/>
      <g stroke="#14110d" stroke-width="5" stroke-linecap="round"><path d="M62 144h50M62 158h50M62 172h50M62 186h36"/></g>
      <rect x="124" y="139" width="56" height="52" fill="#14110d" opacity=".85"/></svg></div>`,
  // the desk's rising line in the brand teal, with a cream rule
  desk: s => `<div style="width:100%;height:100%;background:#16181a;display:grid;place-items:center">
    <svg style="transform:scale(${s})" width="240" height="240" viewBox="0 0 240 240">
      <path d="M48 168l46-46 34 26 64-80" fill="none" stroke="#52d6b5" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M48 196h144" stroke="#faf8f3" stroke-width="5"/></svg></div>`,
};
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const [name, f] of Object.entries(art).filter(([n]) => !process.argv[2] || n === process.argv[2])) {
    for (const [file, n, s] of [[`${name}-192.png`, 192, 1], [`${name}-512.png`, 512, 1],
                                [`${name}-maskable-512.png`, 512, 0.8], [`${name}-apple-180.png`, 180, 1]]) {
      await p.setViewportSize({ width: n, height: n });
      await p.setContent(`<html><head><link href="https://fonts.googleapis.com/css2?family=UnifrakturCook:wght@700&display=block" rel="stylesheet"></head>
        <body style="margin:0;width:${n}px;height:${n}px;overflow:hidden"><div style="width:240px;height:240px;transform:scale(${n / 240});transform-origin:0 0">${f(s)}</div></body></html>`);
      await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
      await p.screenshot({ path: path.join(__dirname, file) });
    }
    for (const n of [32, 64]) {
      await p.setViewportSize({ width: n, height: n });
      await p.setContent(`<html><head><link href="https://fonts.googleapis.com/css2?family=UnifrakturCook:wght@700&display=block" rel="stylesheet"></head>
        <body style="margin:0;width:${n}px;height:${n}px;overflow:hidden"><div style="width:240px;height:240px;transform:scale(${n / 240});transform-origin:0 0">${art[name](1)}</div></body></html>`);
      await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
      await p.screenshot({ path: path.join(__dirname, `${name}-tab-${n}.png`) });
    }
  }
  await b.close();
})();
