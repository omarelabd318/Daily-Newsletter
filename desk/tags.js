// The "Moves" and "Affects" tags shared by the dashboards' stories and every page's news: what a story moves, sector
// first, then the stocks most exposed (desk stocks or not) and the markets it touches, each with its direction.
// A tag in the day's file: { kind: 'sector' | 'stock' | 'market', name, dir: 'up' | 'down' | 'mixed', t, chg }
//   t: the stock's ticker (a desk stock links to its page and its name can be left out); chg: the % change the story
//   gives, if any (never filled from the log: a tag's direction is the story's effect, which a day's move can contradict).
//   Tags.html(list, { names, max }) → '<span class="tags">…</span>', or '' for an empty list.
window.Tags = (() => {
  const esc = (s) => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  const DIR = { up: ['up', 'rises on this'], down: ['down', 'falls on this'], mixed: ['flat', 'mixed'] };
  const KIND = { sector: 'Sector', stock: 'Stock', market: 'Market' };
  const pct = (v) => (v > 0 ? '+' : v < 0 ? '−' : '') + Math.abs(v).toFixed(1) + '%';
  function one(x, names = {}) {
    const d = DIR[x.dir] || DIR.mixed, kind = x.kind in KIND ? x.kind : 'sector';
    const name = x.name || names[x.t] || x.t || '';
    const c = x.chg;
    const inner = `<span class="chg ${d[0]}" aria-hidden="true"></span>${esc(name)}${kind === 'stock' && c != null ? ` <span class="num">${pct(c)}</span>` : ''}`;
    const title = `${KIND[kind]}: ${name}${x.t && name !== x.t ? ` (${x.t})` : ''}, ${d[1]}`;
    return x.t && names[x.t]
      ? `<a class="tag ${kind} ${d[0]}" href="/desk/stock/?t=${encodeURIComponent(x.t)}" title="${esc(title)}">${inner}</a>`
      : `<span class="tag ${kind} ${d[0]}" title="${esc(title)}">${inner}</span>`;
  }
  const html = (list, { names = {}, max = 8 } = {}) =>
    (list && list.length ? `<span class="tags">${list.slice(0, max).map((x) => one(x, names)).join('')}</span>` : '');
  return { html, one };
})();
