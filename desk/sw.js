// The Markets Desk's offline copy (scope /desk/; the newsletter is not touched).
// - Pages, scripts, styles and fonts open from the saved copy at once and are refreshed in the background.
// - Data (.json) comes from the network when it answers within 2.5 seconds, else from the saved copy, so a slow or
//   dropped connection still shows the last desk instead of a blank page.
// - "Save for offline" in the desk's More menu (nav.js) posts {save: true}: every desk page, script and data file is
//   fetched and kept, with progress posted back as {saved, total}.
const CACHE = 'desk-v1';
const PAGES = ['/desk/egypt/', '/desk/usa/', '/desk/global/', '/desk/egp/', '/desk/egx/', '/desk/us/', '/desk/stocks/egypt/',
  '/desk/stocks/us/', '/desk/stock/', '/desk/sectors/', '/desk/fairvalue/', '/desk/views/', '/desk/week/', '/desk/runs/'];
const ASSETS = ['/desk/dash.css', '/desk/desk.css', '/desk/charts.js', '/desk/dash.js', '/desk/desk.js', '/desk/heat.js',
  '/desk/tags.js', '/desk/nav.js', '/desk/search.js', '/desk/manifest.webmanifest', '/icons/desk-apple-180.png'];
const DATA = ['/desk/index.json', '/desk/intraday.json', '/desk/movers.json', '/desk/stocks.json', '/desk/views.json',
  '/desk/calendar.json', '/desk/fairvalue.json', '/desk/flows.json', '/desk/indicators.json', '/desk/rates.json',
  '/desk/reserves.json', '/desk/rolls.json', '/desk/sectors.json', '/desk/heat/index.json', '/data/markets-recent.json'];

self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', (e) => e.waitUntil((async () => {
  for (const k of await caches.keys()) if (k.startsWith('desk-') && k !== CACHE) await caches.delete(k);
  await self.clients.claim();
})()));

// the stock page and the fair-value page read their query string in the page: one saved copy serves them all
const key = (req) => {
  const u = new URL(req.url);
  if (u.origin === location.origin && (req.mode === 'navigate' || /\/$/.test(u.pathname)) && u.pathname.startsWith('/desk/')) return u.origin + u.pathname;
  return req.url;
};

async function put(k, res) {
  if (res && (res.ok || res.type === 'opaque')) { const c = await caches.open(CACHE); await c.put(k, res.clone()); }
  return res;
}

async function staleWhileRevalidate(e) {
  const k = key(e.request), c = await caches.open(CACHE), hit = await c.match(k);
  const net = fetch(e.request).then((r) => put(k, r)).catch(() => null);
  if (hit) { e.waitUntil(net); return hit; }
  return (await net) || Response.error();
}

async function networkFirst(e) {
  const k = key(e.request), c = await caches.open(CACHE);
  const net = fetch(e.request).then((r) => put(k, r));
  const slow = new Promise((ok) => setTimeout(ok, 2500, null));
  try {
    const r = await Promise.race([net, slow]);
    if (r) return r;
    const hit = await c.match(k);
    if (hit) { e.waitUntil(net.catch(() => {})); return hit; }
    return await net;
  } catch (err) {
    return (await c.match(k)) || Response.error();
  }
}

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const u = new URL(req.url);
  if (/^fonts\.(googleapis|gstatic)\.com$/.test(u.hostname)) return e.respondWith(staleWhileRevalidate(e));
  if (u.origin !== location.origin) return;
  if (/\.(mp3|m4a)$/.test(u.pathname)) return;                       // audio streams by range: leave it to the browser
  if (/\.json$/.test(u.pathname)) return e.respondWith(networkFirst(e));
  if (u.pathname.startsWith('/desk/') || u.pathname.startsWith('/icons/')) return e.respondWith(staleWhileRevalidate(e));
});

self.addEventListener('message', (e) => {
  if (!e.data || !e.data.save) return;
  e.waitUntil((async () => {
    const c = await caches.open(CACHE);
    const tell = async (m) => { for (const cl of await self.clients.matchAll()) cl.postMessage(m); };
    let list = PAGES.concat(ASSETS, DATA);
    // the latest day files (the week page reads seven) and the latest heat maps
    try {
      const ix = await (await fetch('/desk/index.json', { cache: 'no-cache' })).json();
      list = list.concat((ix.desks || []).map((d) => d.date).sort().slice(-8).map((d) => `/desk/days/${d}.json`));
      const hx = await (await fetch('/desk/heat/index.json', { cache: 'no-cache' })).json();
      for (const m of Object.keys(hx || {})) list = list.concat((hx[m] || []).slice().sort().slice(-1).map((d) => `/desk/heat/${m}/${d}.json`));
    } catch (err) {}
    let done = 0, failed = 0;
    await tell({ saved: 0, total: list.length });
    await Promise.all(list.map(async (u) => {
      try { const r = await fetch(u, { cache: 'no-cache' }); if (!r.ok) throw 0; await c.put(location.origin + u, r); } catch (err) { failed++; }
      done++; await tell({ saved: done, total: list.length });
    }));
    await tell({ saved: done, total: list.length, finished: true, failed, at: new Date().toISOString() });
  })());
});
