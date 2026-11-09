// Find a stock: the search box in the desk's menu and the phone's top bar, on every desk page and both dashboards.
(function () {
  const esc = (s) => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  // find a stock: type a ticker or part of a name (CIB, nvidia, palm), arrows to pick, Enter to open its page
  const ALIAS = { COMI: 'cib', HRHO: 'efg hermes', 'BRK.B': 'berkshire', GOOGL: 'google', META: 'facebook', ETEL: 'we', EFIH: 'efinance', EMFD: 'emaar' };
  window.DeskSearch = function (box, NAMES, GROUP) {
    const inp = box.querySelector('input'), out = box.querySelector('.dsr');
    let hits = [], at = 0;
    const norm = (x) => x.toLowerCase().replace(/[^a-z0-9.]/g, '');
    const draw = () => {
      out.hidden = !hits.length;
      out.innerHTML = hits.map((t, i) => `<a role="option" href="/desk/stock/?t=${encodeURIComponent(t)}"${i === at ? ' aria-selected="true"' : ''}><b>${esc(t)}</b><span>${esc(NAMES[t])}</span><i>${GROUP.egx.includes(t) ? 'EGX' : 'US'}</i></a>`).join('');
    };
    inp.addEventListener('input', () => {
      const q = norm(inp.value); at = 0;
      if (!q) { hits = []; return draw(); }
      const all = [...GROUP.egx, ...GROUP.us], score = (t) => {
        const tk = norm(t), nm = norm(NAMES[t] || ''), al = norm(ALIAS[t] || '');
        return tk === q ? 0 : tk.startsWith(q) ? 1 : nm.startsWith(q) || al.startsWith(q) ? 2 : nm.includes(q) || al.includes(q) ? 3 : 9;
      };
      hits = all.filter((t) => score(t) < 9).sort((a, b) => score(a) - score(b)).slice(0, 7); draw();
    });
    inp.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') { e.preventDefault(); if (hits.length) { at = (at + (e.key === 'ArrowDown' ? 1 : hits.length - 1)) % hits.length; draw(); } }
      else if (e.key === 'Enter' && hits[at]) { e.preventDefault(); location.href = '/desk/stock/?t=' + encodeURIComponent(hits[at]); }
      else if (e.key === 'Escape') { inp.value = ''; hits = []; draw(); inp.blur(); }
    });
    inp.addEventListener('blur', () => setTimeout(() => { out.hidden = true; }, 150));
    inp.addEventListener('focus', () => { if (hits.length) out.hidden = false; });
  };
})();
