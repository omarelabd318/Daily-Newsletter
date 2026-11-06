// Shared shell and helpers for the desk's pages (EGX, EGP, US, Global, Stocks); the dashboard has its own.
window.Desk = (function () {
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const MINUS = '−';
  // a change that rounds to zero shows as 0.0%, with no sign
  const pct = (v, d = 1) => { if (v == null) return '—'; const r = +v.toFixed(d); return (r > 0 ? '+' : r < 0 ? MINUS : '') + Math.abs(r).toFixed(d) + '%'; };
  const cls = (v) => v == null ? 'dash' : v >= 0.05 ? 'chg up' : v <= -0.05 ? 'chg down' : 'chg flat';
  const num = (v, d = 2) => v == null ? '—' : v.toLocaleString('en-US', { minimumFractionDigits: d, maximumFractionDigits: d });
  const get = (u) => fetch(u, { cache: 'no-cache' }).then((r) => r.ok ? r.json() : null).catch(() => null);
  // ASOF is the EGX's last session; each market has its own last close (ASOF_M), since at weekends Wall Street
  // last traded on Friday and the EGX on Thursday. Every series runs up to the day before the desk's date (CUTOFF).
  let ASOF = null, CUTOFF = null, ASOF_M = {}, DESK = null, INTRA = null, MOVERS = null;
  const day = (iso) => new Date(iso + 'T12:00:00');
  const cut = (iso, back) => new Date(day(iso) - back * 864e5).toISOString().slice(0, 10);
  const short = (iso) => day(iso).toLocaleDateString('en-US', { day: 'numeric', month: 'short' }).replace('Sept', 'Sep');
  const PERIODS = [['1D', 0, 'Last 7 days'], ['1W', 7, 'Last 7 days'], ['1M', 30, 'Last 30 days'], ['6M', 182, 'Last 6 months'], ['1Y', 365, 'Last 12 months']];
  const NAMES = { COMI: 'Commercial International Bank', TMGH: 'Talaat Moustafa', ETEL: 'Telecom Egypt', PHDC: 'Palm Hills', SWDY: 'Elsewedy Electric', ORAS: 'Orascom Construction', FWRY: 'Fawry', ABUK: 'Abu Qir Fertilizers', HRHO: 'EFG Holding', CLHO: 'Cleopatra Hospital', JUFO: 'Juhayna', ALCN: 'Alexandria Containers', MFPC: 'MOPCO', EAST: 'Eastern Company', EFIH: 'e-finance', EMFD: 'Emaar Misr', BQDC: 'Banque du Caire', EGAL: 'Egypt Aluminium', AMOC: 'Alexandria Mineral Oils', SKPC: 'Sidi Kerir Petrochemicals', EFID: 'Edita Food Industries',
    AAPL: 'Apple', MSFT: 'Microsoft', NVDA: 'Nvidia', AMZN: 'Amazon', GOOGL: 'Alphabet', META: 'Meta', TSLA: 'Tesla', JPM: 'JPMorgan Chase', XOM: 'Exxon Mobil', AVGO: 'Broadcom', 'BRK.B': 'Berkshire Hathaway', WMT: 'Walmart', V: 'Visa', ORCL: 'Oracle', COST: 'Costco' };
  const GROUP = { egx: ['COMI', 'TMGH', 'ETEL', 'PHDC', 'SWDY', 'ORAS', 'FWRY', 'ABUK', 'HRHO', 'CLHO', 'JUFO', 'ALCN', 'MFPC', 'EAST', 'EFIH', 'EMFD', 'BQDC', 'EGAL', 'AMOC', 'SKPC', 'EFID'], us: ['AAPL', 'MSFT', 'NVDA', 'AMZN', 'GOOGL', 'META', 'TSLA', 'JPM', 'XOM', 'AVGO', 'BRK.B', 'WMT', 'V', 'ORCL', 'COST'] };
  // broad sectors for grouping the stock lists (stocks.json's sector is finer: 15 for 21 Egyptian stocks)
  const SECTORS = {
    egx: [['Banks and financials', ['COMI', 'BQDC', 'HRHO', 'FWRY', 'EFIH']], ['Real estate and construction', ['TMGH', 'PHDC', 'EMFD', 'ORAS']],
      ['Fertilizers, chemicals and oil', ['ABUK', 'MFPC', 'SKPC', 'AMOC']], ['Industrials and transport', ['SWDY', 'EGAL', 'ALCN']],
      ['Consumer', ['JUFO', 'EFID', 'EAST']], ['Telecoms', ['ETEL']], ['Healthcare', ['CLHO']]],
    us: [['Software and hardware', ['AAPL', 'MSFT', 'ORCL']], ['Semiconductors', ['NVDA', 'AVGO']], ['Internet and e-commerce', ['GOOGL', 'META', 'AMZN']],
      ['Financials', ['JPM', 'V', 'BRK.B']], ['Retail', ['WMT', 'COST']], ['Energy', ['XOM']], ['Cars', ['TSLA']]],
  };
  // the menu, by market: Egypt (dashboard, EGP, EGX, stocks), USA (dashboard, Wall Street, stocks), then Global and Views
  const PAGES = [['/desk/egypt/', 'EGY dashboard', 'M2 13h12M4 10l3-3 2 2 4-5'],
    ['/desk/egp/', 'EGP', 'M8 2v12M11 4.5H6.5a2 2 0 000 4h3a2 2 0 010 4H5'],
    ['/desk/egx/', 'EGX', 'M2 13h12M3 10h2v3H3zM7 7h2v6H7zM11 4h2v9h-2z'],
    ['/desk/stocks/egypt/', 'EGX stocks', 'M3 3h10v10H3zM3 6.5h10M6.5 6.5V13'],
    ['/desk/usa/', 'US dashboard', 'M8 2.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11zM2.5 8h11'],
    ['/desk/us/', 'Wall Street', 'M2 4h12v8H2zM2 7h12'],
    ['/desk/stocks/us/', 'Wall Street stocks', 'M3 3h10v10H3zM3 6.5h10M6.5 6.5V13'],
    ['/desk/global/', 'Global', 'M8 2.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11zM2.5 8h11M8 2.5c1.8 1.6 1.8 9.4 0 11M8 2.5c-1.8 1.6-1.8 9.4 0 11'],
    ['/desk/views/', 'Views', 'M3 3.5h10M3 8h10M3 12.5h6M12 11l1.5 1.5L16 10']];

  let days = [], FULL = false;
  // 3Y and 5Y: the long periods, offered on the EGP, EGX30, Gold in Egypt and stock charts; they load the full log
  const LONG = [['3Y', 1095, 'Last 3 years'], ['5Y', 1826, 'Last 5 years']];
  async function full() {
    if (FULL) return;
    const f = await get('/data/markets.json');
    if (f && f.days) { days = f.days; FULL = true; }
  }
  // a small switch of named options (for example EGP and USD); calls onPick with the chosen index
  function toggle(el, names, onPick) {
    el.innerHTML = names.map((n, i) => `<button type="button" aria-pressed="${!i}">${esc(n)}</button>`).join('');
    el.querySelectorAll('button').forEach((b, i) => b.addEventListener('click', () => {
      el.querySelectorAll('button').forEach((x) => x.setAttribute('aria-pressed', x === b)); onPick(i);
    }));
  }
  // a pound series in dollars: each value divided by that day's dollar rate (strips out the pound's moves)
  function usd(s) {
    const fx = series((e) => e.usd_egp, 'fx');
    return s.map(([d, v]) => { const r = valueAt(fx, d); return r ? [d, v / r] : null; }).filter(Boolean);
  }
  function series(pick, market) {
    const out = [];
    for (const e of days) {
      const v = pick(e); if (typeof v !== 'number') continue;
      const d = new Date(day(e.date) - 864e5), wd = d.getDay(), iso = d.toISOString().slice(0, 10);
      if (iso > CUTOFF) continue;
      if (market === 'egx' && (wd === 5 || wd === 6)) continue;
      if (market === 'us' && (wd === 6 || wd === 0)) continue;
      if (out.length && out[out.length - 1][0] === iso) continue;
      out.push([iso, v]);
    }
    return out;
  }
  // a series' own last date: periods count back from it, so each market measures from its own last close
  const lastDate = (s) => (s.length ? s[s.length - 1][0] : ASOF);
  const asOfFor = (m) => ASOF_M[m] || ASOF;
  const valueAt = (s, iso) => { let v = null; for (const [d, x] of s) { if (d <= iso) v = x; else break; } return v; };
  const last = (s) => s.length ? s[s.length - 1][1] : null;
  const change = (s, back) => {
    if (s.length < 2) return null;
    const base = back ? valueAt(s, cut(lastDate(s), back)) : s[s.length - 2][1];
    return base ? (last(s) / base - 1) * 100 : null;
  };
  const ytd = (s) => { const b = valueAt(s, (lastDate(s).slice(0, 4) - 1) + '-12-31'); return b && s.length ? (last(s) / b - 1) * 100 : null; };
  const range52 = (s) => { const p = s.filter(([d]) => d >= cut(lastDate(s), 365)).map((x) => x[1]); return p.length ? [Math.min(...p), Math.max(...p)] : [null, null]; };
  const stock = (t) => series((e) => (e[GROUP.egx.includes(t) ? 'egx' : 'us'] || {})[t], GROUP.egx.includes(t) ? 'egx' : 'us');

  // every visit opens on the defaults; clear the choices an earlier version of the desk remembered
  try { Object.keys(localStorage).filter((k) => k.startsWith('desk:')).forEach((k) => localStorage.removeItem(k)); } catch (e) {}
  // a row of period buttons; 3Y and 5Y sit behind "More" unless one of them is the starting period
  function segment(el, start, onPick, list = PERIODS) {
    const long = (p) => p[1] > 400, tuck = list.some(long) && !long(list.find((p) => p[0] === start) || [0, 0]);
    el.innerHTML = list.map((p) => `<button type="button" aria-pressed="${p[0] === start}"${tuck && long(p) ? ' hidden' : ''}>${p[0]}</button>`).join('')
      + (tuck ? '<button type="button" class="seg-more" aria-label="More periods">More</button>' : '');
    const bs = [...el.querySelectorAll('button:not(.seg-more)')], more = el.querySelector('.seg-more');
    bs.forEach((b, i) => b.addEventListener('click', () => { bs.forEach((x) => x.setAttribute('aria-pressed', x === b)); onPick(list[i]); }));
    if (more) more.addEventListener('click', () => { bs.forEach((b) => { b.hidden = false; }); more.remove(); });
  }
  // a trend line: the period's closes, or on 1D the last session through the day when it is saved (intra)
  // week: on 1W, the last sessions through the day (weekOf), when saved; otherwise the last seven closes
  function spark(s, back, intra = null, week = null) {
    const pts = !back && intra && intra.length > 1 ? intra.map((x) => x[1]) : back === 7 && week && week.length > 1 ? week
      : (back <= 7 ? s.slice(-7) : s.filter(([d]) => d >= cut(lastDate(s), back))).map((x) => x[1]);
    if (pts.length < 2) return '';
    const w = 72, h = 18, min = Math.min(...pts), max = Math.max(...pts), sp = max - min || 1, st = (w - 4) / (pts.length - 1);
    const xy = pts.map((v, i) => [2 + i * st, h - 2 - (v - min) / sp * (h - 4)]);
    return `<svg class="spark" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" aria-hidden="true"><path d="${xy.map((c, i) => (i ? 'L' : 'M') + c[0].toFixed(1) + ' ' + c[1].toFixed(1)).join('')}"/><circle cx="${xy.at(-1)[0].toFixed(1)}" cy="${xy.at(-1)[1].toFixed(1)}" r="2.2"/></svg>`;
  }
  // the biggest move on the chart: consecutive sessions in the same direction count as one move, shaded
  // across its days ("22–25 Oct −6.9%"); a one-day move keeps a marker line. Only moves above the threshold.
  function bigMove(pts, at = 0.025) {
    let best = null;
    for (let i = 1; i < pts.length;) {
      const dir = Math.sign(pts[i][1] - pts[i - 1][1]); let j = i;
      while (j + 1 < pts.length && Math.sign(pts[j + 1][1] - pts[j][1]) === dir && dir) j++;
      const m = pts[j][1] / pts[i - 1][1] - 1;
      if (!best || Math.abs(m) > Math.abs(best.m)) best = { a: i - 1, b: j, m };
      i = j + 1;
    }
    if (!best || Math.abs(best.m) <= at) return [];
    const p = (v) => (v > 0 ? '+' : '−') + Math.abs(v * 100).toFixed(1) + '%';
    const d = (i) => new Date(pts[i][0] + 'T12:00:00'), dd = (i) => d(i).toLocaleDateString('en-US', { day: 'numeric' });
    const mon = (i) => d(i).toLocaleDateString('en-US', { day: 'numeric', month: 'short' }).replace('Sept', 'Sep');
    if (best.b - best.a === 1) return [{ at: best.b, label: `${mon(best.b)} ${p(best.m)}`, short: p(best.m) }];
    const first = best.a + 1, same = d(first).getMonth() === d(best.b).getMonth();
    return [{ from: best.a, to: best.b, label: `${mon(first)}–${same ? dd(best.b) : mon(best.b)} ${p(best.m)}`, short: p(best.m) }];
  }
  // the last session's prices through the day (desk/intraday.json): market 'egx' or 'us', key a ticker,
  // 'EGX30' or 'COMP'. Returns a caption, or null when there is no one-day data for it.
  // stock and index charts open on 1D when the last session through the day is saved, otherwise on 1M
  const startPeriod = (market, key) => (INTRA && INTRA[market] && INTRA[market].series && INTRA[market].series[key] ? PERIODS[0] : PERIODS[2]);
  // a week through the day: the last five sessions the morning run saved (every 15 minutes), one label per day.
  // Returns the caption, or null when fewer than two sessions are saved (the page then draws the daily closes).
  // the pound's rate on a day, for prices through the day in dollars (the market rate is set once a day)
  const rateOn = (iso) => valueAt(series((e) => e.usd_egp, 'fx'), iso);
  // a stock's or index's last sessions through the day (every 15 minutes), joined, for the 1W trend lines; null
  // until two sessions are saved. In dollars, each session at its own day's rate.
  const weekSessions = (m) => ((INTRA && INTRA.week && INTRA.week[m]) || []).filter((x) => x.session <= asOfFor(m));
  function weekOf(t, inUSD = false) {
    const m = GROUP.egx.includes(t) || /^EGX/.test(t) ? 'egx' : 'us';
    const ss = weekSessions(m).filter((x) => x.series[t] && x.series[t].length > 1 && (!inUSD || rateOn(x.session)));
    return ss.length < 2 ? null : ss.flatMap((x) => { const r = inUSD ? rateOn(x.session) : 1; return x.series[t].map(([, v]) => v / r); });
  }
  function weekChart(el, market, key, name, fmt, inUSD = false) {
    const W = INTRA && INTRA.week && INTRA.week[market];
    const ss = (W || []).filter((x) => x.session <= asOfFor(market) && x.series[key] && x.series[key].length > 1 && (!inUSD || rateOn(x.session)));
    if (ss.length < 2) return null;
    const labels = [], vals = [], text = [], at = [];
    ss.forEach((x) => { const d = day(x.session), dl = `${WD[d.getDay()]} ${d.getDate()}`, r = inUSD ? rateOn(x.session) : 1; at.push(labels.length);
      x.series[key].forEach(([t, v]) => { labels.push(`${dl} ${t}`); vals.push(v / r); text.push(dl); }); });
    el.innerHTML = '';
    const lo = Math.min(...vals), hi = Math.max(...vals), pad = (hi - lo) * 0.15 || lo * 0.002;
    Charts.line(el, { labels, xAt: el.clientWidth < 520 && at.length > 3 ? at.filter((_, j) => (at.length - 1 - j) % 2 === 0) : at, xText: text,
      series: [{ name, values: vals }], format: fmt, endLabel: true, height: el.clientHeight, min: lo - pad });
    const ch = (vals.at(-1) / vals[0] - 1) * 100;
    return `Last ${ss.length} sessions through the day${inUSD ? ', in dollars at each day\'s rate' : ''}: <span class="num ${cls(ch)}">${pct(ch, 2)}</span> from the first trade`;
  }
  function dayChart(el, market, key, name, fmt, inUSD = false) {
    const M_ = INTRA && INTRA[market], I0 = M_ && M_.series && M_.series[key]; el.innerHTML = '';
    const r = inUSD && M_ ? rateOn(M_.session) : 1, I = I0 && r ? I0.map(([t, v]) => [t, v / r]) : I0;
    if (!I) { el.innerHTML = `<p class="sub" style="padding:24px 0">No one-day data for ${esc(name)}: ${/^(sp500|dow|brent|gold_usd|dxy)$/.test(key) ? 'not saved for the last session.' : 'not saved for the last session.'}</p>`; return null; }
    const vals = I.map((x) => x[1]), lo = Math.min(...vals), hi = Math.max(...vals), pad = (hi - lo) * 0.15 || lo * 0.002;
    Charts.line(el, { ...dayAxis(I.map((x) => x[0]), el.clientWidth, !!M_.window), series: [{ name, values: vals }], format: fmt, endLabel: true, height: el.clientHeight, min: lo - pad });
    const ch = (vals.at(-1) / vals[0] - 1) * 100;
    if (M_.window) {   // round-the-clock markets: the last 24 hours, Cairo time
      const to = new Date(M_.to.replace(' ', 'T'));
      return `Last 24 hours to ${to.toLocaleDateString('en-US', { weekday: 'short', day: 'numeric', month: 'short' }).replace('Sept', 'Sep')} ${M_.to.slice(11)} Cairo time: <span class="num ${cls(ch)}">${pct(ch, 2)}</span>`;
    }
    const via = M_.proxy && M_.proxy[key] ? ` · traced by the ${esc(M_.proxy[key])} fund, which tracks it` : '';
    return `${day(M_.session).toLocaleDateString('en-US', { weekday: 'long', day: 'numeric', month: 'short' }).replace('Sept', 'Sep')}, ${I[0][0]}–${I.at(-1)[0]} ${market === 'egx' ? 'Cairo' : 'New York'} time${inUSD ? ', in dollars at the day\'s rate' : ''}: <span class="num ${cls(ch)}">${pct(ch, 2)}</span> from the first trade${via}`;
  }
  // x-axis labels on round, evenly spaced points: each day for a week, one weekday for a month, each month
  // for six months, every other month for a year, the hour through a session, every six hours for 24 hours.
  // Months are three letters (Sep, not Sept); the year shows where it changes. Narrow charts label every other one.
  const MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], WD = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  function axis(dates, back, width) {
    const ds = dates.map((iso) => new Date(iso + 'T12:00:00')), n = ds.length;
    const labels = ds.map((d) => `${MON[d.getMonth()]} ${d.getDate()}`);
    let at = [], text = labels.slice();
    if (back <= 7) { at = [...Array(n).keys()]; text = ds.map((d) => `${WD[d.getDay()]} ${d.getDate()}`); }
    else if (back <= 31) {   // weekly, counting back from the latest point; a week with no session that day takes its last one before
      for (let k = 0; ; k++) {
        const target = ds[n - 1] - k * 7 * 864e5; if (target < ds[0] - 3 * 864e5) break;
        let i = -1; ds.forEach((d, j) => { if (d <= target && d > target - 7 * 864e5) i = j; });
        if (i >= 0 && !at.includes(i)) at.unshift(i);
      }
    }
    else {
      // monthly to a year; every six months (January and July) for three years; each January for five
      const step = back <= 200 ? 1 : back <= 400 ? 2 : back <= 1100 ? 6 : 12, mo = (d) => d.getFullYear() * 12 + d.getMonth(), last = mo(ds[n - 1]);
      ds.forEach((d, i) => { if ((i === 0 && d.getDate() > 7) || (i > 0 && mo(ds[i - 1]) === mo(d))) return; if (step >= 6 ? d.getMonth() % step === 0 : (last - mo(d)) % step === 0) at.push(i); });
      const spans = ds[0].getFullYear() !== ds[n - 1].getFullYear();
      at.forEach((i, j) => { const d = ds[i], prev = j ? ds[at[j - 1]] : null; text[i] = step === 12 ? String(d.getFullYear()) : MON[d.getMonth()] + ((prev ? prev.getFullYear() !== d.getFullYear() : spans) ? ' ' + d.getFullYear() : ''); });
    }
    if (width < 520 && at.length > 4) at = at.filter((_, j) => (at.length - 1 - j) % 2 === 0);
    return { labels, xAt: at, xText: text };
  }
  // the same for prices through the day ('10:05'): on the hour, or every six hours across 24 hours
  function dayAxis(times, width, round = false) {
    const every = round ? 6 : width < 520 ? 2 : 1, seen = new Set(), at = [];
    times.forEach((t, i) => { const [h, m] = t.split(':').map(Number); if (m < 5 && h % every === 0 && !seen.has(h)) { seen.add(h); at.push(i); } });
    return { labels: times, xAt: at, xText: times.map((t) => t.slice(0, 2) + ':00') };
  }
  // a line chart of one series over a period (at least a month), with the biggest day marked when it stands out
  function chart(el, s, back, name, fmt, opts = {}) {
    const pts = s.filter(([d]) => d >= cut(lastDate(s), Math.max(back, 7))); el.innerHTML = '';
    if (pts.length < 2) { el.textContent = 'Not enough closes logged yet.'; return; }
    const vals = pts.map((x) => x[1]), lo = Math.min(...vals), hi = Math.max(...vals), pad = (hi - lo) * 0.15 || lo * 0.01;
    // a week has no shaded move (the change beside the price says it); short series get a dot on each close.
    // opts.rolls ([{session, to}]) marks a futures contract switch, and then no move is shaded (it could be the step)
    const rolls = (opts.rolls || []).map((r) => ({ r, at: pts.findIndex(([d]) => d >= r.session) })).filter((x) => x.at > 0);
    const ann = rolls.length ? rolls.map(({ r, at }) => ({ at, label: `Switched to the ${r.to} contract`, short: 'Contract switch' }))
      : opts.mark !== false && back > 7 ? bigMove(pts, opts.markAt || 0.025) : [];
    Charts.line(el, { ...axis(pts.map((x) => x[0]), Math.max(back, 7), el.clientWidth), series: [{ name, values: vals, muted: !!opts.muted }], format: fmt, annotations: ann, endLabel: true, marks: pts.length <= 12, height: el.clientHeight, min: lo - pad });
    return rolls.map(({ r }) => r);
  }
  // the desk's stocks over a period; notes ({ticker: {why, source, url}}, from deskNotes) add a line under each on 1D
  function movers(el, tickers, back, n = 3, notes = null) {
    // only stocks with a close for their market's last session, so a missed day never shows an older move
    const rows = tickers.filter((t) => { const s = stock(t); return s.length && s[s.length - 1][0] === asOfFor(GROUP.egx.includes(t) ? 'egx' : 'us'); })
      .map((t) => ({ t, c: change(stock(t), back), v: last(stock(t)) })).filter((r) => r.c != null).sort((a, b) => b.c - a.c);
    const why = (t) => { const w = notes && notes[t]; return w ? `<p class="mvwhy">${esc(w.why)}${w.url ? ` <a href="${esc(w.url)}" target="_blank" rel="noopener">${esc(w.source || 'Source')} →</a>` : ''}</p>` : ''; };
    const row = (r) => `<div class="mv"><a href="/desk/stock/?t=${encodeURIComponent(r.t)}"><b>${esc(NAMES[r.t])}</b><span class="t">${esc(r.t)}</span></a><span class="num">${num(r.v)}</span><span class="num ${cls(r.c)}">${pct(r.c)}</span></div>` + why(r.t);
    el.innerHTML = `<div class="movers"><div><h3><span class="chg up" aria-hidden="true"></span>Biggest gainers</h3>${rows.slice(0, n).map(row).join('')}</div><div><h3><span class="chg down" aria-hidden="true"></span>Biggest losers</h3>${rows.slice(-n).reverse().map(row).join('')}</div></div>`;
  }
  // why each of the desk's stocks moved on its last session: the whole-market list's reason when it was a market-wide
  // mover, else its latest checked story from the daily stock research (desk/stocks.json) within three days
  function deskNotes(S, market) {
    const out = {}, X = MOVERS && MOVERS[market], since = cut(asOfFor(market), 3);
    for (const t of GROUP[market]) {
      const n = (((S || {})[t] || {}).news || []).find((x) => x.date && x.date >= since && x.text);
      if (n) out[t] = { why: n.text, source: n.source, url: n.url };
    }
    if (X) for (const r of (X.gainers || []).concat(X.losers || [])) if (r.why && GROUP[market].includes(r.t)) out[r.t] = r;
    return out;
  }
  const intraOf = (t) => { const m = GROUP.egx.includes(t) ? 'egx' : 'us'; return INTRA && INTRA[m] && INTRA[m].series[t]; };
  // the trend column's heading: on 1D, the session its lines show when one is saved for that market
  function trendHead(back, market, label) {
    if (back > 7) return label;
    if (back === 7) { const n = weekSessions(market).length; return n >= 2 ? `Last ${n} sessions` : 'Last 7 days'; }
    const I = INTRA && INTRA[market];
    return !back && I && I.session ? `${WD[day(I.session).getDay()]}, ${MON[day(I.session).getMonth()]} ${day(I.session).getDate()} session` : 'Last 7 days';
  }
  // the whole market's biggest gainers and losers of the last session (desk/movers.json); a stock on the
  // desk links to its page
  // the whole market's biggest movers: the last session, or the past week or month (span 'week' or 'month', from
  // TradingView, with a reason carried over when one was written for the stock in the last 31 days)
  function marketMovers(el, market, n = 5, span = '') {
    const X0 = MOVERS && MOVERS[market], X = span ? X0 && X0[span] : X0;
    if (!X) { el.innerHTML = `<p class="sub">Not saved yet; the morning run saves ${span ? `the past ${span}'s movers` : 'the last session\'s movers once it has closed'}.</p>`; return ''; }
    if (span) {
      const notes = Object.assign({}, X0.why_log || {}); for (const r of (X0.gainers || []).concat(X0.losers || [])) if (r.why) notes[r.t] = r;
      for (const r of X.gainers.concat(X.losers)) if (!r.why && notes[r.t]) Object.assign(r, { why: notes[r.t].why, url: notes[r.t].url, source: notes[r.t].source });
    }
    const row = (r) => { const own = NAMES[r.t], nm = `<b>${esc(own || r.name)}</b><span class="t">${esc(r.t)}</span>`;
      return `<div class="mv">${own ? `<a href="/desk/stock/?t=${encodeURIComponent(r.t)}">${nm}</a>` : `<span style="min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">${nm}</span>`}<span class="num">${num(r.price)}</span><span class="num ${cls(r.pct)}">${pct(r.pct)}</span></div>`
        + (r.why ? `<p class="mvwhy">${esc(r.why)}${r.url ? ` <a href="${esc(r.url)}" target="_blank" rel="noopener">${esc(r.source || 'Source')} →</a>` : ''}</p>` : ''); };
    el.innerHTML = `<div class="movers"><div><h3><span class="chg up" aria-hidden="true"></span>Biggest gainers</h3>${X.gainers.slice(0, n).map(row).join('')}</div><div><h3><span class="chg down" aria-hidden="true"></span>Biggest losers</h3>${X.losers.slice(0, n).map(row).join('') || '<p class="sub">No stock fell.</p>'}</div></div>`;
    if (span) return `${X.basis}. ${X.note}.`;
    const d = day(X.session);
    return `${X.basis}, ${WD[d.getDay()]}, ${MON[d.getMonth()]} ${d.getDate()}.`;
  }
  // the change beside a chart's big number follows the chosen period, labelled ('in a month'); 1D is the day
  const SPAN = { 0: 'on the day', 7: 'in a week', 30: 'in a month', 182: 'in 6 months', 365: 'in a year', 1095: 'in 3 years', 1826: 'in 5 years' };
  function heroChg(s, p) {
    const back = p ? p[1] : 0, c = change(s, back);
    return `<span class="${cls(c)}">${pct(c, 2)}</span> <span class="span-l">${SPAN[back] || ''}</span>`;
  }
  // sort: { key: 'chg' | 'ytd' | null, dir: -1 (highest first) | 1 } from sortable(); without a key, the order given
  function stockTable(body, tickers, back, inUSD = false, sort = null) {
    const rows = tickers.map((t) => { const s = inUSD ? usd(stock(t)) : stock(t); return { t, s, c: change(s, back), y: ytd(s) }; });
    if (sort && sort.key) { const v = (r) => (sort.key === 'chg' ? r.c : r.y); rows.sort((a, b) => (v(a) == null) - (v(b) == null) || sort.dir * (v(a) - v(b))); }
    body.innerHTML = rows.map(({ t, s, c, y }) => `<tr class="click" onclick="location='/desk/stock/?t=${encodeURIComponent(t)}'"><td class="name"><a href="/desk/stock/?t=${encodeURIComponent(t)}"><b>${esc(NAMES[t])}</b><span>${esc(t)}</span></a></td><td class="trend">${spark(s, back, intraOf(t), back === 7 ? weekOf(t, inUSD) : null)}</td><td class="num">${num(last(s))}</td><td class="num"><span class="${cls(c)}">${pct(c)}</span></td><td class="num"><span class="${cls(y)}">${pct(y)}</span></td></tr>`).join('');
  }
  // each broad sector's move: the equal-weighted average of the desk's stocks in it over the period, as bars either
  // side of zero (the table's period and currency), with the best and worst stock named
  function sectorMoves(el, market, back, inUSD = false, label = '') {
    const rows = SECTORS[market].map(([name, ts]) => {
      const cs = ts.map((t) => { const s = inUSD ? usd(stock(t)) : stock(t); return { t, c: s.length && lastDate(s) >= cut(asOfFor(market), 7) ? change(s, back) : null }; }).filter((x) => x.c != null);
      return { name, n: cs.length, avg: cs.length ? cs.reduce((a, x) => a + x.c, 0) / cs.length : null, cs: cs.sort((a, b) => b.c - a.c) };
    }).filter((r) => r.avg != null).sort((a, b) => b.avg - a.avg);
    const max = Math.max(...rows.map((r) => Math.abs(r.avg)), 0.1);
    el.innerHTML = '<div class="secmoves">' + rows.map((r) => `<div class="flow"><div class="flow-top"><span>${esc(r.name)}</span><span class="num ${cls(r.avg)}">${pct(r.avg)}</span></div>`
      + `<div class="flow-bar"><i class="${r.avg >= 0 ? 'pos' : 'neg'}" style="width:${(Math.abs(r.avg) / max * 50).toFixed(1)}%"></i></div>`
      + `<div class="secd">${r.n > 1 ? `${r.n} stocks · best ${esc(r.cs[0].t)} <span class="${cls(r.cs[0].c)}">${pct(r.cs[0].c)}</span> · worst ${esc(r.cs.at(-1).t)} <span class="${cls(r.cs.at(-1).c)}">${pct(r.cs.at(-1).c)}</span>` : esc(r.cs[0].t) + ' only'}</div></div>`).join('') + '</div>'
      + `<p class="stock-note">Equal-weighted average of the desk's stocks in each sector${label ? ', ' + esc(label) : ''}${inUSD ? ', in dollars' : ''}.</p>`;
  }
  // coming up for the desk's stocks: results dates and dividends from desk/calendar.json (TradingView), and the dates
  // the desk confirmed itself (each stock's "next" in desk/stocks.json); the next 30 days first
  function calendar(el, market, CAL, ST) {
    const MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], cur = market === 'egx' ? 'EGP ' : '$';
    const when = (iso) => day(iso).toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' });
    const items = ((CAL && CAL.items) || []).filter((x) => x.market === market && GROUP[market].includes(x.t)).map((x) => ({ date: x.date, t: x.t,
      what: x.kind === 'results' ? `Results${x.period ? ` for the quarter to ${MON[+x.period.slice(5, 7) - 1]} ${x.period.slice(0, 4)}` : ''}${x.time ? ', ' + x.time : ''}` : `Goes ex-dividend: ${cur}${num(x.amount, x.amount < 10 ? 2 : 0)} a share${x.pay ? `, paid ${when(x.pay)}` : ''}`,
      tag: x.kind === 'results' ? (x.expected ? 'Expected' : '') : 'Dividend' }));
    // the desk's own dates: kept unless they repeat a results date already listed
    for (const t of GROUP[market]) for (const n of ((ST || {})[t] || {}).next || []) {
      if (/results/i.test(n.event) && items.some((x) => x.t === t && /^Results/.test(x.what))) continue;
      items.push({ date: n.date || null, t, what: n.event, note: n.when, tag: 'Desk' });
    }
    const today = new Date().toISOString().slice(0, 10);
    const dated = items.filter((x) => x.date && x.date >= today).sort((a, b) => (a.date < b.date ? -1 : a.date > b.date ? 1 : a.t < b.t ? -1 : 1));
    const later = items.filter((x) => !x.date);
    const rows = [...dated, ...later];
    if (!rows.length) { el.innerHTML = '<p class="sub">Nothing scheduled in the next few weeks.</p>'; return; }
    const SHOW = 8;
    el.innerHTML = '<div class="cal">' + rows.map((x, i) => `<div class="cal-r"${i >= SHOW ? ' hidden' : ''}><span class="cal-d">${x.date ? when(x.date) : esc(x.note || 'Date to come')}</span>`
      + `<a href="/desk/stock/?t=${encodeURIComponent(x.t)}"><b>${esc(NAMES[x.t])}</b> <span class="t">${esc(x.t)}</span></a><span class="cal-w">${esc(x.what)}</span>${x.tag ? `<span class="pill open">${esc(x.tag)}</span>` : '<span></span>'}</div>`).join('') + '</div>'
      + (rows.length > SHOW ? `<button type="button" class="more-btn">Show all ${rows.length} dates</button>` : '')
      + `<p class="stock-note">Results dates are TradingView's, often its estimate until the company announces one ("Expected"); "Desk" marks dates the desk confirmed.</p>`;
    const b = el.querySelector('.more-btn');
    if (b) b.addEventListener('click', () => { el.querySelectorAll('.cal-r[hidden]').forEach((r) => { r.hidden = false; }); b.remove(); });
  }
  // the stock tables' Change and YTD headers sort the rows: one tap puts the highest first, a second the lowest, a third
  // goes back to market value. A sorted table shows every row, so "best" is the best of all the desk's stocks.
  function sortable(table, redraw) {
    const ths = [...table.querySelectorAll('thead th')], state = { key: null, dir: -1 };
    for (const [i, key] of [[3, 'chg'], [4, 'ytd']]) {
      const th = ths[i];
      th.innerHTML = `<button type="button" class="sorth" title="Sort by this column"><span class="lab">${esc(th.textContent)}</span><i aria-hidden="true"></i></button>`;
      th.querySelector('button').addEventListener('click', () => {
        if (state.key !== key) { state.key = key; state.dir = -1; } else if (state.dir === -1) state.dir = 1; else state.key = null;
        ths.forEach((x) => { x.removeAttribute('aria-sort'); x.classList.remove('asc', 'desc'); });
        if (state.key) { th.setAttribute('aria-sort', state.dir < 0 ? 'descending' : 'ascending'); th.classList.add(state.dir < 0 ? 'desc' : 'asc'); }
        const tb = table.querySelector('tbody'), more = table.nextElementSibling;
        if (tb.dataset.clip) {
          tb.classList.toggle('clip', !state.key);
          if (more && more.classList.contains('more-btn')) { more.hidden = !!state.key; more.textContent = more.dataset.label; }
        }
        redraw();
      });
    }
    return state;
  }
  // a header's text, kept inside its sort button when it has one
  const headText = (el, t) => { const l = el.querySelector('.lab'); (l || el).textContent = t; };
  // a long table shows its first eight rows; the button under it shows the rest (the rows can be redrawn freely)
  function clipRows(tbody, total, noun) {
    if (total <= 8 || tbody.dataset.clip) return;
    tbody.dataset.clip = '1'; tbody.classList.add('clip');
    const b = document.createElement('button'); b.type = 'button'; b.className = 'more-btn'; b.textContent = b.dataset.label = `Show all ${total} ${noun}`;
    b.addEventListener('click', () => { const on = tbody.classList.toggle('clip'); b.textContent = on ? b.dataset.label : 'Show fewer'; });
    tbody.closest('table').after(b);
  }
  // tickers by market value, largest first (those without one last)
  const byCap = (tickers, S) => { const v = (t) => (((S || {})[t] || {}).cap || {}).value ?? -1; return [...tickers].sort((a, b) => v(b) - v(a)); };
  const kv = (rows) => '<div class="kv">' + rows.map(([k, v]) => `<span class="k">${esc(k)}</span><span class="v num">${v}</span>`).join('') + '</div>';
  const rangeBar = (lo, hi, v, f = (x) => num(x)) => lo == null ? '' : `<div class="range"><i style="left:calc(${((v - lo) / (hi - lo || 1) * 100).toFixed(1)}% - 1px)"></i></div><div class="range-l"><span>52-week low ${f(lo)}</span><span>high ${f(hi)}</span></div>`;

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

  // the day's news for a page: its impact (bullish, bearish or mixed, for the market the page covers), the headline, a
  // line or two, what it affects (tags from desk/tags.js: sectors, stocks and markets, each with its direction) and the
  // outlet's link. Older days carry desk tickers instead of tags; they show as chips.
  const IMPACT = { bullish: ['up', 'Bullish'], bearish: ['down', 'Bearish'], mixed: ['flat', 'Mixed'] };
  const impact = (n) => { const x = IMPACT[n.impact]; return x ? `<span class="impact ${x[0]}"><span class="chg ${x[0]}" aria-hidden="true"></span>${x[1]}</span>` : ''; };
  function news(el, items) {
    const list = items || [], SHOW = 3;
    const chips = (n) => (n.tickers || []).filter((t) => NAMES[t]).map((t) => `<a class="chip" href="/desk/stock/?t=${encodeURIComponent(t)}">${esc(t)}</a>`).join('');
    const tags = (n) => (Array.isArray(n.affects) && n.affects.length ? `<div class="naff"><span class="tags-h">Affects</span>${Tags.html(n.affects, { names: NAMES, max: 4 })}</div>` : '');
    el.innerHTML = list.map((n, i) => `<div class="news"${i >= SHOW ? ' hidden' : ''}>${impact(n)}<b class="nh">${esc(n.headline)}</b><p>${esc(n.text)}</p>${tags(n)}
      <div class="nf">${n.url ? `<a class="src" href="${esc(n.url)}" target="_blank" rel="noopener">${esc(n.source)} →</a>` : `<span class="src">${esc(n.source || '')}</span>`}${Array.isArray(n.affects) && n.affects.length ? '' : chips(n)}</div></div>`).join('')
      + (list.length > SHOW ? `<button type="button" class="more-btn">Show all ${list.length} stories</button>` : '')
      || '<p class="sub">No market news today.</p>';
    const b = el.querySelector('.more-btn');
    if (b) b.addEventListener('click', () => { el.querySelectorAll('.news[hidden]').forEach((x) => { x.hidden = false; }); b.remove(); });
  }

  async function init(page) {
    const icon = (d) => `<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke-width="1.5"><path d="${d}"/></svg>`;
    // the sidebar sits under its market's heading, so its labels drop the market (the phone's page row keeps them)
    const SHORT = { '/desk/egypt/': 'Dashboard', '/desk/stocks/egypt/': 'Stocks', '/desk/usa/': 'Dashboard', '/desk/stocks/us/': 'Stocks' };
    const links = PAGES.map(([h, n, d]) => `<a href="${h}"${h === page ? ' aria-current="page"' : ''}>${icon(d)}${SHORT[h] || n}</a>`);
    const shell = document.createElement('div');
    shell.className = 'app';
    shell.innerHTML = `<aside class="side" aria-label="Markets Desk">
      <div class="brand"><span class="mark" aria-hidden="true"><svg width="18" height="18" viewBox="0 0 18 18"><path d="M2 14l4-4 3 2.5L16 5" fill="none" stroke="#0e1216" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span><b>Markets Desk</b></span></div>
      <nav class="nav" aria-label="Main"><div class="navgroup">Egypt</div>${links.slice(0, 4).join('')}<div class="navgroup">USA</div>${links.slice(4, 7).join('')}<div class="navgroup">Global and record</div>${links[7]}${links[8]}
      <div class="navgroup">Newsletter</div><a href="/">${icon('M3 2.5h10v11H3zM5.5 5.5h5M5.5 8h5M5.5 10.5h3')}Today's newsletter</a></nav>
      <div class="side-foot"><button type="button" class="theme"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M8 2a6 6 0 100 12A4.5 4.5 0 018 2z"/></svg><span>Dark mode</span></button>Cairo · prices in EGP unless marked</div></aside>
      <div><header class="topbar"><div class="brand"><span class="mark" aria-hidden="true"><svg width="18" height="18" viewBox="0 0 18 18"><path d="M2 14l4-4 3 2.5L16 5" fill="none" stroke="#0e1216" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span><b>Markets Desk</b></span></div><a class="btn" href="/">Newsletter</a></header>
      <nav class="pagenav" aria-label="Pages">${PAGES.map(([h, n]) => `<a href="${h}"${h === page ? ' aria-current="page"' : ''}>${n}</a>`).join('')}</nav></div>`;
    const main = document.querySelector('main.canvas');
    shell.lastElementChild.appendChild(main);
    document.body.prepend(shell);
    theme();
    const idx = await get('/desk/index.json');
    const latest = idx && idx.desks && idx.desks.length ? idx.desks.map((d) => d.date).sort().at(-1) : null;
    DESK = latest ? await get('/desk/days/' + latest + '.json') : null;
    if (!DESK) { main.innerHTML = '<p class="finding">No desk has been published yet.</p>'; return null; }
    ASOF = DESK.asOf; CUTOFF = new Date(day(DESK.date) - 864e5).toISOString().slice(0, 10);
    INTRA = await get('/desk/intraday.json');
    MOVERS = await get('/desk/movers.json');
    const log = await get('/data/markets-recent.json');
    days = (log && log.days) || [];
    ASOF_M = { egx: ASOF, us: lastDate(series((e) => e.sp500, 'us')), fx: lastDate(series((e) => e.usd_egp, 'fx')) };
    // a session saved after its market's last logged close (a re-run later in the day) would not match the figures
    if (INTRA) for (const m of ['egx', 'us']) if (INTRA[m] && INTRA[m].session > asOfFor(m)) delete INTRA[m];
    if (DESK.sample) document.querySelectorAll('[data-sample]').forEach((e) => { e.hidden = false; });
    return DESK;
  }
  const dateLine = (iso) => day(iso).toLocaleDateString('en-US', { weekday: 'long', day: 'numeric', month: 'long' });
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
  return { get ASOF() { return ASOF; }, SECTORS, sortable, headText, sectorMoves, calendar, asOfFor, lastDate, $, esc, pct, cls, num, get, dateLine, conf, drivers, day, cut, short, PERIODS, NAMES, GROUP, series, valueAt, last, change, ytd, range52, stock, segment, spark, chart, movers, stockTable, kv, rangeBar, outlook, news, dayChart, axis, dayAxis, LONG, full, usd, toggle, trendHead, marketMovers, heroChg, startPeriod, clipRows, byCap, weekChart, deskNotes, weekOf, get INTRA() { return INTRA; }, get MOVERS() { return MOVERS; }, init };
})();
