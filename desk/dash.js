// The two dashboards, /desk/egypt/ and /desk/usa/: one script, the section named by the page's <body data-section>.
(async function(){
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const MINUS = '−';
  // a change that rounds to zero shows as 0.0%, with no sign
  const pct = (v, d = 1) => { if (v == null) return '—'; const r = +v.toFixed(d); return (r > 0 ? '+' : r < 0 ? MINUS : '') + Math.abs(r).toFixed(d) + '%'; };
  const cls = (v) => v == null ? 'dash' : v >= 0.05 ? 'chg up' : v <= -0.05 ? 'chg down' : 'chg flat';
  // a finding's first sentence in bold (a sentence ends at . ! or ? before a space and a capital, never inside 54.31)
  const lede = (t) => { const m = String(t || '').match(/^(.+?[.!?])\s+(?=[A-Z"“])/); return m ? `<b>${esc(m[1])}</b> ${esc(t.slice(m[0].length))}` : `<b>${esc(t)}</b>`; };
  const get = (u) => fetch(u, { cache: 'no-cache' }).then((r) => r.ok ? r.json() : null).catch(() => null);

  // today's desk: the newest entry in desk/index.json
  const idx = await get('/desk/index.json');
  const latest = idx && idx.desks && idx.desks.length ? idx.desks.slice().sort((a, b) => b.date < a.date ? -1 : 1)[0].date : null;
  const D = latest ? await get('/desk/days/' + latest + '.json') : null;
  if (!D) { $('finding').textContent = 'No desk has been published yet.'; return; }
  // ASOF is the EGX's last session; each market has its own last close (ASOF_M: Wall Street's is Friday at weekends,
  // the EGX's Thursday). Every series runs up to the day before the desk's date (CUTOFF).
  const ASOF = D.asOf;
  const day = (iso) => new Date(iso + 'T12:00:00');
  const CUTOFF = new Date(day(D.date) - 864e5).toISOString().slice(0, 10);
  const cut = (iso, back) => new Date(day(iso) - back * 864e5).toISOString().slice(0, 10);
  const short = (iso) => day(iso).toLocaleDateString('en-US', { day: 'numeric', month: 'short' }).replace('Sept', 'Sep');

  const SECTIONS = {
    egypt: { name: 'Egypt', chart: 'egx30', chartName: 'EGX30', market: 'egx', group: 'egx' },
    global: { name: 'United States', chart: 'nasdaq', chartName: 'Nasdaq', market: 'us', group: 'us' },
  };
  const longDate = day(D.date).toLocaleDateString('en-US', { weekday: 'long', day: 'numeric', month: 'long' });

  // the data log: each entry holds the closes its edition showed, so a close belongs to the day before the entry
  const INTRA = await get('/desk/intraday.json'), MOVERS = await get('/desk/movers.json'), STOCKS = ((await get('/desk/stocks.json')) || {}).stocks || {};
  const log = await get('/data/markets-recent.json');
  let days = (log && log.days) || [];
  function series(pick, market) {
    const out = [];
    for (const e of days) {
      const v = pick(e); if (typeof v !== 'number') continue;
      const d = new Date(day(e.date) - 864e5), wd = d.getDay(), iso = d.toISOString().slice(0, 10);
      if (iso > CUTOFF) continue;
      if (market === 'egx' && (wd === 5 || wd === 6)) continue;   // the EGX trades Sunday to Thursday
      if (market === 'us' && (wd === 6 || wd === 0)) continue;
      if (out.length && out[out.length - 1][0] === iso) continue;
      out.push([iso, v]);
    }
    return out;
  }
  // a series' own last date: periods count back from it, so each market measures from its own last close
  const lastDate = (s) => (s.length ? s[s.length - 1][0] : ASOF);
  const valueAt = (s, iso) => { let v = null; for (const [d, x] of s) { if (d <= iso) v = x; else break; } return v; };
  const change = (s, back) => {
    if (s.length < 2) return null;
    const last = s[s.length - 1][1], base = back ? valueAt(s, cut(lastDate(s), back)) : s[s.length - 2][1];
    return base ? (last / base - 1) * 100 : null;
  };
  const ytd = (s) => { const b = valueAt(s, (lastDate(s).slice(0, 4) - 1) + '-12-31'); return b && s.length ? (s[s.length - 1][1] / b - 1) * 100 : null; };
  const ASOF_M = { egx: ASOF, us: lastDate(series((e) => e.sp500, 'us')) }, asOf = (m) => ASOF_M[m] || ASOF;
  // a session saved after its market's last logged close (a re-run later in the day) would not match the figures
  if (INTRA) for (const m of ['egx', 'us']) if (INTRA[m] && INTRA[m].session > asOf(m)) delete INTRA[m];
  const LONG = [['3Y', 1095, 'Last 3 years'], ['5Y', 1826, 'Last 5 years']]; let fullLoaded = false;
  const SPAN_OF = { 7: 'in a week', 30: 'in a month', 182: 'in 6 months', 365: 'in a year' };
  const PERIODS = [['1D', 0, 'Last 7 days'], ['1W', 7, 'Last 7 days'], ['1M', 30, 'Last 30 days'], ['6M', 182, 'Last 6 months'], ['1Y', 365, 'Last 12 months']];
  // every visit opens on the defaults; clear the choices an earlier version of the desk remembered
  try { Object.keys(localStorage).filter((k) => k.startsWith('desk:')).forEach((k) => localStorage.removeItem(k)); } catch (e) {}
  // a row of period buttons; 3Y and 5Y sit behind "More" unless one of them is the starting period
  const segment = (el, start, onPick, list = PERIODS) => {
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
  };
  const NAMES = { COMI: 'Commercial International Bank', TMGH: 'Talaat Moustafa', ETEL: 'Telecom Egypt', PHDC: 'Palm Hills', SWDY: 'Elsewedy Electric', ORAS: 'Orascom Construction', FWRY: 'Fawry', ABUK: 'Abu Qir Fertilizers', HRHO: 'EFG Holding', CLHO: 'Cleopatra Hospital', JUFO: 'Juhayna', ALCN: 'Alexandria Containers', MFPC: 'MOPCO', EAST: 'Eastern Company', EFIH: 'e-finance', EMFD: 'Emaar Misr', BQDC: 'Banque du Caire', EGAL: 'Egypt Aluminium', AMOC: 'Alexandria Mineral Oils', SKPC: 'Sidi Kerir Petrochemicals', EFID: 'Edita Food Industries',
    AAPL: 'Apple', MSFT: 'Microsoft', NVDA: 'Nvidia', AMZN: 'Amazon', GOOGL: 'Alphabet', META: 'Meta', TSLA: 'Tesla', JPM: 'JPMorgan Chase', XOM: 'Exxon Mobil', AVGO: 'Broadcom', 'BRK.B': 'Berkshire Hathaway', WMT: 'Walmart', V: 'Visa', ORCL: 'Oracle', COST: 'Costco', NFLX: 'Netflix', INTC: 'Intel', LLY: 'Eli Lilly' };
  const GROUP = { egx: ['COMI', 'TMGH', 'ETEL', 'PHDC', 'SWDY', 'ORAS', 'FWRY', 'ABUK', 'HRHO', 'CLHO', 'JUFO', 'ALCN', 'MFPC', 'EAST', 'EFIH', 'EMFD', 'BQDC', 'EGAL', 'AMOC', 'SKPC', 'EFID'], us: ['AAPL', 'MSFT', 'NVDA', 'AMZN', 'GOOGL', 'META', 'TSLA', 'JPM', 'XOM', 'AVGO', 'BRK.B', 'WMT', 'V', 'ORCL', 'COST', 'NFLX', 'INTC', 'LLY'] };
  // the shared masthead and menu (desk/nav.js, with its Find a stock box)
  { const sc = document.createElement('script'); sc.src = '/desk/nav.js'; sc.onload = () => { window.DeskNav.mount(location.pathname, NAMES, GROUP); if (window.__deskStamp && window.DeskNav.stamp(window.__deskStamp)) document.body.classList.add('stamp-up'); if (D) window.DeskNav.label(longDate); }; document.head.appendChild(sc); }
  const callRows = (rows) => rows.map((c) => `<div class="call-row"><b>${esc(c.name)}</b><span class="conf">${esc(c.confidence[0].toUpperCase() + c.confidence.slice(1))}</span><span class="why">${esc(c.why)}</span></div>`).join('');
  const PILL = { 'open': 'open', 'on track': 'ok', 'right': 'ok', 'wrong': 'bad', 'closed': 'open' };


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

  async function render(key) {
    const S = SECTIONS[key], X = D[key];
    document.querySelectorAll('[data-sec]').forEach((a) => { if (a.dataset.sec === key) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current'); });
    $('title').textContent = S.name;   // the date is in the masthead
    document.title = 'Markets Desk · ' + S.name + ' · ' + day(D.date).toLocaleDateString('en-US', { day: 'numeric', month: 'short' }).replace('Sept', 'Sep');
    $('stamp').innerHTML = 'Closes to ' + esc(day(asOf(S.market)).toLocaleDateString('en-US', { weekday: 'short', day: 'numeric', month: 'short' }).replace('Sept', 'Sep').replace(',', '')) + '<br>Fetched ' + esc(String(D.fetched || '').replace(/\b(\d{1,2}) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b/, '$2 $1'));
    // on a laptop the two lines sit on the right of the market's menu row, as one line; a phone keeps them under the title
    window.__deskStamp = $('stamp').innerText.replace(/\s*\n\s*/g, ' · ');
    if (window.DeskNav && window.DeskNav.stamp(window.__deskStamp)) document.body.classList.add('stamp-up');
    // the finding: its first sentence in bold, the day's point; the coming dates live in the Week ahead card
    $('finding').innerHTML = lede(X.finding);
    // the desk read aloud: an 8 to 9 minute summary in the Heart voice (desk_audio.py), one button under the finding
    get('/data/audio/desk-' + D.date + '.json').then((m) => {
      const v = m && m.voices && m.voices[0];
      if (!v || !v.url || document.getElementById('desk-listen')) return;
      const url = /^https?:/.test(v.url) ? v.url : '/' + v.url.replace(/^\//, '');
      const mins = Math.max(1, Math.round((v.duration || 0) / 60));
      const box = document.createElement('div'); box.className = 'd-listen'; box.id = 'desk-listen';
      box.innerHTML = '<button type="button" class="d-play" aria-label="Listen to the day\'s desk"><span class="d-ico">▶</span> Listen to the day</button>'
        + '<span class="d-len">' + mins + ' min · Heart</span><button type="button" class="d-rate" aria-label="Playback speed">1×</button>'
        + '<span class="d-bar" aria-hidden="true"><i></i></span>';
      $('finding').insertAdjacentElement('afterend', box);
      const au = new Audio(); au.preload = 'none';
      const play = box.querySelector('.d-play'), rate = box.querySelector('.d-rate'), bar = box.querySelector('.d-bar i'), len = box.querySelector('.d-len');
      const RATES = [1, 1.25, 1.5, 0.85];
      const fmt = (t) => Math.floor(t / 60) + ':' + ('0' + Math.floor(t % 60)).slice(-2);
      play.addEventListener('click', () => {
        if (!au.src) au.src = url;
        if (au.paused) au.play().catch(() => {}); else au.pause();
      });
      au.addEventListener('play', () => { play.innerHTML = '<span class="d-ico">❚❚</span> Pause'; box.classList.add('on'); });
      au.addEventListener('pause', () => { play.innerHTML = '<span class="d-ico">▶</span> ' + (au.currentTime > 1 && !au.ended ? 'Resume' : 'Listen to the day'); });
      au.addEventListener('timeupdate', () => { if (au.duration) { bar.style.width = (au.currentTime / au.duration * 100) + '%'; len.textContent = fmt(au.currentTime) + ' / ' + fmt(au.duration); } });
      au.addEventListener('ended', () => { bar.style.width = '0'; box.classList.remove('on'); len.textContent = mins + ' min · Heart'; });
      rate.addEventListener('click', () => { const r = RATES[(RATES.indexOf(au.playbackRate) + 1) % RATES.length]; au.playbackRate = r; rate.textContent = (r === 0.85 ? '0.85' : r) + '×'; });
      // a click on the bar jumps there
      box.querySelector('.d-bar').addEventListener('click', (e) => { if (!au.duration) return; const b = e.currentTarget.getBoundingClientRect(); au.currentTime = (e.clientX - b.left) / b.width * au.duration; });
    });

    $('h-close').textContent = X.close.title || 'Close';
    $('close-rows').innerHTML = X.close.groups.map((g) => `<div class="strip-g"><h3>${esc(g.name)}</h3><div class="strip-row">` + g.rows.map((r) =>
      `<div class="fig${r.lead ? ' lead' : ''}"><span class="k">${esc(r.label)}</span><span class="v num${r.value == null ? ' dash' : ''}">${r.value == null ? '—' : esc(r.value)}</span>`
      + `<span class="d num ${cls(r.change)}">${r.change == null ? '<span class="dash">—</span>' : pct(r.change, 2)}</span></div>`).join('') + '</div></div>').join('');
    $('close-note').textContent = X.close.note || '';
    // each figure leads to its chart: an index on this dashboard's own chart, the VIX to its chart below, the
    // pound's figures to the EGP page, world markets to the Global page; the yields have no chart and no link
    const GO = [[/^EGX30/, '/desk/egx/#today'], [/^EGX70/, '/desk/egx/?i=egx70'], [/^S&P 500/, '/desk/us/#today'], [/^Nasdaq/, '/desk/us/?i=nasdaq#today'], [/^Dow/, '/desk/us/?i=dow#today'], [/^VIX/, '#c-vix'],
      [/^USD\/EGP/, '/desk/egp/#c-usd'], [/^Gold 24K/, '/desk/egp/#c-gold'], [/^Inflation/, '/desk/egp/#c-infl'], [/^One-year T-bill/, '/desk/egp/?show=tbill#c-infl'],
      [/^Real one-year/, '/desk/egp/?show=real#c-infl'], [/^Foreign reserves/, '/desk/egp/#c-rsv'],
      [/^Brent/, '/desk/global/#g-brent'], [/^Gold, \$/, '/desk/global/#g-gold_usd'], [/^Dollar index/, '/desk/global/#g-dxy'], [/^Bitcoin/, '/desk/global/#g-btc']];
    const go = (to) => {
      if (to[0] === '/') { location.href = to; return; }
      const t = $(to[0] === '#' ? to.slice(1) : 'c-chart'); if (t) t.scrollIntoView({ behavior: 'smooth', block: 'start' });
      if (to[0] !== '#') { const b = [...$('itabs').querySelectorAll('button')].find((x) => x.textContent === to); if (b && b.getAttribute('aria-pressed') !== 'true') b.click(); }
    };
    const linkFigs = () => document.querySelectorAll('#close-rows .fig:not([data-go])').forEach((f) => {
      const k = (f.querySelector('.k') || {}).textContent || '', hit = GO.find(([re]) => re.test(k));
      f.dataset.go = hit && !(hit[1] === '#c-vix' && !$('c-vix')) && !(/^\/desk\/us\//.test(hit[1]) && key === 'egypt') ? hit[1] : '';
      if (!f.dataset.go) return;
      f.classList.add('go'); f.tabIndex = 0; f.setAttribute('role', 'link'); f.title = 'Open its chart';
      f.addEventListener('click', () => go(f.dataset.go)); f.addEventListener('keydown', (e) => { if (e.key === 'Enter') go(f.dataset.go); });
    });
    linkFigs(); new MutationObserver(linkFigs).observe($('close-rows'), { childList: true, subtree: true });
    // EGY: the pound's other figures as a row of the strip (inflation, the one-year T-bill, the real yield, reserves)
    if (key === 'egypt') {
      const lg = (k) => series((e) => e[k], 'fx'), lastOf = (x) => (x.length ? x[x.length - 1][1] : null);
      const pts = (c) => `${c > 0 ? '+' : c < 0 ? MINUS : ''}${Math.abs(c).toFixed(1)} pts`, figs = [];
      const fig = (k, v, d) => `<div class="fig"><span class="k">${k}</span><span class="v num">${v}</span><span class="d num">${d || ''}</span></div>`;
      const inf = lg('infl_headline'), iv = lastOf(inf), ip = ([...inf].reverse().find(([, x]) => x !== iv) || [])[1], tb = lastOf(lg('tbill_364'));
      if (iv != null) figs.push(fig('Inflation, annual', iv.toFixed(1) + '%', ip != null ? `<span class="chg ${iv > ip ? 'up' : iv < ip ? 'down' : 'flat'} inv">${pts(iv - ip)}</span>` : ''));
      if (tb != null) figs.push(fig('One-year T-bill', tb.toFixed(2) + '%'));
      if (iv != null && tb != null) figs.push(fig('Real one-year yield', (tb - iv).toFixed(1) + ' pts'));
      const R = ((await get('/desk/reserves.json')) || {}).months || [], RL = R[R.length - 1], RP = R[R.length - 2];
      if (RL) { const rc = RP ? (RL.total / RP.total - 1) * 100 : null; figs.push(fig('Foreign reserves', '$' + RL.total.toFixed(2) + 'bn', rc == null ? '' : `<span class="${cls(rc)}">${pct(rc, 2)}</span>`)); }
      if (figs.length) document.querySelector('#c-close .card-h .meta').textContent = 'Day change; the pound\'s on the month';
      if (figs.length) $('close-rows').insertAdjacentHTML('beforeend', `<div class="strip-g"><h3>The pound</h3><div class="strip-row">${figs.join('')}</div></div>`);
    }

    // USA: the VIX beside the indices and a row for the 2-, 10- and 30-year Treasury yields (desk/rates.json, from Cboe and the US
    // Treasury), at the desk's US session with their change on the day, between the indices and the global markets
    if (key === 'global') {
      const RT = ((await get('/desk/rates.json')) || {}).series || {}, at = asOf('us');
      const pair = (s) => { const i = (s || []).filter(([d]) => d <= at).length - 1; return i >= 0 ? [s[i][1], i ? s[i - 1][1] : null] : [null, null]; };
      const fig = (k, v, d) => `<div class="fig"><span class="k">${k}</span><span class="v num">${v}</span><span class="d num">${d}</span></div>`;
      const bp = (v, p) => { if (p == null) return '<span class="dash">—</span>'; const b = Math.round((v - p) * 100); return `<span class="${cls(b)}">${b > 0 ? '+' : b < 0 ? MINUS : ''}${Math.abs(b)} bp</span>`; };
      const out = [], [vx, vp] = pair(RT.vix);
      const row = [...document.querySelectorAll('#close-rows .strip-g')].find((g) => /^USA/.test(g.querySelector('h3').textContent));
      // the VIX sits in the USA row beside the indices; the yields get their own row
      if (vx != null && row) { const c = vp ? (vx / vp - 1) * 100 : null; row.querySelector('.strip-row').insertAdjacentHTML('beforeend', fig('VIX (volatility)', vx.toFixed(2), c == null ? '<span class="dash">—</span>' : `<span class="${cls(-c)}">${pct(c, 1)}</span>`)); }
      for (const [k, lab] of [['us2y', '2-year Treasury'], ['us10y', '10-year Treasury'], ['us30y', '30-year Treasury']]) { const [v, p] = pair(RT[k]); if (v != null) out.push(fig(lab, v.toFixed(2) + '%', bp(v, p))); }
      if (out.length && row) row.insertAdjacentHTML('afterend', `<div class="strip-g"><h3>Yields</h3><div class="strip-row">${out.join('')}</div></div>`);
      // the VIX over time, under winners and losers: daily closes from Cboe (desk/rates.json), with the long-run average
      const VX = (RT.vix || []).filter(([d]) => d <= at);
      if (VX.length > 20 && $('c-vix')) {
        $('c-vix').hidden = false;
        const drawVix = (p) => {
          const pts = VX.filter(([d]) => d >= cut(lastDate(VX), p[1])), el = $('vix-chart'), v = pts.map((x) => x[1]);
          Charts.line(el, { ...axis(pts.map((x) => x[0]), p[1], el.clientWidth), series: [{ name: 'VIX', values: v }], format: Charts.fmt.dec(2), endLabel: true, height: el.clientHeight,
            reference: [{ value: 20, label: 'Long-run average, about 20' }], min: Math.min(...v, 20) - 1 });
          const c = (v[v.length - 1] / v[0] - 1) * 100;   // shown red when it rises, as fear does
          $('vix-lvl').textContent = v[v.length - 1].toFixed(2);
          $('vix-chg').innerHTML = `<span class="${cls(-c)}">${pct(c, 1)}</span> <span class="span-l">${SPAN_OF[p[1]] || ''}</span>`;
          $('vix-cap').innerHTML = `${p[2]}: from <span class="num">${v[0].toFixed(2)}</span> to <span class="num">${v[v.length - 1].toFixed(2)}</span>. The VIX measures the swings in the S&P 500 that options traders expect over the next 30 days; above about 20, the market is nervous.`;
        };
        segment($('vix-seg'), '1M', drawVix, PERIODS.slice(2)); drawVix(PERIODS[2]);
      }
    }

    // the day's stories: the top call in full, then up to four more as compact cards ("Also today"), each tap-to-open.
    // "What it moves" is the story's tags (sector first, then the stocks most exposed and the markets it touches);
    // older days carry a sentence instead, shown as it is
    const calls = (X.calls || [X.top]).filter(Boolean).slice(0, 5);
    const moves = (T) => Array.isArray(T.affects) && T.affects.length ? Tags.html(T.affects, { names: NAMES }) : T.moves ? `<p class="moves-txt">${esc(T.moves)}</p>` : '';
    const T = calls[0];
    { const sec = ((T.affects || []).find((x) => x.kind === 'sector') || {}).name;
      $('story-n').textContent = ['Top call', sec, T.confidence ? 'Confidence ' + T.confidence : null].filter(Boolean).join(' · '); }
    $('h-read').textContent = T.headline;
    // the story's first sentence or two as its lead, in larger type; the rest under it (a sentence ends at . ! or ?
    // before a space and a capital, so 54.31 or 0.67% never splits it)
    { const sents = String(T.body || '').split(/(?<=[.!?])\s+(?=[A-Z"“(])/); let n = 1;
      if (sents.length > 2 && (sents[0] + ' ' + sents[1]).split(/\s+/).length <= 45) n = 2;
      $('top-lede').textContent = sents.slice(0, n).join(' '); $('top-body').textContent = sents.slice(n).join(' '); $('top-body').hidden = !$('top-body').textContent; }
    $('top-view').textContent = T.view; $('top-wrong').textContent = T.wrong;
    $('top-moves').innerHTML = moves(T); $('top-moves').parentElement.hidden = !$('top-moves').innerHTML;
    $('top-conf').textContent = ''; $('top-conf').hidden = true;
    $('top-notice').hidden = !T.notice; $('top-notice').textContent = T.notice || '';
    const rest = calls.slice(1);
    $('also').hidden = !rest.length;
    $('also-g').innerHTML = rest.map((c) => `<article class="also-i">
        <h3>${esc(c.headline)}</h3>
        <p>${esc(c.line || c.view)}</p>
        ${moves(c)}
        <details><summary>The story, the view and when it is wrong</summary>
          <p>${esc(c.body)}</p>${c.line ? `<p><b>The view</b> ${esc(c.view)}</p>` : ''}<p><b>Wrong if</b> ${esc(c.wrong)}</p>
          <p class="meta">Confidence: ${esc(c.confidence)}</p>${c.notice ? `<div class="notice">${esc(c.notice)}</div>` : ''}
        </details></article>`).join('');

    // from the whole day's news and moves, not only the top call; the horizon comes from the day's file
    $('board-h').textContent = `From the day's news and moves · ${(X.board.horizon || 'next 1–4 weeks').replace(/^.*·\s*/, '')}`;
    $('helped').innerHTML = callRows(X.board.helped); $('hurt').innerHTML = callRows(X.board.hurt);
    $('week').innerHTML = X.week.map((w) => `<div class="wk"><span class="day">${esc(w.day)}</span><b>${esc(w.event)}</b><span class="imp${w.impact === 'high' ? ' high' : ''}">${esc(w.impact[0].toUpperCase() + w.impact.slice(1))}</span><span class="why">${esc(w.why)}</span></div>`).join('');
    $('views').innerHTML = X.views.map((v) => `<div class="view"><b>${esc(v.call)}</b><span class="pill ${PILL[v.status] || 'open'}">${esc(v.status[0].toUpperCase() + v.status.slice(1))}</span><span class="why">${esc(v.note)}</span></div>`).join('');
    // on a phone, long lists show their first few items, with a button for the rest
    const fold = (el, sel, n, noun) => {
      if (!matchMedia('(max-width:860px)').matches) return;
      const items = [...el.querySelectorAll(sel)];
      if (items.length <= n) return;
      items.slice(n).forEach((x) => { x.hidden = true; });
      const b = document.createElement('button'); b.type = 'button'; b.className = 'more-btn'; b.textContent = `Show all ${items.length} ${noun}`;
      const label = b.textContent;
      b.addEventListener('click', () => {
        const open = b.getAttribute('aria-expanded') !== 'true';
        items.slice(n).forEach((x) => { x.hidden = !open; });
        b.setAttribute('aria-expanded', open); b.textContent = open ? 'Show fewer' : label;
        if (!open) b.scrollIntoView({ block: 'nearest' });
      });
      el.after(b);
    };
    fold($('week'), '.wk', 3, 'events'); fold($('views'), '.view', 2, 'views');
    // since yesterday: what the day changed for this market: views judged, opened or re-rated, the desk's stocks that
    // moved 5% or more or reached a 52-week high or low, and results or dividends dated today
    (async () => {
      const el = $('since'); if (!el) return;
      const VL = ((await get('/desk/views.json')) || {}).views || [], CAL = ((await get('/desk/calendar.json')) || {}).items || [];
      const mine = (v) => (key === 'egypt' ? ['egx', 'egp'] : ['us', 'global']).includes(v.market), out = [];
      const tag = (k, c) => `<span class="pill ${c}">${k}</span>`, vlink = (v) => `<a href="/desk/views/">${esc(v.title)}</a>`;
      for (const v of VL.filter(mine)) {
        if (v.result && v.result.date === D.date) out.push([0, `${tag(v.status === 'right' ? 'Right' : v.status === 'wrong' ? 'Wrong' : 'Closed', v.status === 'right' ? 'ok' : v.status === 'wrong' ? 'bad' : 'open')} ${vlink(v)}`]);
        if (v.opened === D.date) out.push([1, `${tag('New ' + v.kind, 'open')} ${vlink(v)}`]);
        let prev = v.confidence;
        (v.updates || []).slice().sort((a, b) => (a.date < b.date ? -1 : 1)).forEach((u) => {
          if (u.confidence && u.confidence !== prev && u.date === D.date) out.push([2, `${tag('Confidence ' + ({ low: 0, medium: 1, high: 2 }[u.confidence] > { low: 0, medium: 1, high: 2 }[prev] ? 'up' : 'down') + ' to ' + u.confidence, 'open')} ${vlink(v)}`]);
          if (u.confidence) prev = u.confidence;
        });
      }
      const at = asOf(S.group);
      for (const t of GROUP[S.group]) {
        const sr = series((e) => (e[S.group] || {})[t], S.group); if (!sr.length || sr[sr.length - 1][0] !== at) continue;
        const last = sr[sr.length - 1][1], d1 = change(sr, 0), yr = sr.filter(([d]) => d >= cut(at, 365) && d < at).map((x) => x[1]);
        const link = `<a href="/desk/stock/?t=${encodeURIComponent(t)}">${esc(NAMES[t] || t)}</a>`;
        if (d1 != null && Math.abs(d1) >= 5) out.push([3, `<span class="num ${cls(d1)}">${pct(d1)}</span> ${link}`]);
        if (yr.length > 200 && last > Math.max(...yr)) out.push([4, `${tag('52-week high', 'ok')} ${link}`]);
        if (yr.length > 200 && last < Math.min(...yr)) out.push([4, `${tag('52-week low', 'bad')} ${link}`]);
      }
      for (const t of GROUP[S.group]) { const R = (STOCKS[t] || {}).lastResults;
        if (R && R.date && R.date >= cut(D.date, 1)) out.push([6, `${tag('Results: ' + (({ beat: 'beat', miss: 'missed', 'in line': 'in line', mixed: 'mixed' })[R.verdict] || 'out'), R.verdict === 'beat' ? 'ok' : R.verdict === 'miss' ? 'bad' : 'open')} <a href="/desk/stock/?t=${encodeURIComponent(t)}">${esc(NAMES[t] || t)}</a><span class="meta"> · ${esc(R.headline)}</span>`]); }
      // today's dates, one line per kind: "Results expected · Edita Food Industries, Juhayna"
      const kinds = {};
      for (const c of CAL.filter((c) => c.market === S.group && c.date === D.date)) {
        const k = c.kind === 'results' ? (c.expected ? 'Results expected' : 'Results today') : c.kind === 'split' ? `Stock split ${c.ratio}` : 'Goes ex-dividend';
        (kinds[k] = kinds[k] || []).push(`<a href="/desk/stock/?t=${encodeURIComponent(c.t)}">${esc(NAMES[c.t] || c.t)}</a>${c.time ? `<span class="meta"> (${esc(c.time)})</span>` : ''}`);
      }
      for (const [k, list] of Object.entries(kinds)) out.push([5, `${tag(k, 'open')} <span>${list.join(', ')}</span>`]);
      // grouped by kind, one labelled row each, so unrelated items never share a line
      const GROUPS = [['Views', [0, 1, 2]], ['Results', [6]], ['Big moves', [3]], ['52-week highs and lows', [4]], ['Today', [5]]];
      const rowsOf = (ks) => out.filter((x) => ks.includes(x[0]));
      el.innerHTML = out.length ? GROUPS.map(([g, ks]) => { const r = rowsOf(ks); if (!r.length) return '';
        const inline = ks[0] === 3 || ks[0] === 4;
        return `<div class="since-g"><h3>${g}</h3><div class="since-i${inline ? ' inline' : ''}">${r.map(([, h]) => `<div class="since-row">${h}</div>`).join('')}</div></div>`; }).join('')
        : `<p class="sub">A quiet day for the record: no view judged, opened or re-rated, and none of the desk's stocks moved 5% or more.</p>`;
      // a day with changes: Since yesterday moves up beside the chart; a quiet day leaves it in the right column and
      // the chart at full width, so there is never a near-empty block beside it
      if (out.length && !document.querySelector('.toprow')) {
        const ch = $('c-chart'), si = $('c-since'), w = document.createElement('div');
        w.className = 'toprow'; ch.before(w); w.append(ch, si);
        document.dispatchEvent(new Event('desk:relayout'));
      }
    })();
    // the top story's text and the close strip's sources note: a few lines, then "Read more"
    const clamp = (el, lines, label) => {
      if (!matchMedia('(max-width:860px)').matches || !el || !el.textContent) return;
      el.classList.add('clamp'); el.style.setProperty('--lines', lines);
      if (el.scrollHeight <= el.clientHeight + 4) { el.classList.remove('clamp'); return; }
      const b = document.createElement('button'); b.type = 'button'; b.className = 'readmore'; b.textContent = label;
      b.addEventListener('click', () => {
        const open = el.classList.toggle('clamp') === false;
        b.setAttribute('aria-expanded', open); b.textContent = open ? 'Show less' : label;
        if (!open) b.scrollIntoView({ block: 'nearest' });
      });
      el.after(b);
    };
    clamp($('top-body'), 6, 'Read more'); clamp($('close-note'), 2, 'Sources and notes');
    fold($('helped'), '.call-row', 2, 'helped'); fold($('hurt'), '.call-row', 2, 'hurt');

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
      if (p[1] > 400) {   // 3Y and 5Y need the full log, loaded once (the gold card may have loaded it already)
        if (!fullLoaded) { const f = await get('/data/markets.json'); fullLoaded = true; if (f && f.days) days = f.days; }
        idx = series((e) => e[cur.k], S.market);
      }
      const TTL = { 0: 'today', 7: 'last week', 30: 'last month', 182: 'last 6 months', 365: 'last 12 months', 1095: 'last 3 years', 1826: 'last 5 years' };
      $('chart-name').innerHTML = `${esc(cur.n)}, ${TTL[p[1]] || ''} <span class="num ${cls(change(idx, p[1]))}">${pct(change(idx, p[1]), 2)}</span>`;
      const lv = idx.length ? idx[idx.length - 1][1] : null, hc = change(idx, p[1]);
      $('ilvl').textContent = lv == null ? '—' : lv.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
      $('ichg').innerHTML = `<span class="${cls(hc)}">${pct(hc, 2)}</span> <span class="span-l">${SPAN[p[1]] || ''}</span>`;
      if (!p[1]) {   // the last session through the day, from desk/intraday.json
        const el = $('egx-chart'), mk = S.market, I = INTRA && INTRA[mk] && INTRA[mk].series[cur.intra]; el.innerHTML = '';
        if (!I) { el.style.height = 'auto'; el.innerHTML = '<p class="chart-cap">The last session through the day is not saved yet; the morning run saves it once the session has closed.</p>'; $('egx-cap').textContent = ''; return; }
        // a dotted line at the previous session's close, so a day that opened lower and climbed still reads as down
        const pv = idx.length > 1 ? idx[idx.length - 2][1] : null, ref = pv != null ? [{ value: pv, label: 'Prev. close ' + Charts.fmt.int(pv) }] : null;
        const v = I.map((x) => x[1]), vr = ref ? v.concat(pv) : v, lo = Math.min(...vr), hi = Math.max(...vr), mid = (lo + hi) / 2, half = Math.max((hi - lo) * 0.6, mid * 0.01);
        Charts.line(el, { ...dayAxis(I.map((x) => x[0]), el.clientWidth), series: [{ name: cur.n, values: v }], format: Charts.fmt.int, endLabel: true, height: el.clientHeight, min: mid - half, max: mid + half, reference: ref });
        const ch = change(idx, 0);
        $('egx-cap').innerHTML = `${day(INTRA[mk].session).toLocaleDateString('en-US', { weekday: 'long', day: 'numeric', month: 'short' }).replace('Sept', 'Sep')}, ${I[0][0]}–${I.at(-1)[0]} ${mk === 'egx' ? 'Cairo' : 'New York'} time · on the day <span class="num ${cls(ch)}">${pct(ch, 2)}</span>${INTRA[mk].proxy && INTRA[mk].proxy[cur.intra] ? ` · traced by the ${esc(INTRA[mk].proxy[cur.intra])} fund, which tracks it` : ''}`;
        return;
      }
      if (p[1] === 7 || p[1] === 30) {   // a week (every 15 minutes) or a month (every 30) through the day, once the saved sessions cover it
        const mo = p[1] === 30, src = (INTRA && INTRA[mo ? 'month' : 'week'] && INTRA[mo ? 'month' : 'week'][S.market]) || [];
        const all = src.filter((x) => x.session <= asOf(S.market) && (!mo || x.session > cut(asOf(S.market), 30)));
        const W = all.filter((x) => x.series[cur.intra] && x.series[cur.intra].length > 1);
        const full = W.length >= 2 && W.at(-1) === all.at(-1) && (!mo || (W.length === all.length && W.length >= 15 && W[0].session <= cut(asOf(S.market), 25)));
        if (full) {
          const el = $('egx-chart'), labels = [], vals = [], text = [], at = []; el.innerHTML = ''; let wk = null;
          W.forEach((x) => { const d = day(x.session), dl = mo ? `${MON[d.getMonth()]} ${d.getDate()}` : `${WD[d.getDay()]} ${d.getDate()}`, w = Math.floor((d - day('2026-01-04')) / 6048e5);
            if (!mo || w !== wk) at.push(labels.length); wk = w;
            x.series[cur.intra].forEach(([t, v]) => { labels.push(`${dl} ${t}`); vals.push(v); text.push(dl); }); });
          if (mo && at.length > 2 && at[1] - at[0] < (at[2] - at[1]) / 2) at.shift();
          const lo = Math.min(...vals), hi = Math.max(...vals);
          Charts.line(el, { labels, xAt: el.clientWidth < 520 && at.length > 3 ? at.filter((_, j) => (at.length - 1 - j) % 2 === 0) : at, xText: text, series: [{ name: cur.n, values: vals }], format: Charts.fmt.int, endLabel: true, height: el.clientHeight, min: lo - (hi - lo) * 0.15 });
          const ch = (vals.at(-1) / vals[0] - 1) * 100;
          $('egx-cap').innerHTML = `${esc(cur.n)}, last ${W.length} sessions through the day: <span class="num ${cls(ch)}">${pct(ch, 2)}</span> from the first trade`;
          return;
        }
      }
      const back = Math.max(p[1], 7), pts = idx.filter(([d]) => d >= cut(lastDate(idx), back)), el = $('egx-chart'); el.innerHTML = '';
      if (pts.length < 2) { el.textContent = 'Not enough closes logged yet.'; $('egx-cap').textContent = ''; return; }
      // a week has no shaded move; short series get a dot on each close
      const ann = back > 7 ? bigMove(pts) : [], vals = pts.map((x) => x[1]), lo = Math.min(...vals), hi = Math.max(...vals);
      Charts.line(el, { ...axis(pts.map((x) => x[0]), back, el.clientWidth), series: [{ name: cur.n, values: vals }], format: Charts.fmt.int, annotations: ann, endLabel: true, marks: pts.length <= 12, height: el.clientHeight, min: lo - (hi - lo) * 0.15 });
      const y = ytd(idx);
      $('egx-cap').innerHTML = `${esc(cur.n)}, ${p[2].toLowerCase()} · this year <span class="num ${cls(y)}">${pct(y)}</span>`;
    }
    // opens on 1D when the last session through the day is saved, otherwise on 1M
    const start = INTRA && INTRA[S.market] && INTRA[S.market].series[cur.intra] ? PERIODS[0] : PERIODS[2];
    segment($('egx-seg'), start[0], drawIdx, PERIODS.concat(LONG)); drawIdx(start);
    document.addEventListener('desk:relayout', () => drawIdx(per));   // the chart narrowed beside Since yesterday

    // biggest movers of the last session: the whole market (with the reason where one was found) or the desk's own stocks
    const MV = MOVERS && MOVERS[S.market], f2 = (v) => v.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    $('movers-more').textContent = key === 'egypt' ? 'EGX page →' : 'Wall Street page →'; $('movers-more').href = key === 'egypt' ? '/desk/egx/' : '/desk/us/';
    const mrow = (r) => { const own = NAMES[r.t], nm = `<b>${esc(own || r.name)}</b><span class="t">${esc(r.t)}</span>`;
      return `<div class="mv">${own ? `<a href="/desk/stock/?t=${encodeURIComponent(r.t)}">${nm}</a>` : `<span class="nm">${nm}</span>`}<span class="num">${f2(r.price)}</span><span class="num ${cls(r.pct)}">${pct(r.pct)}</span></div>`
        + (r.why && !/^no company news found/i.test(String(r.why).trim()) ? `<p class="mvwhy">${esc(r.why)}${r.url ? ` <a href="${esc(r.url)}" target="_blank" rel="noopener">${esc(r.source || 'Source')} →</a>` : ''}</p>` : ''); };
    const mlists = (up, down) => `<div class="movers"><div><h3><span class="chg up" aria-hidden="true"></span>Biggest gainers</h3>${up.map(mrow).join('') || '<p class="chart-cap">No stock rose.</p>'}</div><div><h3><span class="chg down" aria-hidden="true"></span>Biggest losers</h3>${down.map(mrow).join('') || '<p class="chart-cap">No stock fell.</p>'}</div></div>`;
    // most active: the five stocks with the most money traded in the session
    const drawActive = () => {
      const tv = (v) => (S.market === 'egx' ? 'EGP ' : '$') + (v >= 1e9 ? (v / 1e9).toFixed(2) + 'bn' : (v / 1e6).toFixed(v >= 1e8 ? 0 : 1) + 'm');
      const row = (r, i) => { const own = NAMES[r.t], nm = `<b>${esc(own || r.name)}</b><span class="t">${esc(r.t)}</span>`;
        return `<div class="mv mv-act"><span class="rk num">${i + 1}</span>${own ? `<a href="/desk/stock/?t=${encodeURIComponent(r.t)}">${nm}</a>` : `<span style="min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">${nm}</span>`}<span class="num">${f2(r.price)}</span><span class="num ${cls(r.pct)}">${pct(r.pct)}</span><span class="num tv">${tv(r.turnover)}</span></div>`; };
      $('movers').innerHTML = `<div class="movers"><div><h3>Most traded, by value</h3>${MV.active.slice(0, 5).map(row).join('')}</div></div>`;
      const sd = day(MV.session); $('movers-note').textContent = `Ranked by the value of shares traded, ${WD[sd.getDay()]}, ${MON[sd.getMonth()]} ${sd.getDate()}.`;
    };
    const drawMovers = (whole) => {
      if (whole === 'active') return drawActive();
      if (whole) {
        if (!MV) { $('movers').innerHTML = '<p class="chart-cap">Not saved yet; the morning run saves the last session\'s movers once it has closed.</p>'; $('movers-note').textContent = ''; return; }
        $('movers').innerHTML = mlists(MV.gainers.slice(0, 3), MV.losers.slice(0, 3));
        const sd = day(MV.session); $('movers-note').textContent = `${MV.basis}, ${WD[sd.getDay()]}, ${MON[sd.getMonth()]} ${sd.getDate()}.`;
        return;
      }
      // the desk's stocks on the day, from the data log; a reason carries over when the stock is also a whole-market mover
      // a reason: the whole-market list's when the stock was a market-wide mover, else its latest checked story within three days
      const notes = {}, since = cut(asOf(S.group), 3);
      for (const t of GROUP[S.group]) { const n = ((STOCKS[t] || {}).news || []).find((x) => x.date && x.date >= since && x.text); if (n) notes[t] = { why: n.text, source: n.source, url: n.url }; }
      if (MV) for (const r of MV.gainers.concat(MV.losers)) if (r.why) notes[r.t] = r;
      const rows = GROUP[S.group].map((t) => { const s = series((e) => (e[S.group] || {})[t], S.group), fresh = s.length && s[s.length - 1][0] === asOf(S.group);
        return fresh && s.length > 1 ? { t, price: s[s.length - 1][1], pct: change(s, 0), why: (notes[t] || {}).why, url: (notes[t] || {}).url, source: (notes[t] || {}).source } : null; }).filter((r) => r && r.pct != null).sort((a, b) => b.pct - a.pct);
      $('movers').innerHTML = mlists(rows.filter((r) => r.pct > 0).slice(0, 3), rows.filter((r) => r.pct < 0).reverse().slice(0, 3));
      const ad = day(asOf(S.group)); $('movers-note').textContent = `Among the desk's ${GROUP[S.group].length} ${key === 'egypt' ? 'Egyptian' : 'US'} stocks, ${WD[ad.getDay()]}, ${MON[ad.getMonth()]} ${ad.getDate()}. Tap one for its page.`;
    };
    $('mscope').innerHTML = ['Whole market', 'Desk stocks'].concat(MV && MV.active ? ['Most active'] : []).map((n, j) => `<button type="button" aria-pressed="${!j}">${n}</button>`).join('');
    $('mscope').querySelectorAll('button').forEach((b, j) => b.addEventListener('click', () => { $('mscope').querySelectorAll('button').forEach((x) => x.setAttribute('aria-pressed', x === b)); drawMovers(j === 2 ? 'active' : j === 0); }));
    drawMovers(true);
  }
  // each dashboard is its own page: /desk/egypt/ and /desk/usa/
  const pick = () => (document.body.dataset.section === 'usa' ? 'global' : 'egypt');
  render(pick());
})();

// theme, shared with the newsletter through localStorage
(function () {
  const tb = document.querySelector('.theme'); if (!tb) return; const lab = tb.querySelector('span');
  const sync = () => { lab.textContent = document.documentElement.getAttribute('data-theme') === 'dark' ? 'Light mode' : 'Dark mode'; };
  sync();
  tb.addEventListener('click', () => {
    const dark = document.documentElement.getAttribute('data-theme') !== 'dark';
    if (dark) document.documentElement.setAttribute('data-theme', 'dark'); else document.documentElement.removeAttribute('data-theme');
    try { localStorage.setItem('theme', dark ? 'dark' : 'light'); } catch (e) {}
    location.reload();
  });
})();
