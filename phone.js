/* The newsletter on a phone: the bar that follows you down the page, the tab bar, the sections and archive sheets,
   swiping between editions, and a note when a newer edition is out. Styles in phone.css; nothing shows above 640px. */
(function(){
  var mq = window.matchMedia('(max-width:640px)');
  var $ = function(id){ return document.getElementById(id); };
  var root = document.documentElement;
  var I = {
    today:'<path d="M4 5h13v14H6a2 2 0 0 1-2-2z"/><path d="M17 9h3v8a2 2 0 0 1-2 2"/><path d="M7 9h7M7 12.5h7M7 16h4"/>',
    sections:'<path d="M4 6h16M4 12h16M4 18h10"/>',
    listen:'<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="14" width="4" height="6" rx="1.5"/><rect x="17" y="14" width="4" height="6" rx="1.5"/>',
    archive:'<rect x="3" y="4" width="18" height="16" rx="1"/><path d="M3 9h18M8 2.5v3M16 2.5v3"/>',
    desk:'<path d="M4 17l5-5 4 3 7-8"/><path d="M4 21h16"/>',
    share:'<path d="M12 3v12M7.5 7.5 12 3l4.5 4.5"/><path d="M5 12v7a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-7"/>',
    search:'<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
    close:'<path d="M6 6l12 12M18 6 6 18"/>'
  };
  var svg = function(k){ return '<svg viewBox="0 0 24 24" aria-hidden="true">'+I[k]+'</svg>'; };

  // ---- the parts ----
  var bar = document.createElement('div'); bar.id = 'ph-bar';
  bar.innerHTML = '<div class="ph-row"><button class="ph-ib" type="button" id="ph-share" aria-label="Share this edition">'+svg('share')+'</button>'
    + '<a class="ph-name" href="#" id="ph-top">Daily Newsletter</a>'
    + '<button class="ph-ib" type="button" id="ph-find" aria-label="Search the archive">'+svg('search')+'</button></div>'
    + '<nav class="ph-chips" id="ph-chips" aria-label="Sections"></nav><div class="ph-prog" id="ph-prog"></div>';
  var tabs = document.createElement('nav'); tabs.id = 'ph-tabs'; tabs.setAttribute('aria-label', 'Main');
  tabs.innerHTML = '<a href="#" id="ph-t-today" aria-current="true">'+svg('today')+'Today</a>'
    + '<button type="button" id="ph-t-sections">'+svg('sections')+'Sections</button>'
    + '<button type="button" id="ph-t-listen" aria-pressed="false">'+svg('listen')+'Listen</button>'
    + '<button type="button" id="ph-t-archive">'+svg('archive')+'Archive</button>'
    + '<a href="/desk/" id="ph-t-desk">'+svg('desk')+'Desk</a>';
  var sheet = document.createElement('div'); sheet.id = 'ph-sheet';
  sheet.innerHTML = '<div class="ph-scrim" id="ph-scrim"></div><div class="ph-panel" role="dialog" aria-modal="true" aria-labelledby="ph-sh-t">'
    + '<div class="ph-grab"></div><div class="ph-sh-h"><b id="ph-sh-t"></b><button class="ph-ib" type="button" id="ph-sh-x" aria-label="Close">'+svg('close')+'</button></div>'
    + '<div class="ph-sh-b" id="ph-sh-b"></div></div>';
  var toast = document.createElement('div'); toast.id = 'ph-toast'; toast.setAttribute('role', 'status');
  document.body.appendChild(bar); document.body.appendChild(tabs); document.body.appendChild(sheet); document.body.appendChild(toast);

  // ---- helpers ----
  function editionKey(){ var a = document.querySelector('#archList a.current'); return a ? a.getAttribute('href').slice(1) : ''; }
  function newestKey(){ var a = document.querySelector('#archList a'); return a ? a.getAttribute('href').slice(1) : ''; }
  var toastT;
  function say(html, action, fn){
    toast.innerHTML = '<span>'+html+'</span>' + (action ? '<button type="button">'+action+'</button>' : '');
    if(action) toast.querySelector('button').addEventListener('click', function(){ toast.classList.remove('on'); fn(); });
    toast.classList.add('on'); clearTimeout(toastT);
    if(!action) toastT = setTimeout(function(){ toast.classList.remove('on'); }, 2200);
  }

  // ---- sheets ----
  var archHome = null, lastFocus = null;
  function openSheet(title, fill){
    lastFocus = document.activeElement;
    $('ph-sh-t').textContent = title; $('ph-sh-b').innerHTML = ''; fill($('ph-sh-b'));
    sheet.classList.add('on'); document.body.style.overflow = 'hidden';
    setTimeout(function(){ $('ph-sh-x').focus(); }, 50);
  }
  function closeSheet(){
    if(!sheet.classList.contains('on')) return;
    sheet.classList.remove('on'); document.body.style.overflow = '';
    var arch = $('archive');
    if(archHome && arch && arch.parentNode !== archHome.parentNode){ archHome.parentNode.insertBefore(arch, archHome); arch.classList.remove('open'); }
    if(lastFocus && lastFocus.focus) lastFocus.focus();
  }
  $('ph-scrim').addEventListener('click', closeSheet);
  $('ph-sh-x').addEventListener('click', closeSheet);
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape') closeSheet(); });
  // drag the sheet down to close it
  (function(){
    var p = sheet.querySelector('.ph-panel'), y0 = null, dy = 0;
    p.addEventListener('touchstart', function(e){ if($('ph-sh-b').scrollTop > 0 && !e.target.closest('.ph-sh-h,.ph-grab')) return; y0 = e.touches[0].clientY; dy = 0; }, {passive:true});
    p.addEventListener('touchmove', function(e){ if(y0 === null) return; dy = Math.max(0, e.touches[0].clientY - y0); if(dy > 4){ p.style.transition = 'none'; p.style.transform = 'translateY('+dy+'px)'; } }, {passive:true});
    p.addEventListener('touchend', function(){ if(y0 === null) return; p.style.transition = ''; p.style.transform = ''; if(dy > 90) closeSheet(); y0 = null; });
  })();

  function sectionsSheet(){
    openSheet('In this edition', function(b){
      var cur = (document.querySelector('#ph-chips a[aria-current="true"]') || {}).hash;
      var list = document.createElement('div'); list.className = 'ph-list';
      var links = [].slice.call(document.querySelectorAll('#toc a'));
      var h = (document.getElementById('front') ? '<a href="#front">Front page</a>' : '') + links.map(function(a){
        var sec = document.querySelector(a.getAttribute('href')), n = sec ? sec.querySelectorAll('.s-body p > strong:first-child, .s-body li > strong:first-child, .s-body h3').length : 0;
        return '<a href="'+a.getAttribute('href')+'"'+(a.hash === cur ? ' aria-current="true"' : '')+'>'+a.textContent+(n > 1 ? ' <small>'+n+'</small>' : '')+'</a>';
      }).join('');
      list.innerHTML = h || '<p>No sections on this page.</p>';
      list.addEventListener('click', function(e){
        var a = e.target.closest('a'); if(!a) return; e.preventDefault(); closeSheet();
        var t = document.querySelector(a.getAttribute('href')); if(t) setTimeout(function(){ t.scrollIntoView({block:'start'}); }, 60);
      });
      b.appendChild(list);
      var lbl = document.createElement('p'); lbl.className = 'ph-lbl'; lbl.textContent = 'Look'; b.appendChild(lbl);
      var th = document.createElement('div'); th.className = 'ph-theme'; th.setAttribute('role', 'group'); th.setAttribute('aria-label', 'Look');
      var now = root.getAttribute('data-theme') || 'light';
      th.innerHTML = ['paper','light','dark'].map(function(k){ return '<button type="button" data-t="'+k+'" aria-pressed="'+(now === k)+'">'+k+'</button>'; }).join('');
      th.addEventListener('click', function(e){
        var bt = e.target.closest('button'); if(!bt) return; var want = bt.getAttribute('data-t'), btn = $('themeBtn'), n = 0;
        while((root.getAttribute('data-theme') || 'light') !== want && n++ < 3) btn.click();   // the page's own switch cycles light, dark, paper
        [].forEach.call(th.querySelectorAll('button'), function(x){ x.setAttribute('aria-pressed', x === bt); });
      });
      b.appendChild(th);
    });
  }
  function archiveSheet(focusSearch){
    openSheet('Archive', function(b){
      var pair = document.createElement('div'); pair.className = 'ph-pair';
      pair.innerHTML = ($('prev').innerHTML || '') + ($('next').innerHTML || '');
      b.appendChild(pair);
      var more = document.createElement('div'); more.className = 'ph-pair';
      more.innerHTML = '<a href="#topics">Topics</a><button type="button" class="ph-btn" aria-expanded="false">Puzzles</button>';
      b.appendChild(more);
      var pz = document.createElement('div'); pz.className = 'ph-puz'; pz.hidden = true; b.appendChild(pz);
      more.querySelector('button').addEventListener('click', function(){ var on = pz.hidden; pz.hidden = !on; this.setAttribute('aria-expanded', on); if(on) puzzleLists(pz); });
      var arch = $('archive'); if(!arch) return;
      if(!archHome){ archHome = document.createComment('archive'); arch.parentNode.insertBefore(archHome, arch); }
      arch.classList.add('open'); b.appendChild(arch);
      if(focusSearch) setTimeout(function(){ $('q').focus(); }, 320);
    });
  }
  // the archive's puzzles: a row for each game, every day's puzzle from the oldest on the left to the newest on the
  // right (scrolled to the newest), with the ones solved on this device ticked; from data/puzzles/index.json
  var LEVEL = ['Easy', 'Easy', 'Medium', 'Medium', 'Hard', 'Hard', 'Hardest'];
  function puzzleLists(box){
    if(box.dataset.done) return; box.dataset.done = '1';
    box.innerHTML = '<p class="ph-lbl">Loading the puzzles</p>';
    fetch('/data/puzzles/index.json', {cache:'no-cache'}).then(function(r){ if(!r.ok) throw 0; return r.json(); }).then(function(ix){
      var days = (ix.days || []).slice().sort(function(a, b){ return a.date < b.date ? -1 : 1; });
      function got(k){ try { return JSON.parse(localStorage.getItem(k)); } catch(e){ return null; } }
      function short(d){ return new Date(d + 'T12:00:00').toLocaleDateString('en-US', {weekday:'short', month:'short', day:'numeric'}); }
      function row(name, tab, sub, won){
        return '<p class="ph-lbl">' + name + '</p><div class="ph-puz-row">' + days.map(function(d){
          var w = won(d.date);
          return '<a href="/puzzles/?d=' + d.date + '#' + tab + '"' + (w ? ' class="won"' : '') + '><b>' + (d.no ? 'No. ' + d.no : '') + '</b><span>' + short(d.date) + '</span><small>' + (w ? '✓ Solved' : sub(d)) + '</small></a>';
        }).join('') + '</div>';
      }
      box.innerHTML = days.length ? row('Crossword', 'cw', function(d){ return d.size ? d.size + ' by ' + d.size : ''; }, function(dt){ var x = got('puz:cw:' + dt); return (x && x.won) || got('puz:cw:' + dt + ':won'); })
        + row('Killer sudoku', 'ks', function(d){ return d.level != null ? LEVEL[d.level] : ''; }, function(dt){ var x = got('puz:ks:' + dt); return x && x.won; })
        + row('The Globe', 'gl', function(){ return 'Find the country'; }, function(dt){ var x = got('puz:gl:' + dt); return x && x.won; })
        : '<p class="ph-lbl">No puzzles yet</p>';
      [].forEach.call(box.querySelectorAll('.ph-puz-row'), function(r){ r.scrollLeft = r.scrollWidth; });
    }).catch(function(){ box.innerHTML = '<p class="ph-lbl"><a href="/puzzles/">Open today\'s puzzles</a></p>'; box.dataset.done = ''; });
  }
  window.addEventListener('hashchange', closeSheet);

  // ---- tabs ----
  $('ph-t-today').addEventListener('click', function(e){
    e.preventDefault(); closeSheet();
    var nk = newestKey();
    if(nk && editionKey() !== nk){ location.hash = nk; return; }
    if(/^#(topics|topic\/)/.test(location.hash)){ location.hash = nk; return; }
    window.scrollTo({top:0, behavior:'smooth'});
  });
  $('ph-top').addEventListener('click', function(e){ e.preventDefault(); window.scrollTo({top:0, behavior:'smooth'}); });
  $('ph-t-sections').addEventListener('click', sectionsSheet);
  $('ph-t-archive').addEventListener('click', function(){ archiveSheet(false); });
  $('ph-find').addEventListener('click', function(){ archiveSheet(true); });
  $('ph-t-listen').addEventListener('click', function(){
    var pl = $('player');
    if(pl && !pl.hidden){ var pp = pl.querySelector('.pl-play'); if(pp){ pp.click(); return; } }
    var b = $('listenBtn'); if(b) b.click(); else say('No audio for this edition yet');
  });
  $('ph-share').addEventListener('click', function(){
    var k = editionKey(), url = location.origin + location.pathname + (k ? '#' + k : '');
    var t = document.title;
    if(navigator.share) navigator.share({title:t, url:url}).catch(function(){});
    else if(navigator.clipboard) navigator.clipboard.writeText(url).then(function(){ say('Link copied'); });
  });
  // the Listen tab shows when audio is playing
  new MutationObserver(function(){ $('ph-t-listen').setAttribute('aria-pressed', document.body.classList.contains('listening')); })
    .observe(document.body, {attributes:true, attributeFilter:['class']});

  // ---- the following bar: shown once the masthead's chips scroll away; its chips follow the section you are in ----
  var targets = [];
  function buildChips(){
    var c = $('ph-chips'), links = [].slice.call(document.querySelectorAll('#toc a'));
    c.innerHTML = (document.getElementById('front') ? '<a href="#front">Front</a>' : '') + links.map(function(a){ return '<a href="'+a.getAttribute('href')+'">'+a.textContent+'</a>'; }).join('');
    c.hidden = !links.length;
    targets = [].slice.call(c.querySelectorAll('a')).map(function(a){ return [a, document.querySelector(a.getAttribute('href'))]; }).filter(function(x){ return x[1]; });
    tick();
  }
  $('ph-chips').addEventListener('click', function(e){
    var a = e.target.closest('a'); if(!a) return; e.preventDefault();
    var t = document.querySelector(a.getAttribute('href')); if(t) t.scrollIntoView({block:'start'});
  });
  var lastCur = null, ticking = false;
  function tick(){
    ticking = false; if(!mq.matches) return;
    var toc = $('toc'), mast = document.querySelector('.mast');
    var edge = toc && !toc.hidden && toc.offsetHeight ? toc.getBoundingClientRect().bottom : (mast ? mast.getBoundingClientRect().bottom : 0);
    bar.classList.toggle('on', edge < 0 && !sheet.classList.contains('on'));
    var h = document.documentElement.scrollHeight - innerHeight;
    $('ph-prog').style.setProperty('--p', h > 0 ? Math.min(1, scrollY / h) : 0);
    var cur = null;
    for(var i = 0; i < targets.length; i++){ if(targets[i][1].getBoundingClientRect().top < 140) cur = targets[i][0]; }
    if(cur !== lastCur){
      if(lastCur) lastCur.removeAttribute('aria-current');
      if(cur){ cur.setAttribute('aria-current', 'true'); var c = $('ph-chips'); c.scrollTo({left: cur.offsetLeft - 16, behavior:'smooth'}); }
      lastCur = cur;
    }
  }
  window.addEventListener('scroll', function(){ if(!ticking){ ticking = true; requestAnimationFrame(tick); } }, {passive:true});
  window.addEventListener('resize', tick);
  var toc = $('toc');
  if(toc) new MutationObserver(function(){ lastCur = null; setTimeout(buildChips, 0); }).observe(toc, {childList:true, attributes:true, attributeFilter:['hidden']});
  new MutationObserver(function(){ setTimeout(buildChips, 0); }).observe($('content'), {childList:true});

  // ---- swipe sideways on the page to go to the older or newer edition ----
  (function(){
    var x0, y0, t0, ok;
    function scrollsSideways(el){
      for(; el && el !== document.body; el = el.parentElement){
        if(el.scrollWidth > el.clientWidth + 2){ var o = getComputedStyle(el).overflowX; if(o === 'auto' || o === 'scroll') return true; }
        if(el.id === 'player' || el.id === 'ph-tabs' || el.id === 'ph-bar') return true;
      }
      return false;
    }
    document.addEventListener('touchstart', function(e){
      ok = mq.matches && e.touches.length === 1 && !sheet.classList.contains('on') && !/^#topic/.test(location.hash);
      if(!ok) return;
      var t = e.touches[0]; x0 = t.clientX; y0 = t.clientY; t0 = Date.now();
      if(x0 < 24 || x0 > innerWidth - 24 || scrollsSideways(e.target)) ok = false;
      if(window.getSelection && String(window.getSelection())) ok = false;
    }, {passive:true});
    document.addEventListener('touchend', function(e){
      if(!ok) return; ok = false;
      var t = e.changedTouches[0], dx = t.clientX - x0, dy = t.clientY - y0;
      if(Date.now() - t0 > 700 || Math.abs(dx) < 90 || Math.abs(dy) > Math.abs(dx) * 0.45) return;
      // older editions lie to the left and newer ones to the right (as the Older and Newer buttons): swiping left
      // brings in the newer edition, swiping right the older one
      var a = (dx < 0 ? $('next') : $('prev')).querySelector('a');
      if(!a){ say(dx < 0 ? 'This is the newest edition' : 'This is the oldest edition'); return; }
      var c = $('content'); c.classList.add('ph-swiping'); c.style.transform = 'translateX('+(dx < 0 ? -40 : 40)+'px)'; c.style.opacity = '.3';
      setTimeout(function(){ location.hash = a.getAttribute('href').slice(1); window.scrollTo(0, 0); c.style.transform = ''; c.style.opacity = ''; setTimeout(function(){ c.classList.remove('ph-swiping'); }, 250); }, 160);
      say(dx < 0 ? 'Newer edition →' : '← Older edition');
    }, {passive:true});
  })();

  // ---- a newer edition: checked when you come back to the page (a home-screen app can stay open for days) ----
  var hiddenAt = 0, offered = '';
  function checkNew(){
    var have = newestKey(); if(!have) return;
    fetch('editions/index.json', {cache:'no-cache'}).then(function(r){ return r.json(); }).then(function(d){
      var keys = (d.editions || []).map(function(e){ return e.id || e.date; }).sort(); var top = keys[keys.length - 1];
      if(top && top > have && top !== offered){
        offered = top;
        var label = /recap/.test(top) ? 'The Weekly Recap is out' : 'A new edition is out';
        say(label, 'Read it', function(){ location.href = location.pathname; });
      }
    }).catch(function(){});
  }
  document.addEventListener('visibilitychange', function(){
    if(document.hidden){ hiddenAt = Date.now(); return; }
    if(hiddenAt && Date.now() - hiddenAt > 10 * 60 * 1000) checkNew();
  });
  setInterval(function(){ if(!document.hidden && mq.matches) checkNew(); }, 30 * 60 * 1000);

  mq.addEventListener ? mq.addEventListener('change', tick) : mq.addListener(tick);
  buildChips();
})();
