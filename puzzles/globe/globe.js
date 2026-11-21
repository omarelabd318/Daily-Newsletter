// The Globe: find the day's mystery country. Each guess is painted on the globe, warmer (deeper red) the closer its
// border is to the answer's. One country a day, the same for everyone, plus practice rounds to play as often as you
// like. Data: world.json (built by build.mjs); drawing: d3-geo and topojson-client in lib.js.
(function(){
  var $ = function(id){ return document.getElementById(id); };
  var store = { get: function(k){ try { return JSON.parse(localStorage.getItem(k)); } catch(e){ return null; } }, set: function(k, v){ try { localStorage.setItem(k, JSON.stringify(v)); } catch(e){} } };
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var W, feats = [], land = [], byIdx = [], pool = [], lookup = {}, names = [];
  var mode = 'daily', date, state, ans, msg = '';

  window.Globe = { start: function(d){
    date = d;
    $('gl-meta').textContent = 'Loading the globe';
    fetch('/puzzles/globe/world.json').then(function(r){ if(!r.ok) throw 0; return r.json(); }).then(function(w){ W = w; init(); }, function(){ $('gl-meta').textContent = 'The globe did not load. Try again later.'; });
  } };

  // ---- names: what a player types is matched without accents, case, dots or a leading "the" ----
  function norm(s){ return s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/&/g, ' and ').replace(/\bst\.?\s/g, 'saint ').replace(/[^a-z ]/g, ' ').replace(/^\s*the\s+/, '').replace(/\s+/g, ' ').trim(); }

  function init(){
    var geos = W.topo.objects.countries.geometries;
    geos.forEach(function(g){
      var f = topojson.feature(W.topo, g); f.p = g.properties; f.c = d3.geoCentroid(f);
      // a country spread over far islands (France, the US): aim at its biggest piece instead of the middle of the sea
      if(f.geometry.type === 'MultiPolygon'){ var big = null, ba = -1; f.geometry.coordinates.forEach(function(poly){ var a = d3.geoArea({type:'Polygon', coordinates:poly}); if(a > ba){ ba = a; big = poly; } }); f.c = d3.geoCentroid({type:'Polygon', coordinates:big}); }
      land.push(f);
      if(f.p.g){ byIdx[f.p.i] = f; names.push(f.p.n); [f.p.n].concat(f.p.k || []).forEach(function(n){ lookup[norm(n)] = f.p.i; }); if(f.p.a) pool.push(f.p.i); }
    });
    names.sort(function(a, b){ return a.localeCompare(b); });
    pool.sort(function(a, b){ return a - b; });
    globe(); form();
    $('gl-daily').addEventListener('click', function(){ setMode('daily'); });
    $('gl-prac').addEventListener('click', function(){ setMode('practice'); });
    $('gl-new').addEventListener('click', function(){ if(mode !== 'practice') return setMode('practice'); if(state.g.length && !state.won && !state.gave && !confirm('Start a new country? This one will count as unsolved.')) return; if(state.g.length && !state.won && !state.gave) record(false); newPractice(); });
    $('gl-give').addEventListener('click', function(){ if(state.won || state.gave) return; if(!confirm(mode === 'daily' ? 'Give up on today’s country and see the answer?' : 'Show the answer?')) return; state.gave = 1; if(mode === 'practice') record(false); save(); msg = 'The answer was ' + byIdx[ans].p.n + '.'; render(); fly(byIdx[ans]); });
    setMode(location.hash === '#gl-practice' ? 'practice' : 'daily');
  }

  // ---- which country: today's is fixed by the date (a shuffled list, so none comes back for months); practice is random ----
  function rng(seed){ return function(){ seed |= 0; seed = seed + 0x6D2B79F5 | 0; var t = Math.imul(seed ^ seed >>> 15, 1 | seed); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
  function dailyAnswer(d){
    var r = rng(20261121), p = pool.slice();
    for(var i = p.length - 1; i > 0; i--){ var j = Math.floor(r() * (i + 1)), x = p[i]; p[i] = p[j]; p[j] = x; }
    var n = Math.round((Date.UTC(+d.slice(0, 4), +d.slice(5, 7) - 1, +d.slice(8, 10)) - Date.UTC(2026, 0, 1)) / 864e5);
    return p[((n % p.length) + p.length) % p.length];
  }
  function newPractice(){
    var recent = (store.get('puz:gl:recent') || []).concat([dailyAnswer(date)]), cand = pool.filter(function(i){ return recent.indexOf(i) < 0; });
    var a = cand[Math.floor(Math.random() * cand.length)];
    store.set('puz:gl:recent', (store.get('puz:gl:recent') || []).concat([a]).slice(-40));
    state = { a: a, g: [] }; ans = a; msg = 'A new country is hidden. Make a first guess.'; save(); render(); spinHome();
  }
  function setMode(m){
    mode = m;
    $('gl-daily').setAttribute('aria-pressed', m === 'daily'); $('gl-prac').setAttribute('aria-pressed', m === 'practice');
    try { history.replaceState(null, '', location.pathname + location.search + (m === 'practice' ? '#gl-practice' : '#gl')); } catch(e){}
    if(m === 'daily'){ ans = dailyAnswer(date); state = store.get('puz:gl:' + date) || { g: [] }; msg = state.won ? 'Solved. A new country tomorrow, or play a practice round.' : state.gave ? 'The answer was ' + byIdx[ans].p.n + '.' : state.g.length ? '' : 'Type any country to start.'; }
    else { state = store.get('puz:gl:prac'); if(!state || state.a == null || pool.indexOf(state.a) < 0) return newPractice(); ans = state.a; msg = state.won || state.gave ? 'Press New country for another.' : state.g.length ? '' : 'A country is hidden. Make a first guess.'; }
    render();
    var last = state.won || state.gave ? byIdx[ans] : state.g.length ? byIdx[state.g[state.g.length - 1]] : null;
    if(last) fly(last, true); else spinHome();
  }
  function save(){ store.set(mode === 'daily' ? 'puz:gl:' + date : 'puz:gl:prac', state); }
  function record(won){ var s = store.get('puz:gl:stats') || {p: 0, w: 0, t: 0, b: 0}; s.p++; if(won){ s.w++; s.t += state.g.length; if(!s.b || state.g.length < s.b) s.b = state.g.length; } store.set('puz:gl:stats', s); }

  // ---- distance between two countries' closest borders, in km (0: they share a border) ----
  function dist(i, j){ if(i === j) return 0; if(i > j){ var x = i; i = j; j = x; } return W.dist[i * W.n - i * (i + 1) / 2 + (j - i - 1)]; }
  // the heat scale: pale sand far away, through orange, to a deep red for a neighbour
  var STOPS = [[0, [122, 22, 16]], [400, [170, 40, 26]], [1200, [214, 86, 50]], [2500, [235, 140, 80]], [4500, [242, 186, 122]], [8000, [246, 222, 170]], [13000, [247, 238, 214]]];
  function heat(d){
    for(var k = 1; k < STOPS.length; k++) if(d <= STOPS[k][0]){ var a = STOPS[k - 1], b = STOPS[k], t = (d - a[0]) / (b[0] - a[0]); return 'rgb(' + a[1].map(function(v, q){ return Math.round(v + (b[1][q] - v) * t); }).join(',') + ')'; }
    return 'rgb(' + STOPS[STOPS.length - 1][1].join(',') + ')';
  }
  var WIN = '#2f8a4f';
  function color(i){ return i === ans ? WIN : heat(dist(i, ans)); }
  function km(d){ return d === 0 ? 'Borders it' : d.toLocaleString('en-US') + ' km'; }

  // ---- the guess box, with suggestions as you type ----
  function form(){
    var inp = $('gl-in'), sug = $('gl-sug'), on = -1, list = [];
    function show(){
      var q = norm(inp.value); on = -1;
      list = q ? names.filter(function(n){ return norm(n).indexOf(q) === 0; }).concat(names.filter(function(n){ var m = norm(n); return m.indexOf(q) > 0 && m.indexOf(' ' + q) >= 0; })).slice(0, 6) : [];
      var al = Object.keys(lookup).filter(function(k){ return q.length > 1 && k.indexOf(q) === 0; }).map(function(k){ return byIdx[lookup[k]].p.n; });
      al.forEach(function(n){ if(list.indexOf(n) < 0 && list.length < 6) list.push(n); });
      sug.innerHTML = list.map(function(n, i){ return '<li role="option" data-i="' + i + '">' + esc(n) + '</li>'; }).join(''); sug.hidden = !list.length;
    }
    function pick(i){ inp.value = list[i]; sug.hidden = true; go(); }
    function hl(){ [].forEach.call(sug.children, function(li, i){ li.classList.toggle('on', i === on); }); }
    inp.addEventListener('input', show);
    inp.addEventListener('keydown', function(e){
      if(e.key === 'ArrowDown' && !sug.hidden){ on = Math.min(list.length - 1, on + 1); hl(); e.preventDefault(); }
      else if(e.key === 'ArrowUp' && !sug.hidden){ on = Math.max(-1, on - 1); hl(); e.preventDefault(); }
      else if(e.key === 'Escape'){ sug.hidden = true; }
      else if(e.key === 'Enter' && on >= 0){ e.preventDefault(); pick(on); }
    });
    sug.addEventListener('mousedown', function(e){ var li = e.target.closest('li'); if(li){ e.preventDefault(); pick(+li.dataset.i); } });
    inp.addEventListener('blur', function(){ setTimeout(function(){ sug.hidden = true; }, 120); });
    $('gl-form').addEventListener('submit', function(e){ e.preventDefault(); go(); });
    function go(){
      var v = inp.value.trim(); if(!v) return; sug.hidden = true;
      if(state.won || state.gave){ msg = mode === 'daily' ? 'Today’s country is done. Try a practice round.' : 'Press New country for another.'; render(); return; }
      var i = lookup[norm(v)];
      if(i == null){ var q = norm(v), hit = names.filter(function(n){ return norm(n).indexOf(q) === 0; }); if(hit.length === 1) i = lookup[norm(hit[0])]; }
      if(i == null){ msg = 'No country called “' + v + '”. Check the spelling.'; render(); return; }
      inp.value = '';
      if(state.g.indexOf(i) >= 0){ msg = byIdx[i].p.n + ' is already on the globe.'; render(); fly(byIdx[i]); return; }
      var before = state.g.length ? Math.min.apply(null, state.g.map(function(x){ return dist(x, ans); })) : null, d = dist(i, ans);
      state.g.push(i);
      if(i === ans){ state.won = 1; if(mode === 'practice') record(true); msg = 'Found it: ' + byIdx[i].p.n + ', in ' + state.g.length + (state.g.length === 1 ? ' guess.' : ' guesses.'); save(); render(); fly(byIdx[i]); setTimeout(won, reduce ? 200 : 1100); return; }
      var n = byIdx[i].p.n;
      msg = d === 0 ? n + ' borders the answer!' : before == null ? n + ' is ' + km(d) + ' from the answer.' : d < before ? 'Warmer. ' + n + ' is ' + km(d) + ' away, the closest yet.' : d === before ? n + ' is just as close: ' + km(d) + '.' : 'Colder. ' + n + ' is ' + km(d) + ' away.';
      save(); render(); fly(byIdx[i]);
    }
  }
  function esc(s){ return String(s).replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }

  // ---- everything but the globe: the message, the list of guesses (closest first), the counts and buttons ----
  function render(){
    $('gl-msg').textContent = msg;
    var g = state.g, done = state.won || state.gave;
    $('gl-meta').textContent = (mode === 'daily' ? 'Today’s country · ' + new Date(date + 'T12:00:00').toLocaleDateString('en-US', {month:'long', day:'numeric'}) : 'Practice round') + ' · ' + g.length + (g.length === 1 ? ' guess' : ' guesses');
    $('gl-in').disabled = !!done; $('gl-in').placeholder = done ? (mode === 'daily' ? 'Done for today' : 'Press New country') : 'Type a country';
    $('gl-give').hidden = !!done || !g.length; $('gl-give').textContent = mode === 'daily' ? 'Give up' : 'Show answer';
    $('gl-new').hidden = mode === 'daily';
    $('gl-new').textContent = mode === 'daily' ? 'Practice round' : 'New country';
    var rows = g.slice().sort(function(a, b){ return dist(a, ans) - dist(b, ans); });
    $('gl-list').innerHTML = rows.length ? rows.map(function(i){ return '<li data-i="' + i + '"><i style="background:' + color(i) + '"></i><span>' + esc(byIdx[i].p.n) + '</span><small>' + (i === ans ? 'The answer' : km(dist(i, ans))) + '</small></li>'; }).join('') : '<li class="none">Your guesses will be listed here, closest first.</li>';
    if(state.gave && g.indexOf(ans) < 0) $('gl-list').insertAdjacentHTML('afterbegin', '<li data-i="' + ans + '" class="ans"><i style="background:' + WIN + '"></i><span>' + esc(byIdx[ans].p.n) + '</span><small>The answer</small></li>');
    var s = store.get('puz:gl:stats');
    $('gl-stats').textContent = mode === 'practice' && s && s.p ? 'Practice: ' + s.p + ' played, ' + s.w + ' found' + (s.w ? ', ' + (s.t / s.w).toFixed(1) + ' guesses on average, best ' + s.b : '') + '.' : '';
    draw();
  }
  [].forEach.call(document.querySelectorAll('#gl-list'), function(ol){ ol.addEventListener('click', function(e){ var li = e.target.closest('li[data-i]'); if(li) fly(byIdx[+li.dataset.i]); }); });

  function won(){
    var old = document.querySelector('.won-card'); if(old) old.remove();
    var n = state.g.length, card = document.createElement('div'); card.className = 'won-card'; card.setAttribute('role', 'dialog'); card.setAttribute('aria-label', 'Found');
    card.innerHTML = '<div class="won-in"><p class="won-k">' + (mode === 'daily' ? 'The Globe · today’s country' : 'The Globe · practice') + '</p><h3>Found</h3><p class="won-t"><span></span> in <b>' + n + '</b> ' + (n === 1 ? 'guess' : 'guesses') + '</p>'
      + '<p class="won-s">' + (mode === 'daily' ? 'A new country tomorrow. Until then, practice as much as you like.' : 'Another one?') + '</p><div class="won-b"><button type="button" data-a="more">' + (mode === 'daily' ? 'Practice round' : 'New country') + '</button><button type="button" data-a="close" class="ghost">Close</button></div></div>';
    card.querySelector('.won-t span').textContent = byIdx[ans].p.n;
    card.addEventListener('click', function(e){ var a = e.target.dataset && e.target.dataset.a; if(e.target === card || a === 'close') card.remove(); if(a === 'more'){ card.remove(); if(mode === 'daily') setMode('practice'); else newPractice(); } });
    document.body.appendChild(card); card.querySelector('button').focus();
  }
  // ---- the globe: an orthographic map on a canvas; drag to turn it, scroll or pinch to zoom, tap a guess for its name ----
  var cv, cx, proj, path, size, zoom = 1, rot = [-30, -20], anim = null, spin = null, grat = d3.geoGraticule10(), tip;
  function globe(){
    cv = $('gl-cv'); cx = cv.getContext('2d'); tip = $('gl-tip');
    proj = d3.geoOrthographic().clipAngle(90).precision(0.4); path = d3.geoPath(proj, cx);
    fit(); window.addEventListener('resize', function(){ fit(); draw(); });
    var ptrs = {}, start = null, moved = false, pinch = null;
    cv.addEventListener('pointerdown', function(e){ cv.setPointerCapture(e.pointerId); ptrs[e.pointerId] = [e.clientX, e.clientY]; stop(); moved = false;
      var ks = Object.keys(ptrs); if(ks.length === 2){ var a = ptrs[ks[0]], b = ptrs[ks[1]]; pinch = { d: Math.hypot(a[0] - b[0], a[1] - b[1]), z: zoom }; } else start = { x: e.clientX, y: e.clientY, r: rot.slice() }; });
    cv.addEventListener('pointermove', function(e){
      if(!ptrs[e.pointerId]){ hover(e); return; }
      ptrs[e.pointerId] = [e.clientX, e.clientY]; var ks = Object.keys(ptrs);
      if(ks.length === 2 && pinch){ var a = ptrs[ks[0]], b = ptrs[ks[1]]; setZoom(pinch.z * Math.hypot(a[0] - b[0], a[1] - b[1]) / pinch.d); moved = true; return; }
      if(!start) return; var dx = e.clientX - start.x, dy = e.clientY - start.y; if(Math.abs(dx) + Math.abs(dy) > 4) moved = true;
      var k = 180 / (Math.PI * proj.scale());   // degrees per pixel, so the land follows the finger
      rot = [start.r[0] + dx * k, Math.max(-90, Math.min(90, start.r[1] - dy * k))]; draw();
    });
    function up(e){ delete ptrs[e.pointerId]; if(Object.keys(ptrs).length < 2) pinch = null; if(!Object.keys(ptrs).length){ if(!moved) tap(e); start = null; } }
    cv.addEventListener('pointerup', up); cv.addEventListener('pointercancel', up);
    cv.addEventListener('pointerleave', function(){ if(!Object.keys(ptrs).length) tip.hidden = true; });
    cv.addEventListener('wheel', function(e){ e.preventDefault(); stop(); setZoom(zoom * Math.exp(-e.deltaY * 0.0015)); }, { passive: false });
    $('gl-zin').addEventListener('click', function(){ stop(); setZoom(zoom * 1.5); });
    $('gl-zout').addEventListener('click', function(){ stop(); setZoom(zoom / 1.5); });
  }
  function fit(){
    var phone = innerWidth < 860, s = phone ? Math.min(innerWidth - 24, 520) : Math.max(340, Math.min(540, innerHeight - 330, Math.min(innerWidth, 1180) - 660));
    size = Math.floor(s); var dpr = Math.min(2, window.devicePixelRatio || 1);
    cv.width = size * dpr; cv.height = size * dpr; cv.style.width = cv.style.height = size + 'px'; cx.setTransform(dpr, 0, 0, dpr, 0, 0);
    proj.translate([size / 2, size / 2]); setZoom(zoom, true);
  }
  function setZoom(z, quiet){ zoom = Math.max(1, Math.min(12, z)); proj.scale((size / 2 - 6) * zoom); if(!quiet) draw(); }
  function stop(){ if(anim){ cancelAnimationFrame(anim); anim = null; } spin = null; }
  function draw(){
    if(!cv || !W) return;
    proj.rotate([rot[0], rot[1], 0]);
    var r = proj.scale(), c = size / 2;
    cx.clearRect(0, 0, size, size);
    // the sea: a soft blue-grey, lighter where the light falls
    var g = cx.createRadialGradient(c - r * .35, c - r * .4, r * .1, c, c, r * 1.02); g.addColorStop(0, '#cbd8da'); g.addColorStop(1, '#93a9b0');
    cx.beginPath(); path({type: 'Sphere'}); cx.fillStyle = g; cx.fill();
    cx.beginPath(); path(grat); cx.strokeStyle = 'rgba(20,17,13,.09)'; cx.lineWidth = .6; cx.stroke();
    // land, then the guesses on top
    var guessed = {}; state && state.g.forEach(function(i){ guessed[i] = 1; }); if(state && state.gave) guessed[ans] = 1;
    cx.beginPath(); land.forEach(function(f){ if(!(f.p.g && guessed[f.p.i])) path(f); }); cx.fillStyle = '#d9d3bf'; cx.fill(); cx.strokeStyle = 'rgba(20,17,13,.3)'; cx.lineWidth = .5; cx.stroke();
    Object.keys(guessed).forEach(function(k){ var f = byIdx[k]; cx.beginPath(); path(f); cx.fillStyle = color(+k); cx.fill(); cx.strokeStyle = '#14110d'; cx.lineWidth = .9; cx.stroke();
      // a small country gets a ring so it can be seen at any zoom
      if(f.p.s){ var p = proj(f.c), vis = d3.geoDistance(f.c, [-rot[0], -rot[1]]) < Math.PI / 2; if(p && vis){ cx.beginPath(); cx.arc(p[0], p[1], 7, 0, 2 * Math.PI); cx.strokeStyle = color(+k); cx.lineWidth = 2.5; cx.stroke(); } } });
    cx.beginPath(); path({type: 'Sphere'}); cx.strokeStyle = '#14110d'; cx.lineWidth = 1.4; cx.stroke();
  }
  // turn the globe so a country faces you
  function fly(f, now){
    stop(); var to = [-f.c[0], -f.c[1]];
    if(now || reduce){ rot = to; draw(); return; }
    var from = rot.slice(), t0 = performance.now(), dur = 900, ip = d3.geoInterpolate([-from[0], -from[1]], f.c), z0 = zoom;
    (function step(t){ var k = Math.min(1, (t - t0) / dur), e = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2, p = ip(e);
      rot = [-p[0], -p[1]]; if(z0 > 2.5) setZoom(z0 + (2.5 - z0) * e, true); draw(); anim = k < 1 ? requestAnimationFrame(step) : null; })(t0);
  }
  // before the first guess the globe turns slowly on its own
  function spinHome(){
    stop(); rot = [rot[0], -18]; draw(); if(reduce) return;
    var last = performance.now(); spin = true;
    (function step(t){ if(!spin) return; rot[0] += (t - last) * 0.006; last = t; draw(); anim = requestAnimationFrame(step); })(last);
  }
  function at(e){ var b = cv.getBoundingClientRect(), p = proj.invert([e.clientX - b.left, e.clientY - b.top]); if(!p || d3.geoDistance(p, [-rot[0], -rot[1]]) > Math.PI / 2) return null;
    var hit = null; state.g.concat(state.gave ? [ans] : []).forEach(function(i){ var f = byIdx[i]; if(d3.geoContains(f, p) || (f.p.s && d3.geoDistance(f.c, p) * proj.scale() < 9)) hit = f; }); return { f: hit, x: e.clientX - b.left, y: e.clientY - b.top }; }
  function showTip(h){ if(!h || !h.f){ tip.hidden = true; return; } var i = h.f.p.i; tip.textContent = h.f.p.n + (i === ans ? ' — the answer' : ' · ' + km(dist(i, ans))); tip.style.left = h.x + 'px'; tip.style.top = h.y + 'px'; tip.hidden = false; }
  function hover(e){ if(e.pointerType === 'mouse') showTip(at(e)); }
  function tap(e){ showTip(at(e)); }
})();
