// Shared shell and helpers for the desk's pages (EGX, EGP, US, Global, Stocks); the dashboard has its own.
window.Desk = (function () {
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const MINUS = '−';
  const pct = (v, d = 1) => v == null ? '—' : (v > 0 ? '+' : v < 0 ? MINUS : '') + Math.abs(v).toFixed(d) + '%';
  const cls = (v) => v == null ? 'dash' : v > 0 ? 'chg up' : v < 0 ? 'chg down' : 'chg flat';
  const num = (v, d = 2) => v == null ? '—' : v.toLocaleString('en-GB', { minimumFractionDigits: d, maximumFractionDigits: d });
  const get = (u) => fetch(u, { cache: 'no-cache' }).then((r) => r.ok ? r.json() : null).catch(() => null);
  let ASOF = null, DESK = null;
  const day = (iso) => new Date(iso + 'T12:00:00');
  const cut = (iso, back) => new Date(day(iso) - back * 864e5).toISOString().slice(0, 10);
  const short = (iso) => day(iso).toLocaleDateString('en-GB', { day: 'numeric', month: 'short' });
  const PERIODS = [['1D', 0, 'Last 7 days'], ['1W', 7, 'Last 7 days'], ['1M', 30, 'Last 30 days'], ['6M', 182, 'Last 6 months'], ['1Y', 365, 'Last 12 months']];
  const NAMES = { COMI: 'Commercial International Bank', TMGH: 'Talaat Moustafa', ETEL: 'Telecom Egypt', PHDC: 'Palm Hills', SWDY: 'Elsewedy Electric', ORAS: 'Orascom Construction', FWRY: 'Fawry', ABUK: 'Abu Qir Fertilizers', HRHO: 'EFG Holding', CLHO: 'Cleopatra Hospital', JUFO: 'Juhayna', ALCN: 'Alexandria Containers',
    AAPL: 'Apple', MSFT: 'Microsoft', NVDA: 'Nvidia', AMZN: 'Amazon', GOOGL: 'Alphabet', META: 'Meta', TSLA: 'Tesla', JPM: 'JPMorgan Chase', XOM: 'Exxon Mobil', AVGO: 'Broadcom', 'BRK.B': 'Berkshire Hathaway', WMT: 'Walmart' };
  const GROUP = { egx: ['COMI', 'TMGH', 'ETEL', 'PHDC', 'SWDY', 'ORAS', 'FWRY', 'ABUK', 'HRHO', 'CLHO', 'JUFO', 'ALCN'], us: ['AAPL', 'MSFT', 'NVDA', 'AMZN', 'GOOGL', 'META', 'TSLA', 'JPM', 'XOM', 'AVGO', 'BRK.B', 'WMT'] };
  const PAGES = [['/desk/', 'Dashboard', 'M2 13h12M4 10l3-3 2 2 4-5'], ['/desk/egx/', 'EGX', 'M2 13h12M3 10h2v3H3zM7 7h2v6H7zM11 4h2v9h-2z'], ['/desk/egp/', 'EGP', 'M8 2v12M11 4.5H6.5a2 2 0 000 4h3a2 2 0 010 4H5'],
    ['/desk/us/', 'US', 'M2 4h12v8H2zM2 7h12'], ['/desk/global/', 'Global', 'M8 2.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11zM2.5 8h11M8 2.5c1.8 1.6 1.8 9.4 0 11M8 2.5c-1.8 1.6-1.8 9.4 0 11'], ['/desk/stock/', 'Stocks', 'M3 3h10v10H3zM3 6.5h10M6.5 6.5V13']];

  let days = [];
  function series(pick, market) {
    const out = [];
    for (const e of days) {
      const v = pick(e); if (typeof v !== 'number') continue;
      const d = new Date(day(e.date) - 864e5), wd = d.getDay(), iso = d.toISOString().slice(0, 10);
      if (iso > ASOF) continue;
      if (market === 'egx' && (wd === 5 || wd === 6)) continue;
      if (market === 'us' && (wd === 6 || wd === 0)) continue;
      if (out.length && out[out.length - 1][0] === iso) continue;
      out.push([iso, v]);
    }
    return out;
  }
  const valueAt = (s, iso) => { let v = null; for (const [d, x] of s) { if (d <= iso) v = x; else break; } return v; };
  const last = (s) => s.length ? s[s.length - 1][1] : null;
  const change = (s, back) => {
    if (s.length < 2) return null;
    const base = back ? valueAt(s, cut(ASOF, back)) : s[s.length - 2][1];
    return base ? (last(s) / base - 1) * 100 : null;
  };
  const ytd = (s) => { const b = valueAt(s, (ASOF.slice(0, 4) - 1) + '-12-31'); return b && s.length ? (last(s) / b - 1) * 100 : null; };
  const range52 = (s) => { const p = s.filter(([d]) => d >= cut(ASOF, 365)).map((x) => x[1]); return [Math.min(...p), Math.max(...p)]; };
  const stock = (t) => series((e) => (e[GROUP.egx.includes(t) ? 'egx' : 'us'] || {})[t], GROUP.egx.includes(t) ? 'egx' : 'us');

  function segment(el, start, onPick, list = PERIODS) {
    el.innerHTML = list.map((p) => `<button type="button" aria-pressed="${p[0] === start}">${p[0]}</button>`).join('');
    el.querySelectorAll('button').forEach((b, i) => b.addEventListener('click', () => {
      el.querySelectorAll('button').forEach((x) => x.setAttribute('aria-pressed', x === b)); onPick(list[i]);
    }));
  }
  function spark(s, back) {
    const pts = (back <= 7 ? s.slice(-7) : s.filter(([d]) => d >= cut(ASOF, back))).map((x) => x[1]);
    if (pts.length < 2) return '';
    const w = 72, h = 18, min = Math.min(...pts), max = Math.max(...pts), sp = max - min || 1, st = (w - 4) / (pts.length - 1);
    const xy = pts.map((v, i) => [2 + i * st, h - 2 - (v - min) / sp * (h - 4)]);
    return `<svg class="spark" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" aria-hidden="true"><path d="${xy.map((c, i) => (i ? 'L' : 'M') + c[0].toFixed(1) + ' ' + c[1].toFixed(1)).join('')}"/><circle cx="${xy.at(-1)[0].toFixed(1)}" cy="${xy.at(-1)[1].toFixed(1)}" r="2.2"/></svg>`;
  }
  // a line chart of one series over a period (at least a month), with the biggest day marked when it stands out
  function chart(el, s, back, name, fmt, opts = {}) {
    const pts = s.filter(([d]) => d >= cut(ASOF, Math.max(back, 30))); el.innerHTML = '';
    if (pts.length < 2) { el.textContent = 'Not enough closes logged yet.'; return; }
    const vals = pts.map((x) => x[1]), lo = Math.min(...vals), hi = Math.max(...vals), pad = (hi - lo) * 0.15 || lo * 0.01;
    const big = pts.reduce((m, x, i) => i && Math.abs(x[1] / pts[i - 1][1] - 1) > Math.abs(m.v) ? { i, v: x[1] / pts[i - 1][1] - 1 } : m, { i: -1, v: 0 });
    const ann = opts.mark !== false && big.i > 0 && Math.abs(big.v) > (opts.markAt || 0.025) ? [{ at: big.i, label: `${short(pts[big.i][0])} ${pct(big.v * 100)}`, short: pct(big.v * 100) }] : [];
    Charts.line(el, { labels: pts.map((x) => short(x[0])), series: [{ name, values: vals, muted: !!opts.muted }], format: fmt, annotations: ann, endLabel: true, height: el.clientHeight, min: lo - pad, xAt: opts.xAt ? [0, Math.floor((pts.length - 1) / 2), pts.length - 1] : null });
  }
  function movers(el, tickers, back, n = 3) {
    const rows = tickers.map((t) => ({ t, c: change(stock(t), back), v: last(stock(t)) })).filter((r) => r.c != null).sort((a, b) => b.c - a.c);
    const row = (r) => `<div class="mv"><a href="/desk/stock/?t=${encodeURIComponent(r.t)}"><b>${esc(NAMES[r.t])}</b><span class="t">${esc(r.t)}</span></a><span class="num">${num(r.v)}</span><span class="num ${cls(r.c)}">${pct(r.c)}</span></div>`;
    el.innerHTML = `<div class="movers"><div><h3><span class="chg up" aria-hidden="true"></span>Biggest gainers</h3>${rows.slice(0, n).map(row).join('')}</div><div><h3><span class="chg down" aria-hidden="true"></span>Biggest losers</h3>${rows.slice(-n).reverse().map(row).join('')}</div></div>`;
  }
  function stockTable(body, tickers, back) {
    body.innerHTML = tickers.map((t) => {
      const s = stock(t), c = change(s, back), y = ytd(s);
      return `<tr class="click" onclick="location='/desk/stock/?t=${encodeURIComponent(t)}'"><td class="name"><a href="/desk/stock/?t=${encodeURIComponent(t)}"><b>${esc(NAMES[t])}</b><span>${esc(t)}</span></a></td><td class="trend">${spark(s, back)}</td><td class="num">${num(last(s))}</td><td class="num"><span class="${cls(c)}">${pct(c)}</span></td><td class="num"><span class="${cls(y)}">${pct(y)}</span></td></tr>`;
    }).join('');
  }
  const kv = (rows) => '<div class="kv">' + rows.map(([k, v]) => `<span class="k">${esc(k)}</span><span class="v num">${v}</span>`).join('') + '</div>';
  const rangeBar = (lo, hi, v, f = (x) => num(x)) => `<div class="range"><i style="left:calc(${((v - lo) / (hi - lo || 1) * 100).toFixed(1)}% - 1px)"></i></div><div class="range-l"><span>52-week low ${f(lo)}</span><span>high ${f(hi)}</span></div>`;

  // bullish and bearish: sectors with a reason, stocks with a projected range, each with a confidence level
  function outlook(el, O, cur) {
    const conf = (c) => `<span class="conf ${c}">${c[0].toUpperCase() + c.slice(1)}</span>`;
    const sector = (x) => `<div class="ol"><div class="ol-h"><b style="font-weight:500">${esc(x.name)}</b>${conf(x.confidence)}</div><p>${esc(x.why)}</p></div>`;
    const stockRow = (x) => {
      const s = stock(x.t), v = last(s), lo = (x.range[0] / v - 1) * 100, hi = (x.range[1] / v - 1) * 100;
      return `<div class="ol"><div class="ol-h"><a href="/desk/stock/?t=${encodeURIComponent(x.t)}">${esc(NAMES[x.t])}<span class="t">${esc(x.t)} · ${num(v)}</span></a>${conf(x.confidence)}</div>
        <div class="proj">Projection: <b class="num">${cur === '$' ? '$' : cur + ' '}${num(x.range[0], x.dp ?? 2)}–${num(x.range[1], x.dp ?? 2)}</b> by ${esc(x.by)} <span class="num">(${pct(lo, 0)} to ${pct(hi, 0)})</span></div>
        <p>${esc(x.why)}</p><p class="wrong"><b>Wrong if</b> ${esc(x.wrong)}</p></div>`;
    };
    const side = (k, label, arrow) => `<div><h3><span class="chg ${arrow}" aria-hidden="true"></span>${label}</h3><h4>Sectors</h4>${O[k].sectors.map(sector).join('')}<h4>Stocks</h4>${O[k].stocks.map(stockRow).join('')}</div>`;
    el.innerHTML = `<div class="outlook">${side('bull', 'Bullish', 'up')}${side('bear', 'Bearish', 'down')}</div>
      <p class="ol-key"><b>Confidence.</b> High: several independent reasons and the figures agree. Medium: a clear driver, with cross-currents. Low: momentum, or one reason only. Projections are the desk's view, not advice; each is scored here, right or wrong, when its date passes.</p>`;
  }

  async function init(page) {
    const icon = (d) => `<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke-width="1.5"><path d="${d}"/></svg>`;
    const links = PAGES.map(([h, n, d]) => `<a href="${h}"${h === page ? ' aria-current="page"' : ''}>${icon(d)}${n}</a>`);
    const shell = document.createElement('div');
    shell.className = 'app';
    shell.innerHTML = `<aside class="side" aria-label="Markets Desk">
      <div class="brand"><span class="mark" aria-hidden="true"><svg width="18" height="18" viewBox="0 0 18 18"><path d="M2 13l4-4 3 2.5L16 4" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span><b>Markets Desk</b><span>Daily Newsletter · EGP</span></span></div>
      <nav class="nav" aria-label="Main"><div class="navgroup">Today</div>${links[0]}<div class="navgroup">Markets</div>${links.slice(1, 5).join('')}<div class="navgroup">Stocks</div>${links[5]}
      <div class="navgroup">Newsletter</div><a href="/">${icon('M3 2.5h10v11H3zM5.5 5.5h5M5.5 8h5M5.5 10.5h3')}Today's newsletter</a></nav>
      <div class="side-foot"><button type="button" class="theme"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M8 2a6 6 0 100 12A4.5 4.5 0 018 2z"/></svg><span>Dark mode</span></button>Cairo · prices in EGP unless marked</div></aside>
      <div><header class="topbar"><div class="brand"><span class="mark" aria-hidden="true"><svg width="18" height="18" viewBox="0 0 18 18"><path d="M2 13l4-4 3 2.5L16 4" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span><b>Markets Desk</b></span></div><a class="btn" href="/">Newsletter</a></header>
      <nav class="pagenav" aria-label="Pages">${PAGES.map(([h, n]) => `<a href="${h}"${h === page ? ' aria-current="page"' : ''}>${n}</a>`).join('')}</nav></div>`;
    const main = document.querySelector('main.canvas');
    shell.lastElementChild.appendChild(main);
    document.body.prepend(shell);
    theme();
    const idx = await get('/desk/index.json');
    const latest = idx && idx.desks && idx.desks.length ? idx.desks.map((d) => d.date).sort().at(-1) : null;
    DESK = latest ? await get('/desk/days/' + latest + '.json') : null;
    if (!DESK) { main.innerHTML = '<p class="finding">No desk has been published yet.</p>'; return null; }
    ASOF = DESK.asOf;
    const log = await get('/data/markets-recent.json');
    days = (log && log.days) || [];
    if (DESK.sample) document.querySelectorAll('[data-sample]').forEach((e) => { e.hidden = false; });
    return DESK;
  }
  const dateLine = (iso) => day(iso).toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long' });
  const conf = (c) => `<span class="conf ${c === 'high' ? 'high' : ''}">${esc(c[0].toUpperCase() + c.slice(1))}</span>`;
  // rows of a named driver, a confidence level and a line of reasoning
  const drivers = (rows) => rows.map((r) => `<div class="drv"><b>${esc(r.name)}</b>${r.move ? `<span class="num ${r.move.trim().startsWith('−') || r.move.trim().startsWith('-') ? 'chg down' : 'chg up'}">${esc(r.move)}</span>` : conf(r.confidence)}<span class="why">${esc(r.why)}</span></div>`).join('');
  function theme() {
    const tb = document.querySelector('.theme'); if (!tb) return;
    const lab = tb.querySelector('span');
    const sync = () => { lab.textContent = document.documentElement.getAttribute('data-theme') === 'dark' ? 'Light mode' : 'Dark mode'; };
    sync();
    tb.addEventListener('click', () => {
      const dark = document.documentElement.getAttribute('data-theme') !== 'dark';
      if (dark) document.documentElement.setAttribute('data-theme', 'dark'); else document.documentElement.removeAttribute('data-theme');
      try { localStorage.setItem('theme', dark ? 'dark' : 'light'); } catch (e) {}
      location.reload();
    });
  }
  return { get ASOF() { return ASOF; }, $, esc, pct, cls, num, get, dateLine, conf, drivers, day, cut, short, PERIODS, NAMES, GROUP, series, valueAt, last, change, ytd, range52, stock, segment, spark, chart, movers, stockTable, kv, rangeBar, outlook, init };
})();
