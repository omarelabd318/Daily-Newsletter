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
    ['/desk/views/', 'Views', 'M3 3.5h10M3 8h10M3 12.5h6M12 11l1.5 1.5L16 10'],
    ['/desk/week/', 'The week', 'M3 3.5h10v10H3zM3 6.5h10M6 2v3M10 2v3'],
    ['/desk/runs/', 'Runs', 'M8 2.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11zM8 5v3l2 1.5']];

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
    if (more) more.addEventListener('click', () => {
      const open = more.getAttribute('aria-expanded') !== 'true';
      bs.forEach((b, i) => { b.hidden = !open && long(list[i]) && b.getAttribute('aria-pressed') !== 'true'; });
      more.setAttribute('aria-expanded', open); more.textContent = open ? 'Fewer' : 'More';
      more.setAttribute('aria-label', open ? 'Fewer periods' : 'More periods');
    });
  }
  // a trend line: the period's closes, or on 1D the last session through the day when it is saved (intra)
  // week: on 1W, the last sessions through the day (weekOf), and on 1M the month's (monthOf), when saved; otherwise closes
  function spark(s, back, intra = null, week = null) {
    const pts = !back && intra && intra.length > 1 ? intra.map((x) => x[1]) : (back === 7 || back === 30) && week && week.length > 1 ? week
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
  // a week (1W, every 15 minutes) or a month (1M, every 30 minutes) through each session, from desk/intraday.json's
  // "week" and "month"; null (the caller draws daily closes) until the stored sessions cover the whole period
  // the saved sessions behind a 1W or 1M line for one or more keys, or null while they do not cover the period: a
  // period must run to the market's latest session, and a month must reach back to its start with no session missing
  function intraPeriod(market, keys, back, inUSD = false) {
    const W = INTRA && INTRA[back > 7 ? 'month' : 'week'] && INTRA[back > 7 ? 'month' : 'week'][market];
    const all = (W || []).filter((x) => x.session <= asOfFor(market) && (back <= 7 || x.session > cut(asOfFor(market), back)));
    const ss = all.filter((x) => [].concat(keys).every((k) => x.series[k] && x.series[k].length > 1) && (!inUSD || rateOn(x.session)));
    if (ss.length < 2 || ss.at(-1) !== all.at(-1)) return null;
    if (back > 7 && (ss.length < all.length || ss.length < 15 || ss[0].session > cut(asOfFor(market), back - 5))) return null;
    return ss;
  }
  // a table's trend line over a month: the saved sessions, hourly (enough for a line 72 pixels wide)
  function monthOf(t, inUSD = false) {
    const m = GROUP.egx.includes(t) || /^EGX/.test(t) ? 'egx' : 'us', ss = intraPeriod(m, t, 30, inUSD);
    return ss && ss.flatMap((x) => { const r = inUSD ? rateOn(x.session) : 1, pts = x.series[t];
      return pts.filter(([tm], i) => tm.endsWith(':00') || i === pts.length - 1).map(([, v]) => v / r); });
  }
  function weekChart(el, market, key, name, fmt, inUSD = false, back = 7) {
    const ss = intraPeriod(market, key, back, inUSD);
    if (!ss) return null;
    const labels = [], vals = [], text = [], at = [];
    let wk = null;
    ss.forEach((x) => { const d = day(x.session), r = inUSD ? rateOn(x.session) : 1;
      const dl = back > 7 ? `${MON[d.getMonth()]} ${d.getDate()}` : `${WD[d.getDay()]} ${d.getDate()}`;
      // a week's labels: every session; a month's: the first session of each week
      const w = Math.floor((d - day('2026-01-04')) / 6048e5);
      if (back <= 7 || w !== wk) at.push(labels.length); wk = w;
      x.series[key].forEach(([t, v]) => { labels.push(`${dl} ${t}`); vals.push(v / r); text.push(dl); }); });
    el.innerHTML = '';
    // a month's first week, when it has only a session or two, would print its date on top of the next week's
    if (back > 7 && at.length > 2 && at[1] - at[0] < (at[2] - at[1]) / 2) at.shift();
    const lo = Math.min(...vals), hi = Math.max(...vals), pad = (hi - lo) * 0.15 || lo * 0.002;
    Charts.line(el, { labels, xAt: el.clientWidth < 520 && at.length > 3 ? at.filter((_, j) => (at.length - 1 - j) % 2 === 0) : at, xText: text,
      series: [{ name, values: vals }], format: fmt, endLabel: true, height: el.clientHeight, min: lo - pad });
    const ch = (vals.at(-1) / vals[0] - 1) * 100;
    return `Last ${ss.length} sessions through the day${inUSD ? ', in dollars at each day\'s rate' : ''}: <span class="num ${cls(ch)}">${pct(ch, 2)}</span> from the first trade`;
  }
  // a day's line spans at least 2% of its level, so a quiet session reads as quiet instead of filling the chart
  function dayRange(vals) {
    const lo = Math.min(...vals), hi = Math.max(...vals), mid = (lo + hi) / 2, half = Math.max((hi - lo) * 0.6, mid * 0.01);
    return [mid - half, mid + half];
  }
  function dayChart(el, market, key, name, fmt, inUSD = false, prev = null) {
    const M_ = INTRA && INTRA[market]; el.innerHTML = '';
    // the session's 5-minute line, or else the same session's 15-minute line from the week, where only that was saved
    const wk = !M_ || M_.window ? null : ((INTRA.week || {})[market] || []).find((x) => x.session === M_.session);
    const I0 = (M_ && M_.series && M_.series[key]) || (wk && wk.series[key] && wk.series[key].length > 1 ? wk.series[key] : null);
    const r = inUSD && M_ ? rateOn(M_.session) : 1, I = I0 && r ? I0.map(([t, v]) => [t, v / r]) : I0;
    if (!I) { el.innerHTML = `<p class="sub" style="padding:24px 0">No one-day data for ${esc(name)}: ${/^(sp500|dow|brent|gold_usd|dxy)$/.test(key) ? 'not saved for the last session.' : 'not saved for the last session.'}</p>`; return null; }
    // a dotted line at the previous session's close, so a day that opened lower and climbed still reads as down
    const ref = prev != null && !M_.window ? [{ value: prev, label: 'Prev. close ' + fmt(prev) }] : null;
    const vals = I.map((x) => x[1]), [ymin, ymax] = dayRange(ref ? vals.concat(prev) : vals);
    Charts.line(el, { ...dayAxis(I.map((x) => x[0]), el.clientWidth, !!M_.window), series: [{ name, values: vals }], format: fmt, endLabel: true, height: el.clientHeight, min: ymin, max: ymax, reference: ref });
    const ch = (vals.at(-1) / vals[0] - 1) * 100;
    if (M_.window) {   // round-the-clock markets: the last 24 hours, Cairo time
      const to = new Date(M_.to.replace(' ', 'T'));
      return `Last 24 hours to ${to.toLocaleDateString('en-US', { weekday: 'short', day: 'numeric', month: 'short' }).replace('Sept', 'Sep')} ${M_.to.slice(11)} Cairo time: <span class="num ${cls(ch)}">${pct(ch, 2)}</span>`;
    }
    const via = M_.proxy && M_.proxy[key] ? ` · traced by the ${esc(M_.proxy[key])} fund, which tracks it` : '';
    // one change in the caption: the caller adds the day's change from the previous close
    return `${day(M_.session).toLocaleDateString('en-US', { weekday: 'long', day: 'numeric', month: 'short' }).replace('Sept', 'Sep')}, ${I[0][0]}–${I.at(-1)[0]} ${market === 'egx' ? 'Cairo' : 'New York'} time${inUSD ? ', in dollars at the day\'s rate' : ''}${via}`;
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
    const why = (t) => { const w = notes && notes[t]; return w && !/^no company news found/i.test(String(w.why || '').trim()) ? `<p class="mvwhy">${esc(w.why)}${w.url ? ` <a href="${esc(w.url)}" target="_blank" rel="noopener">${esc(w.source || 'Source')} →</a>` : ''}</p>` : ''; };
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
        + (r.why && !/^no company news found/i.test(String(r.why).trim()) ? `<p class="mvwhy">${esc(r.why)}${r.url ? ` <a href="${esc(r.url)}" target="_blank" rel="noopener">${esc(r.source || 'Source')} →</a>` : ''}</p>` : ''); };
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
  // the EGX and Wall Street tables. group (a market: 'egx' or 'us') lists the stocks under the desk's broad sectors,
  // each headed by the equal-weighted average of its stocks' change and YTD, best sector first (or by the sorted column)
  function stockTable(body, tickers, back, inUSD = false, sort = null, group = null) {
    const rows = tickers.map((t) => { const s = inUSD ? usd(stock(t)) : stock(t); return { t, s, c: change(s, back), y: ytd(s) }; });
    const v = (r) => (sort && sort.key === 'ytd' ? r.y : r.c);
    if (sort && sort.key) rows.sort((a, b) => (v(a) == null) - (v(b) == null) || sort.dir * (v(a) - v(b)));
    const row = ({ t, s, c, y }) => `<tr class="click" onclick="location='/desk/stock/?t=${encodeURIComponent(t)}'"><td class="name"><a href="/desk/stock/?t=${encodeURIComponent(t)}"><b>${esc(NAMES[t])}</b><span>${esc(t)}</span></a></td><td class="trend">${spark(s, back, intraOf(t), back === 7 ? weekOf(t, inUSD) : back === 30 ? monthOf(t, inUSD) : null)}</td><td class="num">${num(last(s))}</td><td class="num"><span class="${cls(c)}">${pct(c)}</span></td><td class="num"><span class="${cls(y)}">${pct(y)}</span></td></tr>`;
    body.dataset.grouped = group ? '1' : '';
    if (!group) { body.innerHTML = rows.map(row).join(''); return; }
    const avg = (rs, k) => { const xs = rs.map((r) => r[k]).filter((x) => x != null); return xs.length ? xs.reduce((a, x) => a + x, 0) / xs.length : null; };
    const groups = SECTORS[group].map(([name, ts]) => ({ name, rs: rows.filter((r) => ts.includes(r.t)) }));
    const left = rows.filter((r) => !SECTORS[group].some(([, ts]) => ts.includes(r.t)));
    if (left.length) groups.push({ name: 'Other', rs: left });
    groups.forEach((g) => { g.c = avg(g.rs, 'c'); g.y = avg(g.rs, 'y'); });
    const gv = (g) => (sort && sort.key === 'ytd' ? g.y : g.c), dir = sort && sort.key ? sort.dir : -1;
    const shown = groups.filter((g) => g.rs.length).sort((a, b) => (gv(a) == null) - (gv(b) == null) || dir * (gv(a) - gv(b)));
    body.innerHTML = shown.map((g) => `<tr class="sec-row"><th scope="rowgroup">${esc(g.name)}<span>${g.rs.length > 1 ? `${g.rs.length} stocks, average` : '1 stock'}</span></th><td class="trend"></td><td></td>`
      + `<td class="num"><span class="${cls(g.c)}">${pct(g.c)}</span></td><td class="num"><span class="${cls(g.y)}">${pct(g.y)}</span></td></tr>` + g.rs.map(row).join('')).join('');
  }
  // a clipped table shows every row while it is sorted or grouped by sector, and its first eight again after
  function showAllRows(tbody) {
    if (!tbody.dataset.clip) return;
    const all = !!tbody.dataset.grouped || !!tbody.dataset.sorted, more = tbody.closest('table').nextElementSibling;
    if (tbody.dataset.allRows === String(all)) return;   // unchanged: a table opened with "Show all" stays open
    tbody.dataset.allRows = String(all);
    tbody.classList.toggle('clip', !all);
    if (more && more.classList.contains('more-btn')) { more.hidden = all; more.textContent = more.dataset.label; }
  }
  // coming up for the desk's stocks: results dates and dividends from desk/calendar.json (TradingView; for the US,
  // declared dividends and splits from Polygon), and the dates
  // the desk confirmed itself (each stock's "next" in desk/stocks.json); the next 30 days first
  function calendar(el, market, CAL, ST) {
    const MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], cur = market === 'egx' ? 'EGP ' : '$';
    const when = (iso) => day(iso).toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' });
    const items = ((CAL && CAL.items) || []).filter((x) => x.market === market && GROUP[market].includes(x.t)).map((x) => ({ date: x.date, t: x.t,
      what: x.kind === 'results' ? `Results${x.period ? ` for the quarter to ${MON[+x.period.slice(5, 7) - 1]} ${x.period.slice(0, 4)}` : ''}${x.time ? ', ' + x.time : ''}`
        : x.kind === 'split' ? `Stock split, ${x.ratio}: the share price divides by ${num(x.factor, x.factor % 1 ? 2 : 0)}, nothing else changes`
        : `Goes ex-dividend: ${cur}${num(x.amount, x.amount < 10 ? 2 : 0)} a share${x.pay ? `, paid ${when(x.pay)}` : ''}${x.declared ? ` (declared ${when(x.declared)})` : ''}`,
      tag: x.kind === 'results' ? (x.expected ? 'Expected' : '') : x.kind === 'split' ? 'Split' : 'Dividend' }));
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
    if (b) moreToggle(b, [...el.querySelectorAll('.cal-r')].slice(SHOW), `Show all ${rows.length} dates`);
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
        const tb = table.querySelector('tbody');
        tb.dataset.sorted = state.key ? '1' : '';
        redraw(); showAllRows(tb);
      });
    }
    return state;
  }
  // a header's text, kept inside its sort button when it has one
  const headText = (el, t) => { const l = el.querySelector('.lab'); (l || el).textContent = t; };
  // a "Show all" button that opens the hidden items and, pressed again, folds them back ("Show fewer"), keeping itself on screen
  function moreToggle(b, items, label) {
    b.addEventListener('click', () => {
      const open = b.getAttribute('aria-expanded') !== 'true';
      items.forEach((x) => { x.hidden = !open; });
      b.setAttribute('aria-expanded', open); b.textContent = open ? 'Show fewer' : label;
      if (!open) b.scrollIntoView({ block: 'nearest' });
    });
  }
  // a long table shows its first eight rows; the button under it shows the rest (the rows can be redrawn freely)
  function clipRows(tbody, total, noun) {
    if (total <= 8 || tbody.dataset.clip) return;
    tbody.dataset.clip = '1'; tbody.classList.add('clip');
    const b = document.createElement('button'); b.type = 'button'; b.className = 'more-btn'; b.textContent = b.dataset.label = `Show all ${total} ${noun}`;
    b.addEventListener('click', () => { const on = tbody.classList.toggle('clip'); b.textContent = on ? b.dataset.label : 'Show fewer'; if (on) b.scrollIntoView({ block: 'nearest' }); });
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
    el.classList.add('news-g');
    const chips = (n) => (n.tickers || []).filter((t) => NAMES[t]).map((t) => `<a class="chip" href="/desk/stock/?t=${encodeURIComponent(t)}">${esc(t)}</a>`).join('');
    const tags = (n) => (Array.isArray(n.affects) && n.affects.length ? `<div class="naff"><span class="tags-h">Affects</span>${Tags.html(n.affects, { names: NAMES, max: 4 })}</div>` : '');
    el.innerHTML = list.map((n, i) => `<div class="news"${i >= SHOW ? ' hidden' : ''}>${impact(n)}<b class="nh">${esc(n.headline)}</b><p>${esc(n.text)}</p>${tags(n)}
      <div class="nf">${n.url ? `<a class="src" href="${esc(n.url)}" target="_blank" rel="noopener">${esc(n.source)} →</a>` : `<span class="src">${esc(n.source || '')}</span>`}${Array.isArray(n.affects) && n.affects.length ? '' : chips(n)}</div></div>`).join('')
      + (list.length > SHOW ? `<button type="button" class="more-btn">Show all ${list.length} stories</button>` : '')
      || '<p class="sub">No market news today.</p>';
    const b = el.querySelector('.more-btn');
    if (b) moreToggle(b, [...el.querySelectorAll('.news')].slice(SHOW), `Show all ${list.length} stories`);
  }

  // the Find a stock box (desk/search.js, shared with the dashboards), loaded once
  const withSearch = (cb) => { if (window.DeskSearch) return cb(window.DeskSearch); const sc = document.createElement('script'); sc.src = '/desk/search.js'; sc.onload = () => cb(window.DeskSearch); document.head.appendChild(sc); };
  // the shared masthead and menu (desk/nav.js), loaded once
  const withNav = () => new Promise((ok) => { if (window.DeskNav) return ok(window.DeskNav); const sc = document.createElement('script'); sc.src = '/desk/nav.js'; sc.onload = () => ok(window.DeskNav); document.head.appendChild(sc); });
  async function init(page) {
    const shell = document.createElement('div');
    shell.className = 'app';
    const main = document.querySelector('main.canvas');
    shell.appendChild(main);
    document.body.prepend(shell);
    (await withNav()).mount(page, NAMES, GROUP);
    const idx = await get('/desk/index.json');
    const latest = idx && idx.desks && idx.desks.length ? idx.desks.map((d) => d.date).sort().at(-1) : null;
    DESK = latest ? await get('/desk/days/' + latest + '.json') : null;
    if (!DESK) { main.innerHTML = '<p class="finding">No desk has been published yet.</p>'; return null; }
    { const lb = document.getElementById('dm-label'); if (lb) { lb.dataset.base = lb.dataset.base || lb.textContent; lb.textContent = `${day(DESK.date).toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric' })}`; } }
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
  // a finding's first sentence in bold: the day's point, then the detail
  const lede = (t) => { const m = String(t || '').match(/^(.+?[.!?])\s+(?=[A-Z"“])/); return m ? `<b>${esc(m[1])}</b> ${esc(t.slice(m[0].length))}` : `<b>${esc(t)}</b>`; };
  const dateLine = (iso) => day(iso).toLocaleDateString('en-US', { weekday: 'long', day: 'numeric', month: 'long' });
  const conf = (c) => `<span class="conf ${c === 'high' ? 'high' : ''}">${esc(c[0].toUpperCase() + c.slice(1))}</span>`;
  // a view's confidence now: the latest update that changed it (desk/views.json updates[].confidence), else the opening level
  const confNow = (v) => { const c = (v.updates || []).filter((x) => x.confidence).sort((a, b) => (a.date < b.date ? -1 : a.date > b.date ? 1 : 0)); return c.length ? c[c.length - 1].confidence : v.confidence; };
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
  return { get ASOF() { return ASOF; }, SECTORS, lede, sortable, headText, showAllRows, calendar, asOfFor, lastDate, $, esc, pct, cls, num, get, dateLine, conf, confNow, drivers, day, cut, short, PERIODS, NAMES, GROUP, series, valueAt, last, change, ytd, range52, stock, segment, spark, chart, movers, stockTable, kv, rangeBar, outlook, news, dayChart, axis, dayAxis, LONG, full, usd, toggle, trendHead, marketMovers, heroChg, startPeriod, clipRows, byCap, weekChart, deskNotes, weekOf, monthOf, intraPeriod, get INTRA() { return INTRA; }, get MOVERS() { return MOVERS; }, init };
})();
