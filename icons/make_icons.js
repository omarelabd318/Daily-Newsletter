// Renders the home-screen icons in icons/. Run: node icons/make_icons.js (needs Playwright + network for Google Fonts)
const { chromium } = require('playwright');
const path = require('path');
const art = {
  // blackletter D from the masthead, with the masthead's double rule
  newsletter: s => `<div style="width:100%;height:100%;background:#faf8f3;display:grid;place-items:center">
    <div style="transform:scale(${s});width:240px;height:240px;position:relative;display:grid;place-items:center">
      <b style="font:700 190px/1 'UnifrakturCook';color:#16181a;margin-top:-14px">D</b>
      <i style="position:absolute;left:40px;right:40px;bottom:34px;height:6px;border-top:4px solid #16181a;border-bottom:2px solid #16181a"></i></div></div>`,
  // the desk's rising line in the brand teal, with a cream rule
  desk: s => `<div style="width:100%;height:100%;background:#16181a;display:grid;place-items:center">
    <svg style="transform:scale(${s})" width="240" height="240" viewBox="0 0 240 240">
      <path d="M48 168l46-46 34 26 64-80" fill="none" stroke="#52d6b5" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M48 196h144" stroke="#faf8f3" stroke-width="5"/></svg></div>`,
};
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const [name, f] of Object.entries(art)) {
    for (const [file, n, s] of [[`${name}-192.png`, 192, 1], [`${name}-512.png`, 512, 1],
                                [`${name}-maskable-512.png`, 512, 0.8], [`${name}-apple-180.png`, 180, 1]]) {
      await p.setViewportSize({ width: n, height: n });
      await p.setContent(`<html><head><link href="https://fonts.googleapis.com/css2?family=UnifrakturCook:wght@700&display=block" rel="stylesheet"></head>
        <body style="margin:0;width:${n}px;height:${n}px;overflow:hidden"><div style="width:240px;height:240px;transform:scale(${n / 240});transform-origin:0 0">${f(s)}</div></body></html>`);
      await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
      await p.screenshot({ path: path.join(__dirname, file) });
    }
  }
  await b.close();
})();
