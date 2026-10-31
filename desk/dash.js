// The two dashboards, /desk/egypt/ and /desk/usa/: one script, the section named by the page's <body data-section>.
(async function(){
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const MINUS = '−';
  const pct = (v, d = 1) => v == null ? '—' : (v > 0 ? '+' : v < 0 ? MINUS : '') + Math.abs(v).toFixed(d) + '%';
  const cls = (v) => v == null ? 'dash' : v > 0 ? 'chg up' : v < 0 ? 'chg down' : 'chg flat';
  const get = (u) => fetch(u, { cache: 'no-cache' }).then((r) => r.ok ? r.json() : null).catch(() => null);

  // today's desk: the newest entry in desk/index.json
  const idx = await get('/desk/index.json');
  const latest = idx && idx.desks && idx.desks.length ? idx.desks.slice().sort((a, b) => b.date < a.date ? -1 : 1)[0].date : null;
  const D = latest ? await get('/desk/days/' + latest + '.json') : null;
  if (!D) { $('finding').textContent = 'No desk has been published yet.'; return; }
  const ASOF = D.asOf;
  const day = (iso) => new Date(iso + 'T12:00:00');
  const cut = (iso, back) => new Date(day(iso) - back * 864e5).toISOString().slice(0, 10);
  const short = (iso) => day(iso).toLocaleDateString('en-GB', { day: 'numeric', month: 'short' }).replace('Sept', 'Sep');

  const SECTIONS = {
    egypt: { name: 'Egypt', chart: 'egx30', chartName: 'EGX30', market: 'egx', group: 'egx' },
    global: { name: 'USA', chart: 'nasdaq', chartName: 'Nasdaq', market: 'us', group: 'us' },
  };
  const longDate = day(D.date).toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long' });
  $('stamp').innerHTML = 'Closes to ' + esc(day(ASOF).toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'short' }).replace('Sept', 'Sep').replace(',', '')) + '<br>Fetched ' + esc(D.fetched || '');

  // the data log: each entry holds the closes its edition showed, so a close belongs to the day before the entry
  const INTRA = await get('/desk/intraday.json'), MOVERS = await get('/desk/movers.json');
  // a session saved after the desk's closes (a re-run later in the day) would not match its figures: leave it out
  if (INTRA) for (const m of ['egx', 'us']) if (INTRA[m] && INTRA[m].session > ASOF) delete INTRA[m];
  const log = await get('/data/markets-recent.json');
  let days = (log && log.days) || [];
  function series(pick, market) {
    const out = [];
    for (const e of days) {
      const v = pick(e); if (typeof v !== 'number') continue;
      const d = new Date(day(e.date) - 864e5), wd = d.getDay(), iso = d.toISOString().slice(0, 10);
      if (iso > ASOF) continue;
      if (market === 'egx' && (wd === 5 || wd === 6)) continue;   // the EGX trades Sunday to Thursday
      if (market === 'us' && (wd === 6 || wd === 0)) continue;
      if (out.length && out[out.length - 1][0] === iso) continue;
      out.push([iso, v]);
    }
    return out;
  }
  const valueAt = (s, iso) => { let v = null; for (const [d, x] of s) { if (d <= iso) v = x; else break; } return v; };
  const change = (s, back) => {
    if (s.length < 2) return null;
    const last = s[s.length - 1][1], base = back ? valueAt(s, cut(ASOF, back)) : s[s.length - 2][1];
    return base ? (last / base - 1) * 100 : null;
  };
  const ytd = (s) => { const b = valueAt(s, (ASOF.slice(0, 4) - 1) + '-12-31'); return b && s.length ? (s[s.length - 1][1] / b - 1) * 100 : null; };
  const LONG = [['3Y', 1095, 'Last 3 years'], ['5Y', 1826, 'Last 5 years']]; let fullLoaded = false;
  const PERIODS = [['1D', 0, 'Last 7 days'], ['1W', 7, 'Last 7 days'], ['1M', 30, 'Last 30 days'], ['6M', 182, 'Last 6 months'], ['1Y', 365, 'Last 12 months']];
  // every visit opens on the defaults; clear the choices an earlier version of the desk remembered
  try { Object.keys(localStorage).filter((k) => k.startsWith('desk:')).forEach((k) => localStorage.removeItem(k)); } catch (e) {}
  const segment = (el, start, onPick, list = PERIODS) => {
    el.innerHTML = list.map((p) => `<button type="button" aria-pressed="${p[0] === start}">${p[0]}</button>`).join('');
    el.querySelectorAll('button').forEach((b, i) => b.addEventListener('click', () => {
      el.querySelectorAll('button').forEach((x) => x.setAttribute('aria-pressed', x === b)); onPick(list[i]);
    }));
  };
  const NAMES = { COMI: 'Commercial International Bank', TMGH: 'Talaat Moustafa', ETEL: 'Telecom Egypt', PHDC: 'Palm Hills', SWDY: 'Elsewedy Electric', ORAS: 'Orascom Construction', FWRY: 'Fawry', ABUK: 'Abu Qir Fertilizers', HRHO: 'EFG Holding', CLHO: 'Cleopatra Hospital', JUFO: 'Juhayna', ALCN: 'Alexandria Containers', MFPC: 'MOPCO', EAST: 'Eastern Company', EFIH: 'e-finance', EMFD: 'Emaar Misr', BQDC: 'Banque du Caire', EGAL: 'Egypt Aluminium',
    AAPL: 'Apple', MSFT: 'Microsoft', NVDA: 'Nvidia', AMZN: 'Amazon', GOOGL: 'Alphabet', META: 'Meta', TSLA: 'Tesla', JPM: 'JPMorgan Chase', XOM: 'Exxon Mobil', AVGO: 'Broadcom', 'BRK.B': 'Berkshire Hathaway', WMT: 'Walmart', V: 'Visa', ORCL: 'Oracle', COST: 'Costco' };
  const GROUP = { egx: ['COMI', 'TMGH', 'ETEL', 'PHDC', 'SWDY', 'ORAS', 'FWRY', 'ABUK', 'HRHO', 'CLHO', 'JUFO', 'ALCN', 'MFPC', 'EAST', 'EFIH', 'EMFD', 'BQDC', 'EGAL'], us: ['AAPL', 'MSFT', 'NVDA', 'AMZN', 'GOOGL', 'META', 'TSLA', 'JPM', 'XOM', 'AVGO', 'BRK.B', 'WMT', 'V', 'ORCL', 'COST'] };
  const STOCK = {}; for (const g in GROUP) for (const t of GROUP[g]) STOCK[t] = series((e) => (e[g] || {})[t], g);
  const callRows = (rows) => rows.map((c) => `<div class="call-row"><b>${esc(c.name)}</b><span class="conf">${esc(c.confidence[0].toUpperCase() + c.confidence.slice(1))}</span><span class="why">${esc(c.why)}</span></div>`).join('');
  const PILL = { 'open': 'open', 'on track': 'ok', 'right': 'ok', 'wrong': 'bad', 'closed': 'open' };
  // a trend line: the period's closes, or on 1D the last session through the day when it is saved (intra)
  function spark(s, back, intra = null) {
    const pts = !back && intra && intra.length > 1 ? intra.map((x) => x[1]) : (back <= 7 ? s.slice(-7) : s.filter(([d]) => d >= cut(ASOF, back))).map((x) => x[1]);
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
    const d = (i) => new Date(pts[i][0] + 'T12:00:00'), dd = (i) => d(i).toLocaleDateString('en-GB', { day: 'numeric' });
    const mon = (i) => d(i).toLocaleDateString('en-GB', { day: 'numeric', month: 'short' }).replace('Sept', 'Sep');
    if (best.b - best.a === 1) return [{ at: best.b, label: `${mon(best.b)} ${p(best.m)}`, short: p(best.m) }];
    const first = best.a + 1, same = d(first).getMonth() === d(best.b).getMonth();
    return [{ from: best.a, to: best.b, label: `${same ? dd(first) : mon(first)}–${mon(best.b)} ${p(best.m)}`, short: p(best.m) }];
  }

  // x-axis labels on round, evenly spaced points: each day for a week, one weekday for a month, each month
  // for six months, every other month for a year, the hour through a session, every six hours for 24 hours.
  // Months are three letters (Sep, not Sept); the year shows where it changes. Narrow charts label every other one.
  const MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], WD = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  function axis(dates, back, width) {
    const ds = dates.map((iso) => new Date(iso + 'T12:00:00')), n = ds.length;
    const labels = ds.map((d) => `${d.getDate()} ${MON[d.getMonth()]}`);
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

  async function render(key) {
    const S = SECTIONS[key], X = D[key];
    document.querySelectorAll('[data-sec]').forEach((a) => { if (a.dataset.sec === key) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current'); });
    $('title').textContent = S.name + ' · ' + longDate;
    document.title = 'Markets Desk · ' + S.name + ' · ' + day(D.date).toLocaleDateString('en-GB', { day: 'numeric', month: 'short' }).replace('Sept', 'Sep');
    $('finding').innerHTML = esc(X.finding) + (X.next ? ' <span class="when">' + esc(X.next) + '</span>' : '');

    $('stk-more').textContent = key === 'egypt' ? 'EGX page →' : 'Wall Street page →'; $('stk-more').href = key === 'egypt' ? '/desk/egx/' : '/desk/us/';
    $('h-close').textContent = X.close.title || 'Close';
    $('close-rows').innerHTML = X.close.groups.map((g) => '<h3>' + esc(g.name) + '</h3>' + g.rows.map((r) =>
      `<div class="lrow${r.lead ? ' lead' : ''}"><span class="k">${esc(r.label)}</span><span class="v num${r.value == null ? ' dash' : ''}">${r.value == null ? '—' : esc(r.value)}</span><span class="d num ${cls(r.change)}">${r.change == null ? '—' : pct(r.change, 2)}</span></div>`).join('')).join('');
    $('close-note').textContent = X.close.note || '';

    // the day's stories: the top call first, then up to two more, one at a time; arrows, dots, keys or a swipe move between them
    const calls = (X.calls || [X.top]).filter(Boolean).slice(0, 3);
    let at = 0;
    const show = (i) => {
      at = (i + calls.length) % calls.length;
      const T = calls[at];
      $('story-n').textContent = calls.length > 1 ? (at ? `Story ${at + 1} of ${calls.length}` : `Top call · 1 of ${calls.length}`) : 'Top call';
      $('h-read').textContent = T.headline; $('top-body').textContent = T.body;
      $('top-view').textContent = T.view; $('top-moves').textContent = T.moves; $('top-wrong').textContent = T.wrong;
      $('top-conf').textContent = 'Confidence: ' + T.confidence;
      $('top-notice').hidden = !T.notice; $('top-notice').textContent = T.notice || '';
      $('story-dots').querySelectorAll('button').forEach((b, j) => b.setAttribute('aria-selected', j === at));
    };
    $('story-arrows').hidden = $('story-dots').hidden = calls.length < 2;
    $('story-dots').innerHTML = calls.map((c, j) => `<button type="button" role="tab" aria-label="${esc(c.headline)}"></button>`).join('');
    $('story-dots').querySelectorAll('button').forEach((b, j) => { b.onclick = () => show(j); });
    $('story-prev').onclick = () => show(at - 1); $('story-next').onclick = () => show(at + 1);
    show(0);

    $('board-h').textContent = X.board.horizon || '';
    $('helped').innerHTML = callRows(X.board.helped); $('hurt').innerHTML = callRows(X.board.hurt);
    $('week').innerHTML = X.week.map((w) => `<div class="wk"><span class="day">${esc(w.day)}</span><b>${esc(w.event)}</b><span class="imp${w.impact === 'high' ? ' high' : ''}">${esc(w.impact[0].toUpperCase() + w.impact.slice(1))}</span><span class="why">${esc(w.why)}</span></div>`).join('');
    $('views').innerHTML = X.views.map((v) => `<div class="view"><b>${esc(v.call)}</b><span class="pill ${PILL[v.status] || 'open'}">${esc(v.status[0].toUpperCase() + v.status.slice(1))}</span><span class="why">${esc(v.note)}</span></div>`).join('');

    // the section's index, in the one chart hue: the EGX30, or the S&P 500, Nasdaq and Dow in the Wall Street page's order
    const IDX = key === 'egypt' ? [{ k: 'egx30', n: 'EGX30', intra: 'EGX30' }]
      : [{ k: 'sp500', n: 'S&P 500', intra: 'sp500' }, { k: 'nasdaq', n: 'Nasdaq', intra: 'COMP' }, { k: 'dow', n: 'Dow Jones', intra: 'dow' }];
    let cur = IDX[0], per = PERIODS[2], idx = series((e) => e[cur.k], S.market);
    $('chart-more').textContent = key === 'egypt' ? 'EGX page →' : 'Wall Street page →'; $('chart-more').href = key === 'egypt' ? '/desk/egx/' : '/desk/us/';
    $('itabs').hidden = IDX.length < 2;
    $('itabs').innerHTML = IDX.length < 2 ? '' : IDX.map((x, i) => `<button type="button" aria-pressed="${!i}">${esc(x.n)}</button>`).join('');
    $('itabs').querySelectorAll('button').forEach((b, i) => b.addEventListener('click', () => {
      $('itabs').querySelectorAll('button').forEach((x) => x.setAttribute('aria-pressed', x === b)); cur = IDX[i]; idx = series((e) => e[cur.k], S.market); drawIdx(per);
    }));
    // the change beside the big number follows the chosen period; 1D is the day
    const SPAN = { 0: 'on the day', 7: 'in a week', 30: 'in a month', 182: 'in 6 months', 365: 'in a year', 1095: 'in 3 years', 1826: 'in 5 years' };
    async function drawIdx(p) {
      per = p; $('egx-chart').style.height = '';
      if (p[1] > 400 && !fullLoaded) {   // 3Y and 5Y need the full log, loaded once
        const f = await get('/data/markets.json'); fullLoaded = true;
        if (f && f.days) { days = f.days; idx = series((e) => e[cur.k], S.market); }
      }
      $('chart-name').textContent = IDX.length < 2 ? cur.n : 'Wall Street';
      const lv = idx.length ? idx[idx.length - 1][1] : null, hc = change(idx, p[1]);
      $('ilvl').textContent = lv == null ? '—' : lv.toLocaleString('en-GB', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
      $('ichg').innerHTML = `<span class="${cls(hc)}">${pct(hc, 2)}</span> <span class="span-l">${SPAN[p[1]] || ''}</span>`;
      if (!p[1]) {   // the last session through the day, from desk/intraday.json
        const el = $('egx-chart'), mk = S.market, I = INTRA && INTRA[mk] && INTRA[mk].series[cur.intra]; el.innerHTML = '';
        if (!I) { el.style.height = 'auto'; el.innerHTML = '<p class="chart-cap">The last session through the day is not saved yet; the morning run saves it once the session has closed.</p>'; $('egx-cap').textContent = ''; return; }
        const v = I.map((x) => x[1]), lo = Math.min(...v), hi = Math.max(...v);
        Charts.line(el, { ...dayAxis(I.map((x) => x[0]), el.clientWidth), series: [{ name: cur.n, values: v }], format: Charts.fmt.int, endLabel: true, height: el.clientHeight, min: lo - (hi - lo) * 0.15 });
        const ch = (v.at(-1) / v[0] - 1) * 100;
        $('egx-cap').innerHTML = `${day(INTRA[mk].session).toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'short' }).replace('Sept', 'Sep')}, ${I[0][0]}–${I.at(-1)[0]} ${mk === 'egx' ? 'Cairo' : 'New York'} time: <span class="num ${cls(ch)}">${pct(ch, 2)}</span> from the first trade${INTRA[mk].proxy && INTRA[mk].proxy[cur.intra] ? ` · traced by the ${esc(INTRA[mk].proxy[cur.intra])} fund, which tracks it` : ''}`;
        return;
      }
      const back = Math.max(p[1], 7), pts = idx.filter(([d]) => d >= cut(ASOF, back)), el = $('egx-chart'); el.innerHTML = '';
      if (pts.length < 2) { el.textContent = 'Not enough closes logged yet.'; $('egx-cap').textContent = ''; return; }
      const ann = bigMove(pts), vals = pts.map((x) => x[1]), lo = Math.min(...vals), hi = Math.max(...vals);
      Charts.line(el, { ...axis(pts.map((x) => x[0]), back, el.clientWidth), series: [{ name: cur.n, values: vals }], format: Charts.fmt.int, annotations: ann, endLabel: true, height: el.clientHeight, min: lo - (hi - lo) * 0.15 });
      const y = ytd(idx);
      $('egx-cap').innerHTML = `${esc(cur.n)}, ${p[2].toLowerCase()} · this year <span class="num ${cls(y)}">${pct(y)}</span>`;
    }
    // opens on 1D when the last session through the day is saved, otherwise on 1M
    const start = INTRA && INTRA[S.market] && INTRA[S.market].series[cur.intra] ? PERIODS[0] : PERIODS[2];
    segment($('egx-seg'), start[0], drawIdx, PERIODS.concat(LONG)); drawIdx(start);

    // the whole market's biggest movers of the last session, three each way, with the reason where one was found
    const MV = MOVERS && MOVERS[S.market];
    $('movers-more').textContent = key === 'egypt' ? 'EGX page →' : 'Wall Street page →'; $('movers-more').href = key === 'egypt' ? '/desk/egx/' : '/desk/us/';
    if (!MV) { $('movers').innerHTML = '<p class="chart-cap">Not saved yet; the morning run saves the last session\'s movers once it has closed.</p>'; $('movers-note').textContent = ''; }
    else {
      const f2 = (v) => v.toLocaleString('en-GB', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
      const row = (r) => { const own = NAMES[r.t], nm = `<b>${esc(own || r.name)}</b><span class="t">${esc(r.t)}</span>`;
        return `<div class="mv">${own ? `<a href="/desk/stock/?t=${encodeURIComponent(r.t)}">${nm}</a>` : `<span class="nm">${nm}</span>`}<span class="num">${f2(r.price)}</span><span class="num ${cls(r.pct)}">${pct(r.pct)}</span></div>`
          + (r.why ? `<p class="mvwhy">${esc(r.why)}${r.url ? ` <a href="${esc(r.url)}" target="_blank" rel="noopener">${esc(r.source || 'Source')} →</a>` : ''}</p>` : ''); };
      $('movers').innerHTML = `<div class="movers"><div><h3><span class="chg up" aria-hidden="true"></span>Biggest gainers</h3>${MV.gainers.slice(0, 3).map(row).join('')}</div><div><h3><span class="chg down" aria-hidden="true"></span>Biggest losers</h3>${MV.losers.slice(0, 3).map(row).join('') || '<p class="chart-cap">No stock fell.</p>'}</div></div>`;
      const sd = day(MV.session); $('movers-note').textContent = `${MV.basis}, ${WD[sd.getDay()]} ${sd.getDate()} ${MON[sd.getMonth()]}.`;
    }

    // side card: Egypt asks whether the pound's move is local; USA shows oil, the price that reaches Egypt most
    $('pvd-legend').innerHTML = ''; $('pvd').innerHTML = '';
    if (key === 'egypt') {
      $('h-pvd').textContent = 'Dollar in pounds'; $('side-meta').textContent = 'EGP page →'; $('side-meta').href = '/desk/egp/';
      const fx = series((e) => e.usd_egp, 'fx').filter(([d]) => d >= cut(ASOF, 30));
      if (fx.length < 2) { $('pvd-read').textContent = 'Not enough logged rates yet.'; }
      else {
        const pv = $('pvd'), vals = fx.map((x) => x[1]), lo = Math.min(...vals), hi = Math.max(...vals);
        Charts.line(pv, { ...axis(fx.map((x) => x[0]), 30, pv.clientWidth), series: [{ name: 'USD/EGP', values: vals }], format: Charts.fmt.dec(2), height: pv.clientHeight, min: lo - (hi - lo) * 0.15, endLabel: true });
        const ch = (vals[vals.length - 1] / vals[0] - 1) * 100, now = vals[vals.length - 1];
        const yr = series((e) => e.usd_egp, 'fx').filter(([d]) => d >= cut(ASOF, 365)).map((x) => x[1]), lo52 = Math.min(...yr), hi52 = Math.max(...yr);
        const where = now >= hi52 - (hi52 - lo52) * 0.05 ? 'near its 52-week high' : now <= lo52 + (hi52 - lo52) * 0.05 ? 'near its 52-week low'
          : `between its 52-week low of <span class="num">${lo52.toFixed(2)}</span> and high of <span class="num">${hi52.toFixed(2)}</span>`;
        $('pvd-read').innerHTML = `The dollar buys <span class="num">EGP ${now.toFixed(2)}</span>, <span class="num ${cls(ch)}">${pct(ch)}</span> over the month and ${where}. Whether the pound's move is local is on the EGP page.`;
      }
      // the pound's figures: inflation (a fall shows green), the real one-year yield and reserves
      const lg = (k) => series((e) => e[k], 'fx'), lastOf = (s) => (s.length ? s[s.length - 1][1] : null);
      const pts = (c) => `${c > 0 ? '+' : c < 0 ? MINUS : ''}${Math.abs(c).toFixed(1)} pts`, rows = [];
      const inf = lg('infl_headline'), iv = lastOf(inf), ip = ([...inf].reverse().find(([, x]) => x !== iv) || [])[1], tb = lastOf(lg('tbill_364'));
      if (iv != null) rows.push(['Inflation (annual)', iv.toFixed(1) + '%', ip != null ? `<span class="chg ${iv > ip ? 'up' : iv < ip ? 'down' : 'flat'} inv">${pts(iv - ip)}</span>` : '']);
      if (iv != null && tb != null) rows.push(['Real one-year yield', (tb - iv).toFixed(1) + ' pts', '']);
      const R = ((await get('/desk/reserves.json')) || {}).months || [], RL = R[R.length - 1], RP = R[R.length - 2];
      if (RL) { const rc = RP ? (RL.total / RP.total - 1) * 100 : null; rows.push(['Foreign reserves', '$' + RL.total.toFixed(2) + 'bn', rc == null ? '' : `<span class="${cls(rc)}">${pct(rc, 2)}</span>`]); }
      $('pvd-figs').hidden = !rows.length;
      $('pvd-figs').innerHTML = rows.map(([k, v, d]) => `<div class="lrow"><span class="k">${esc(k)}</span><span class="v num">${v}</span><span class="d num">${d}</span></div>`).join('');
    } else {
      $('pvd-figs').hidden = true;
      const br = series((e) => e.brent, 'us').filter(([d]) => d >= cut(ASOF, 30));
      $('h-pvd').textContent = 'Oil'; $('side-meta').textContent = 'Global page →'; $('side-meta').href = '/desk/global/';
      if (br.length < 2) { $('pvd-read').textContent = 'Not enough logged prices yet.'; }
      else {
        const pv = $('pvd'), vals = br.map((x) => x[1]);
        Charts.line(pv, { ...axis(br.map((x) => x[0]), 30, pv.clientWidth), series: [{ name: 'Brent', values: vals, muted: true }], format: Charts.fmt.dec(2), height: pv.clientHeight, min: Math.floor(Math.min(...vals) - 2), endLabel: true });
        const ch = (vals[vals.length - 1] / vals[0] - 1) * 100, lastDay = short(br[br.length - 1][0]);
        $('pvd-read').innerHTML = `Brent is <span class="num">${pct(ch)}</span> over the month, last logged at <span class="num">$${vals[vals.length - 1].toFixed(2)}</span> (${lastDay}). Oil feeds Egypt's import bill and fuel prices.`;
      }
    }

    // who bought and who sold (Egypt only): net flows by investor group, bought to the right of the centre line
    const F = X.flows;
    $('c-flows').hidden = !F;
    if (F) {
      const max = Math.max(...F.rows.map((r) => Math.abs(r.net))) || 1;
      $('h-flows').textContent = F.title || 'Who bought and who sold';
      $('flows-sub').textContent = F.sub || '';
      $('flows').innerHTML = F.rows.map((r) => `<div class="flow"><div class="flow-top"><span>${esc(r.who)}</span><span class="num">${r.net > 0 ? '+' : r.net < 0 ? MINUS : ''}${Math.abs(r.net).toFixed(2)}</span></div><div class="flow-bar"><i class="${r.net >= 0 ? 'buy' : 'sell'}" style="width:${(Math.abs(r.net) / max * 50).toFixed(1)}%"></i></div></div>`).join('')
        + '<div class="flow-axis"><span>Net sold</span><span>Net bought</span></div>';
      $('flows-read').textContent = F.read || '';
      $('flows-note').hidden = !!F.confirmed;
      $('flows-note').textContent = F.confirmed ? '' : 'Not yet confirmed: ' + (F.source || 'one source only') ;
    }

    // stocks for this section
    let period = PERIODS[0];
    function drawStocks() {
      const back = period[1];
      $('chg-h').textContent = `Change (${period[0]})`;
      const I1 = INTRA && INTRA[S.group];
      $('trend-h').textContent = back > 7 ? period[2] : !back && I1 && I1.session ? `${WD[day(I1.session).getDay()]} ${day(I1.session).getDate()} ${MON[day(I1.session).getMonth()]} session` : 'Last 7 days';
      $('stk-note').innerHTML = X.stocksNote || '';
      $('stk-body').innerHTML = GROUP[S.group].map((t) => {
        const s = STOCK[t], fresh = s.length && s[s.length - 1][0] === ASOF;
        const last = fresh ? s[s.length - 1][1] : null, c = fresh ? change(s, back) : null, y = fresh ? ytd(s) : null;
        return `<tr style="cursor:pointer" onclick="location='/desk/stock/?t=${encodeURIComponent(t)}'"><td class="name"><b>${NAMES[t]}</b><span>${t}</span></td><td class="trend">${fresh ? spark(s, back, INTRA && INTRA[S.group] && INTRA[S.group].series[t]) : ''}</td><td class="num${last == null ? ' dash' : ''}">${last == null ? '—' : last.toLocaleString('en-GB', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td><td class="num"><span class="${cls(c)}">${pct(c)}</span></td><td class="num"><span class="${cls(y)}">${pct(y)}</span></td></tr>`;
      }).join('');
    }
    segment($('stk-seg'), '1D', (p) => { period = p; drawStocks(); });
    drawStocks();
  }
  // each dashboard is its own page: /desk/egypt/ and /desk/usa/
  const pick = () => (document.body.dataset.section === 'usa' ? 'global' : 'egypt');
  // swipe and arrow keys for the stories, set once
  const story = $('story'); let x0 = null;
  story.addEventListener('touchstart', (e) => { x0 = e.touches[0].clientX; }, { passive: true });
  story.addEventListener('touchend', (e) => { if (x0 == null) return; const dx = e.changedTouches[0].clientX - x0; x0 = null; if (Math.abs(dx) > 50) $(dx < 0 ? 'story-next' : 'story-prev').click(); });
  story.addEventListener('keydown', (e) => { if (e.key === 'ArrowRight') $('story-next').click(); if (e.key === 'ArrowLeft') $('story-prev').click(); });
  render(pick());
})();

// theme, shared with the newsletter through localStorage
(function () {
  const tb = document.querySelector('.theme'), lab = tb.querySelector('span');
  const sync = () => { lab.textContent = document.documentElement.getAttribute('data-theme') === 'dark' ? 'Light mode' : 'Dark mode'; };
  sync();
  tb.addEventListener('click', () => {
    const dark = document.documentElement.getAttribute('data-theme') !== 'dark';
    if (dark) document.documentElement.setAttribute('data-theme', 'dark'); else document.documentElement.removeAttribute('data-theme');
    try { localStorage.setItem('theme', dark ? 'dark' : 'light'); } catch (e) {}
    location.reload();
  });
})();
