// The EGX30 by sector: a treemap of its members, each box sized by market value and coloured by its change over the
// session, five sessions or 21 sessions (TradingView, saved in the movers file); a desk stock opens its page.
// Used by the EGX page (opening on the day) and The week (opening on the week). The page supplies the elements
// #c-heat, #hseg, #heat, #heat-key and #heat-cap.
window.DeskHeat = function (M, HT, k0) {
    M.$('c-heat').hidden = false;
    // squarified treemap: rows of boxes laid along the shorter side, each row as close to square as it can be
    const squarify = (items, x, y, w, h) => {
      const out = [], total = items.reduce((a, b) => a + b.v, 0), scale = (w * h) / total;
      let rest = items.map((it) => ({ ...it, a: it.v * scale })), X = x, Y = y, W = w, H = h;
      const worst = (row, side) => { const s = row.reduce((a, b) => a + b.a, 0), mx = Math.max(...row.map((r) => r.a)), mn = Math.min(...row.map((r) => r.a)); return Math.max(side * side * mx / (s * s), (s * s) / (side * side * mn)); };
      while (rest.length) {
        const side = Math.min(W, H); let row = [rest[0]], i = 1;
        while (i < rest.length && worst(row.concat(rest[i]), side) <= worst(row, side)) row.push(rest[i++]);
        rest = rest.slice(i);
        const s = row.reduce((a, b) => a + b.a, 0);
        if (W >= H) { const cw = s / H; let yy = Y; for (const r of row) { const ch = r.a / cw; out.push({ ...r, x: X, y: yy, w: cw, h: ch }); yy += ch; } X += cw; W -= cw; }
        else { const ch = s / W; let xx = X; for (const r of row) { const cw = r.a / ch; out.push({ ...r, x: xx, y: Y, w: cw, h: ch }); xx += cw; } Y += ch; H -= ch; }
      }
      return out;
    };
    const SCALE = { d1: 3, w1: 6, m1: 10 }, LBL = { d1: 'on the day', w1: 'over five sessions', m1: 'over 21 sessions' };
    const colour = (v, k) => { const t = Math.min(1, Math.abs(v) / SCALE[k]); return Math.abs(v) < 0.05 ? 'var(--raised)' : `color-mix(in srgb, var(${v > 0 ? '--positive' : '--negative'}) ${Math.round(18 + t * 72)}%, var(--surface))`; };
    const drawHeat = (k) => {
      const el = M.$('heat'), W = el.clientWidth, H = W < 600 ? 520 : 440, LH = 18;
      const groups = {}; for (const r of HT.rows) (groups[r.sector] = groups[r.sector] || []).push(r);
      const secs = Object.entries(groups).map(([name, rs]) => ({ name, rs: rs.sort((a, b) => b.cap - a.cap), v: rs.reduce((a, r) => a + r.cap, 0) })).sort((a, b) => b.v - a.v);
      let html = '';
      for (const s of squarify(secs, 0, 0, W, H)) {
        // the sector's change: its members' changes weighted by market value
        const sc = s.rs.reduce((a, r) => a + r[k] * r.cap, 0) / s.v, lab = s.h > 40 && s.w > 70;
        html += `<div class="heat-s" style="left:${s.x}px;top:${s.y}px;width:${s.w}px;height:${s.h}px">` + (lab ? `<div class="heat-sh"><span>${M.esc(s.name)}</span><span class="num ${M.cls(sc)}">${M.pct(sc, 2)}</span></div>` : '');
        for (const b of squarify(s.rs.map((r) => ({ ...r, v: r.cap })), 1, (lab ? LH : 0) + 1, Math.max(0, s.w - 2), Math.max(0, s.h - (lab ? LH : 0) - 2))) {
          const v = b[k], strong = Math.abs(v) / SCALE[k] > 0.55, own = M.NAMES[b.t], big = b.w > 46 && b.h > 30;
          const inner = big ? `<b>${M.esc(b.t)}</b><span class="num">${M.pct(v, 2)}</span>` : '';
          const tag = own ? 'a' : 'div', href = own ? ` href="/desk/stock/?t=${encodeURIComponent(b.t)}"` : '';
          html += `<${tag}${href} class="heat-b${strong ? ' strong' : ''}" data-i="${HT.rows.indexOf(HT.rows.find((r) => r.t === b.t))}" aria-label="${M.esc(own || b.name)} (${M.esc(b.t)}): ${M.pct(v, 2)} ${LBL[k]}" style="left:${b.x}px;top:${b.y}px;width:${Math.max(0, b.w - 2)}px;height:${Math.max(0, b.h - 2)}px;background:${colour(v, k)}">${inner}</${tag}>`;
        }
        html += '</div>';
      }
      el.style.height = H + 'px'; el.innerHTML = html + '<div class="heat-tip" hidden></div>';
      const sc = SCALE[k];
      M.$('heat-key').innerHTML = `<span class="num">−${sc}%</span>` + [-1, -0.66, -0.33, 0, 0.33, 0.66, 1].map((f) => `<i style="background:${colour(f * sc, k)}"></i>`).join('') + `<span class="num">+${sc}%</span>`;
      const ups = HT.rows.filter((r) => r[k] > 0).length;
      M.$('heat-cap').textContent = `${HT.rows.length} members ${LBL[k]} to ${M.short(HT.session)}: ${ups} up, ${HT.rows.length - ups} down or flat. Boxes are sized by market value; a desk stock opens its page.`;
    };
    // the box shown over a member: its name and sector, last close, change for the period shown, shares traded,
    // market value and its share of the members' combined value; a desk stock opens its page on a click
    const total = HT.rows.reduce((a, r) => a + r.cap, 0), PER = { d1: '1D', w1: '1W', m1: '1M' };
    const big = (v) => (v >= 1e9 ? (v / 1e9).toFixed(1) + 'bn' : v >= 1e6 ? (v / 1e6).toFixed(2) + 'm' : Math.round(v).toLocaleString('en-US'));
    const tipHtml = (r) => { const own = M.NAMES[r.t];
      return `<div class="ht-h"><b>${M.esc(r.t)}</b><span>${M.esc(r.sector)}</span></div><div class="ht-n">${M.esc(own || r.name)}</div>`
        + M.kv([['Last', r.price != null ? 'EGP ' + M.num(r.price, 2) : '—'], [`Change ${PER[hk]}`, `<span class="${M.cls(r[hk])}">${M.pct(r[hk], 2)}</span>`],
          ['Volume', r.vol != null ? big(r.vol) + ' shares' : '—'], ['Market value', 'EGP ' + big(r.cap)], ['Share of the EGX30 members\' value', (r.cap / total * 100).toFixed(2) + '%']])
        + (own ? '<div class="ht-f">Click to open its page</div>' : ''); };
    const heatEl = M.$('heat');
    const showTip = (box, ev) => {
      const tip = heatEl.querySelector('.heat-tip'), r = HT.rows[+box.dataset.i]; if (!tip || !r) return;
      tip.innerHTML = tipHtml(r); tip.hidden = false;
      const hr = heatEl.getBoundingClientRect(), tw = tip.offsetWidth, th = tip.offsetHeight;
      const px = (ev && ev.clientX != null ? ev.clientX : box.getBoundingClientRect().left + box.offsetWidth / 2) - hr.left, py = (ev && ev.clientY != null ? ev.clientY : box.getBoundingClientRect().top + box.offsetHeight / 2) - hr.top;
      tip.style.left = Math.max(0, Math.min(hr.width - tw, px + 14)) + 'px';
      tip.style.top = Math.max(0, py + 14 + th > hr.height ? py - th - 10 : py + 14) + 'px';
    };
    heatEl.addEventListener('pointermove', (e) => { const box = e.target.closest('.heat-b'); if (box && e.pointerType !== 'touch') showTip(box, e); else if (!box) { const t = heatEl.querySelector('.heat-tip'); if (t) t.hidden = true; } });
    heatEl.addEventListener('pointerleave', () => { const t = heatEl.querySelector('.heat-tip'); if (t) t.hidden = true; });
    heatEl.addEventListener('focusin', (e) => { const box = e.target.closest('.heat-b'); if (box) showTip(box); });
    // on a phone a tap shows the box; a desk stock's box opens its page on a second tap
    heatEl.addEventListener('click', (e) => { const box = e.target.closest('.heat-b'); if (!box || !matchMedia('(hover: none)').matches) return;
      if (box.dataset.shown !== '1') { e.preventDefault(); heatEl.querySelectorAll('.heat-b').forEach((b) => delete b.dataset.shown); box.dataset.shown = '1'; showTip(box); } });
    let hk = k0 || 'd1';
    M.segment(M.$('hseg'), PER[hk], (p) => { hk = { 0: 'd1', 7: 'w1', 30: 'm1' }[p[1]]; drawHeat(hk); }, M.PERIODS.slice(0, 3)); drawHeat(hk);
    let hw = M.$('heat').clientWidth; addEventListener('resize', () => { if (Math.abs(M.$('heat').clientWidth - hw) > 4) { hw = M.$('heat').clientWidth; drawHeat(hk); } });
};
