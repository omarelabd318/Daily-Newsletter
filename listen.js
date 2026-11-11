/* The newsletter read aloud. Two voices:
   - recorded: a natural voice made with each edition (data/audio/KEY.json names the MP3 and when each block starts);
   - this device: the browser's own text-to-speech, for any edition, with the device's voices to choose from.
   The blocks are the ones read_aloud.py reads (.claude/skills/daily-newsletter): every section but Sources and the two watch tables, its
   headings, paragraphs and list items; tables are skipped, and so is a section that is only tables. */
(function(){
  'use strict';
  var $ = function(id){ return document.getElementById(id); };
  var store = { get: function(k){ try { return localStorage.getItem(k); } catch(e){ return null; } },
                set: function(k, v){ try { localStorage.setItem(k, v); } catch(e){} } };
  var synth = window.speechSynthesis || null;

  // ---- figures and abbreviations as they are said (the same rules as read_aloud.py's speakable) ----
  var MONTHS = {Jan:'January',Feb:'February',Mar:'March',Apr:'April',Jun:'June',Jul:'July',Aug:'August',Sep:'September',Sept:'September',Oct:'October',Nov:'November',Dec:'December'};
  var UNITS = {tn:'trillion',bn:'billion',mn:'million',m:'million',k:'thousand'};
  var WORDS = [['Sisi','Seesee'],['YTD','year to date'],['YoY','year on year'],['EGX30','E G X thirty'],['EGX70','E G X seventy'],['EGX100','E G X one hundred'],
    ['S&P 500','S and P 500'],['S&P','S and P'],['CBE','C B E'],['IMF','I M F'],['GDP','G D P'],['OPEC+','OPEC plus'],
    ['Q1','the first quarter'],['Q2','the second quarter'],['Q3','the third quarter'],['Q4','the fourth quarter']];
  var SAY = /^(NATO|OPEC|NASA|FIFA|UEFA|COVID|ASEAN|BRICS|SWIFT|LIBOR|SOFR|MENA|NEOM|AFCON|AIDS|IKEA|LEGO|ISIS|CAPMAS|UNICEF|UNESCO|SIM|PIN|LASER|RAM|GIF)$/;
  var NUM = '(\\d+(?:,\\d{3})*(?:\\.\\d+)?)';   // 76,000 or 4.5, never a comma after it
  function esc(re){ return re.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }
  function speakable(t){
    t = t.replace(new RegExp('\\bEGP\\s?' + NUM + '(?:\\s?(tn|bn|mn|m|k)\\b|\\s(trillion|billion|million|thousand)\\b)?', 'g'), function(m, n, u, w){ return n + (u ? ' ' + UNITS[u] : w ? ' ' + w : '') + ' pounds'; });
    t = t.replace(new RegExp('\\$' + NUM + '\\s?(tn|bn|mn|m|k)\\b', 'g'), function(m, n, u){ return n + ' ' + UNITS[u] + ' dollars'; });
    t = t.replace(new RegExp('\\$' + NUM + '(?:\\s(trillion|billion|million|thousand))?', 'g'), function(m, n, u){ return n + (u ? ' ' + u : '') + ' dollars'; });
    // other currencies (the same rule as read_aloud.py): EUR 4.10 -> 4.1 euros
    var CUR = {EUR:'euros','€':'euros',GBP:'pounds sterling','£':'pounds sterling',AED:'dirhams',SAR:'riyals',QAR:'riyals',KWD:'dinars'};
    t = t.replace(new RegExp('(?:\\b(EUR|GBP|AED|SAR|QAR|KWD)\\s?|([€£]))' + NUM + '(?:\\s?(tn|bn|mn|m|k)\\b|\\s(trillion|billion|million|thousand)\\b)?', 'g'), function(m, c, s2, n, u, w){ return n.replace(/(\.\d*?)0+$/, '$1').replace(/\.$/, '') + (u ? ' ' + UNITS[u] : w ? ' ' + w : '') + ' ' + CUR[c || s2]; });
    t = t.replace(/(\d)-a-(share|day|year|month|week|barrel|ton|tonne|gram|head|night)\b/g, '$1 a $2');
    t = t.replace(new RegExp('\\b' + NUM + '\\s?bps?\\b', 'g'), '$1 basis points');
    t = t.replace(new RegExp(NUM + '\\s?%', 'g'), '$1 percent');
    t = t.replace(/\s?°C\b/g, ' degrees');
    t = t.replace(/\b(\d{1,2}(?::\d\d)?)\s?(am|pm)\b/g, function(m, h, ap){ return h + (ap === 'am' ? ' a.m.' : ' p.m.'); });
    t = t.replace(/(\d)\s?[–—-]\s?(\d)/g, '$1 to $2');
    t = t.replace(/\b(\d{1,2}) (Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\b/g, '$2 $1');
    t = t.replace(/(^|[^\w.])([+−-])(\d)/g, function(m, pre, s, d){ return pre + (s === '+' ? 'plus ' : 'minus ') + d; });
    Object.keys(MONTHS).forEach(function(k){ t = t.replace(new RegExp('\\b' + k + '\\.?(?= \\d)', 'g'), MONTHS[k]); });
    WORDS.forEach(function(w){ t = t.replace(new RegExp('(^|[^\\w&])' + esc(w[0]) + '(?![\\w&])', 'g'), '$1' + w[1]); });
    // short all-caps abbreviations are spelled out (IPO, CIB, US, AI), except those said as words (NATO, OPEC)
    t = t.replace(/\b[A-Z]{2,5}\b/g, function(w){ return SAY.test(w) || /^(?:X{0,3})(?:IX|IV|V?I{0,3})$/.test(w) ? w : w.split('').join(' '); });
    return t.replace(/&/g, ' and ').replace(/\//g, ' ').replace(/·/g, ',').replace(/→/g, '').replace(/\s+/g, ' ').trim();
  }

  // ---- the edition's blocks, in reading order ----
  var SKIP = /^(Stocks Watch|Stocks This Week|Currency and Commodities Watch)$/i;   // tables: read on the page
  function blocks(intro){
    var out = intro ? [{sec: '', n: 0, kind: 'title', el: null, text: intro}] : [];
    [].forEach.call(document.querySelectorAll('#content section.s:not(.src)'), function(sec){
      var h2 = sec.querySelector('h2'), title = h2 ? h2.textContent.trim() : '';
      if(SKIP.test(title)) return;
      var els = [].filter.call(sec.querySelectorAll('.s-body h3, .s-body h4, .s-body p, .s-body li, .s-body blockquote'), function(el){
        if(el.closest('table, .tablewrap, .pbar, .sp, details, .topics') || el.classList.contains('deskline')) return false;
        if(el.tagName === 'P' && el.closest('li, blockquote')) return false;   // a list item is read whole
        return true;
      });
      var items = [], sub = '';
      els.forEach(function(el){
        var c = el.cloneNode(true);
        [].forEach.call(c.querySelectorAll('.topics, svg, sup, .chg'), function(x){ x.remove(); });
        var text = c.textContent.replace(/\s+/g, ' ').trim();
        if(!text) return;
        var kind = /^H[34]$/.test(el.tagName) ? 'heading' : 'text', f = el.firstElementChild;
        if(kind === 'heading') sub = text;
        var lead = kind === 'text' && f && f.tagName === 'STRONG' && el.firstChild === f ? f.textContent.replace(/[:.]\s*$/, '').trim() : '';
        items.push({el: el, kind: kind, text: text, story: lead || sub});
      });
      // a subhead with no text under it (Stocks Watch's "Egypt" over a table) is skipped
      items = items.filter(function(b, i){ if(b.kind !== 'heading') return true; var nx = items[i + 1]; return nx && nx.kind === 'text'; });
      if(!items.some(function(b){ return b.kind === 'text'; })) return;
      var n = 0;
      out.push({sec: title, n: n++, kind: 'section', el: h2, text: title});
      items.forEach(function(b){ b.sec = title; b.n = n++; out.push(b); });
    });
    return out;
  }

  // ---- words: each block's words on the page (as ranges, for the word highlight and for clicks), and how the
  // spoken words (figures written out: "3.9 percent", "E G X thirty") line up with them ----
  // a word's key for matching the spoken words to the page; a name respelled for the voice (Seesee) keys as written (Sisi)
  function wkey(w){ return w.toLowerCase().replace(/[^a-z0-9]/g, '').replace(/seesee/g, 'sisi'); }
  // each word is wrapped in its own <span> when the block is first read (the text looks the same), and the word being
  // said gets a class: a plain style change, which every browser redraws (Safari did not always redraw a text highlight)
  function domWords(b){
    if(b.dw) return b.dw;
    var out = [];
    if(b.el){
      var walk = document.createTreeWalker(b.el, NodeFilter.SHOW_TEXT, {acceptNode: function(n){
        return n.parentElement && n.parentElement.closest('.topics, svg, sup, .chg, .w') ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT; }});
      var nodes = [], n;
      while((n = walk.nextNode())) nodes.push(n);
      // "EGP 54.01" is one word on the page, said as "54.01 pounds"
      var re = /(?:EGP|US\$)\s+\d\S*|\S+/g;
      nodes.forEach(function(n){
        var t = n.data, m, last = 0, frag = document.createDocumentFragment();
        re.lastIndex = 0;
        while((m = re.exec(t))){
          if(m.index > last) frag.appendChild(document.createTextNode(t.slice(last, m.index)));
          var sp = document.createElement('span'); sp.className = 'w'; sp.textContent = m[0]; frag.appendChild(sp);
          out.push({el: sp, k: wkey(m[0].replace(/^(EGP|US\$)\s+/, ''))});
          last = m.index + m[0].length;
        }
        if(last < t.length) frag.appendChild(document.createTextNode(t.slice(last)));
        if(n.parentNode) n.parentNode.replaceChild(frag, n);
      });
    }
    return (b.dw = out);
  }
  var UNITW = /^(percent|pounds?|dollars?|degrees|basis|points|million|billion|trillion|thousand|am|pm)$/;
  function same(a, b){
    if(a === b) return true;
    return a.length >= 3 && b.length >= 3 && (a.indexOf(b) === 0 || b.indexOf(a) === 0);
  }
  // spoken word -> page word: each spoken word that matches one a little ahead moves the place on; the others (units,
  // spelled-out letters) stay with the figure they belong to or go to the next word
  function align(spoken, dw){
    var map = [], cur = -1, miss = 0;
    for(var s = 0; s < spoken.length; s++){
      var k = wkey(spoken[s]), found = -1;
      // a range or score on the page ("3-2", "7-6(5)", "2026-27") is said "3 to 2": the three spoken words are that one page word
      if(/^\d+$/.test(k) && wkey(spoken[s + 1] || '') === 'to' && /^\d/.test(wkey(spoken[s + 2] || ''))){
        var kk = k + wkey(spoken[s + 2]);
        for(var j2 = cur + 1; j2 < Math.min(dw.length, cur + 4 + miss); j2++) if(dw[j2].k === kk){ map[s] = map[s + 1] = map[s + 2] = cur = j2; miss = 0; found = j2; break; }
        if(found >= 0){ s += 2; continue; }
      }
      // a unit said after a figure ("98.29 dollars", "3.9 percent") stays on the figure
      // (unless the page says it too: "$125 million", "100 basis points")
      var prev = s ? map[s - 1] : -1;
      if(prev >= 0 && UNITW.test(k) && /\d|^(million|billion|trillion|thousand)$/.test(dw[prev].k) && !(dw[prev + 1] && same(k, dw[prev + 1].k))){ map[s] = prev; continue; }
      // a short word ("to", "a") only matches the next word or the one after, so it cannot jump ahead past real words;
      // after a run of spoken words with no match on the page (a score read as "3 to 6, 6 to 4") the search reaches further
      if(k) for(var j = cur + 1; j < Math.min(dw.length, cur + (k.length <= 3 ? 3 : 7) + miss); j++) if(same(k, dw[j].k)){ found = j; break; }
      if(found >= 0){ cur = found; miss = 0; } else miss++;
      map[s] = found >= 0 ? found : cur >= 0 && /\d/.test(dw[cur].k) ? cur : Math.min(cur + 1, dw.length - 1);
    }
    return map;
  }
  var wordAt = null;
  function markWord(b, d){
    if(S && b) S.at = d;
    var dw = b ? domWords(b) : [], el = d != null && d >= 0 && dw[d] ? dw[d].el : null;
    if(el === wordAt) return;
    if(wordAt) wordAt.classList.remove('w-on');
    wordAt = el;
    if(el) el.classList.add('w-on');
  }

  // ---- voices on this device: English ones, the natural-sounding first; the novelty voices left out ----
  var JUNK = /^(Albert|Bad News|Bahh|Bells|Boing|Bubbles|Cellos|Good News|Jester|Organ|Superstar|Trinoids|Whisper|Wobble|Zarvox|Junior|Ralph|Fred|Kathy|Grandma|Grandpa|Rocko|Shelley|Eddy|Flo|Reed|Sandy)\b/;
  function deviceVoices(){
    if(!synth) return [];
    var score = function(v){ var n = v.name; return (/Premium/i.test(n) ? 6 : /Enhanced|Natural|Neural/i.test(n) ? 5 : /Google|Siri/i.test(n) ? 3 : 0) + (/^en[-_]US/i.test(v.lang) ? 1 : 0); };
    return synth.getVoices().filter(function(v){ return /^en/i.test(v.lang) && !JUNK.test(v.name); })
      .sort(function(a, b){ return score(b) - score(a) || (a.name < b.name ? -1 : 1); });
  }

  // ---- state ----
  var S = null;   // {key, list, i, playing, mode: 'rec'|'dev', rec: manifest or null, audio, rate, voice}
  var RATES = [0.85, 1, 1.15, 1.3, 1.5];

  function fmt(s){ s = Math.max(0, Math.round(s)); return Math.floor(s / 60) + ':' + ('0' + s % 60).slice(-2); }
  function words(list){ return list.reduce(function(a, b){ return a + b.text.split(/\s+/).length; }, 0); }

  function bar(){
    var p = $('player');
    if(p) return p;
    p = document.createElement('div'); p.id = 'player'; p.hidden = true; p.setAttribute('role', 'region'); p.setAttribute('aria-label', 'Listen to this edition');
    // left: what is being read; middle: the controls over the progress bar; right: speed, voice, close
    p.innerHTML = '<div class="pl-in">'
      + '<div class="pl-l"><b id="plSec"></b></div>'
      + '<div class="pl-ctl">'
      + '<button type="button" class="pl-b" data-a="prev" aria-label="Previous section"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 5h2v14H6zM20 5v14L9 12z"/></svg></button>'
      + '<button type="button" class="pl-b pl-play" data-a="play" aria-label="Pause"></button>'
      + '<button type="button" class="pl-b" data-a="next" aria-label="Next section"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16 5h2v14h-2zM4 5v14l11-7z"/></svg></button>'
      + '</div>'
      + '<div class="pl-prog"><span id="plCur"></span><input id="plSeek" type="range" min="0" max="1000" value="0" aria-label="Position"><span id="plDur"></span></div>'
      + '<div class="pl-r"><select id="plRate" aria-label="Speed">' + RATES.map(function(r){ return '<option value="' + r + '"' + (r === 1 ? ' selected' : '') + '>' + r + '×</option>'; }).join('') + '</select>'
      + '<div class="pl-rr"><select id="plVoice" aria-label="Voice"></select>'
      + '<button type="button" class="pl-b pl-x" data-a="close" aria-label="Stop listening"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.4 5 5 6.4 10.6 12 5 17.6 6.4 19 12 13.4 17.6 19 19 17.6 13.4 12 19 6.4 17.6 5 12 10.6z"/></svg></button></div></div>'
      + '</div><button type="button" class="pl-back" id="plBack" hidden></button>';
    document.body.appendChild(p);
    $('plBack').addEventListener('click', function(){ if(lastEl) lastEl.scrollIntoView({block: 'center', behavior: 'smooth'}); });
    p.addEventListener('click', function(e){
      var b = e.target.closest('[data-a]'); if(!b || !S) return;
      var a = b.getAttribute('data-a');
      if(a === 'play') S.playing ? pause() : play();
      else if(a === 'prev') jumpSection(-1);
      else if(a === 'next') jumpSection(1);
      else if(a === 'close') stop();
    });
    $('plRate').addEventListener('change', function(){ if(!S) return; S.rate = +this.value; store.set('nl:rate', this.value); if(S.mode === 'rec') S.audio.playbackRate = S.rate; else if(S.playing){ speakFrom(S.i); } });
    $('plVoice').addEventListener('change', function(){ if(!S) return; var v = this.value; store.set('nl:voice', v); var was = S.playing, at = S.i; halt(); choose(v); if(was){ S.i = at; play(); } else paint(); });
    $('plSeek').addEventListener('input', function(){
      if(!S) return;
      var f = this.value / 1000; this.style.setProperty('--p', (this.value / 10) + '%');
      if(S.mode === 'rec' && S.audio.duration) S.audio.currentTime = f * S.audio.duration;
      else { S.i = Math.min(S.list.length - 1, Math.floor(f * S.list.length)); if(S.playing) speakFrom(S.i); else paint(); }
    });
    return p;
  }

  function fillVoices(){
    var sel = $('plVoice'); if(!sel || !S) return;
    var html = '';
    // an edition with recorded voices offers only those; the device's voices are for the editions without
    if(S.rec) html += S.rec.voices.map(function(v){ return '<option value="rec:' + v.voice + '">' + v.name + '</option>'; }).join('');
    var dv = deviceVoices();
    if(!S.rec && dv.length) html += '<optgroup label="This device">' + dv.map(function(v){ return '<option value="dev:' + v.voiceURI.replace(/"/g, '&quot;') + '">' + v.name.replace(/</g, '') + '</option>'; }).join('') + '</optgroup>';
    sel.innerHTML = html || '<option>No voice available</option>';
    sel.value = (S.mode === 'rec' ? 'rec:' + S.recVoice.voice : 'dev:' + (S.voice ? S.voice.voiceURI : ''));
  }

  // pick the voice: one saved before if this edition has it, else the natural voice, else the device's best
  function choose(want){
    var dv = deviceVoices();
    S.audio && S.audio.pause();
    if(want && want.indexOf('rec:') === 0 && S.rec){
      var r = S.rec.voices.filter(function(v){ return 'rec:' + v.voice === want; })[0] || S.rec.voices[0];
      S.mode = 'rec'; S.recVoice = r;
      if(!S.audio || S.audio.getAttribute('data-src') !== r.url){
        if(S.audio) S.audio.pause();
        S.audio = new Audio(); S.audio.preload = 'metadata'; S.audio.src = r.url; S.audio.setAttribute('data-src', r.url);
        S.audio.addEventListener('timeupdate', onTime); S.audio.addEventListener('ended', function(){ S && (S.playing = false, paint()); });
        S.audio.addEventListener('error', function(){ if(S && S.mode === 'rec'){ S.rec = null; choose('dev:'); fillVoices(); if(S.playing) play(); } });
      }
      S.audio.playbackRate = S.rate;
      return;
    }
    S.mode = 'dev';
    var id = want && want.indexOf('dev:') === 0 ? want.slice(4) : '';
    S.voice = dv.filter(function(v){ return v.voiceURI === id; })[0] || dv[0] || null;
  }

  // ---- highlight and follow ----
  var lastEl = null;
  function mark(el){
    if(el === lastEl) return;
    var follow = lastEl ? (function(r){ return r.bottom > 0 && r.top < innerHeight; })(lastEl.getBoundingClientRect()) : true;
    if(lastEl) lastEl.classList.remove('reading');
    lastEl = el; markWord(null);
    if(!el){ backBtn(); return; }
    el.classList.add('reading');
    var r = el.getBoundingClientRect();
    if(follow && (r.top < 80 || r.bottom > innerHeight - 110)) el.scrollIntoView({block: 'center', behavior: 'smooth'});
    else backBtn();
  }
  // scrolled away from the block being read: a button above the bar goes back to it
  function backBtn(){
    var b = $('plBack'); if(!b) return;
    var off = '';
    if(S && lastEl){ var r = lastEl.getBoundingClientRect(), bar = $('player').getBoundingClientRect().top; off = r.bottom < 0 ? 'up' : r.top > bar ? 'down' : ''; }
    b.hidden = !off;
    if(off) b.innerHTML = '<span aria-hidden="true">' + (off === 'up' ? '↑' : '↓') + '</span> Back to where it\u2019s reading';
  }
  var ticking = false;
  window.addEventListener('scroll', function(){ if(!S || ticking) return; ticking = true; requestAnimationFrame(function(){ ticking = false; backBtn(); }); }, {passive: true});
  function seekTo(v){ var e = $('plSeek'); e.value = v; e.style.setProperty('--p', (v / 10) + '%'); }
  function paint(){
    if(!S) return;
    var b = S.list[S.i] || {};
    var head = (b.sec || 'Daily Newsletter').replace(/</g, '&lt;'), story = b.story && b.story !== b.sec ? b.story.replace(/</g, '&lt;') : '';
    $('plSec').innerHTML = '<strong>' + head + '</strong>' + (story ? ' · ' + story : '');
    $('plSec').title = $('plSec').textContent;
    var btn = document.querySelector('#player .pl-play');
    btn.innerHTML = S.playing ? '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5h4v14H7zM13 5h4v14h-4z"/></svg>' : '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5v14l12-7z"/></svg>';
    btn.setAttribute('aria-label', S.playing ? 'Pause' : 'Play');
    if(S.mode === 'rec'){
      var d = S.audio.duration || S.recVoice.duration || 0, t = S.audio.currentTime || 0;
      $('plCur').textContent = fmt(t / S.rate); $('plDur').textContent = fmt(d / S.rate);
      seekTo(d ? Math.round(t / d * 1000) : 0);
    } else {
      var left = words(S.list.slice(S.i)) / (165 * S.rate) * 60;
      $('plCur').textContent = ''; $('plDur').textContent = 'About ' + Math.max(1, Math.round(left / 60)) + ' min left';
      seekTo(Math.round(S.i / S.list.length * 1000));
    }
    mark(b.el || null);
    if('mediaSession' in navigator){
      try { navigator.mediaSession.playbackState = S.playing ? 'playing' : 'paused'; } catch(e){}
    }
  }

  // ---- recorded voice: the manifest gives each block's start time ----
  function onTime(){
    if(!S || S.mode !== 'rec') return;
    var t = S.audio.currentTime, seg = S.recVoice.segments, k = 0;
    while(k + 1 < seg.length && seg[k + 1].t <= t + 0.05) k++;
    var s = seg[k];
    if(s){ var idx = indexOf(s.sec, s.n); if(idx >= 0) S.i = idx; }
    paint();
    var b = S.list[S.i];
    if(s && s.w && s.w.length && b){
      if(!s.map) s.map = align(s.w.map(function(x){ return x[1]; }), domWords(b));
      var wi = -1, rel = (t - s.t) * 100;
      while(wi + 1 < s.w.length && s.w[wi + 1][0] <= rel + 4) wi++;
      markWord(b, wi >= 0 ? s.map[wi] : null);
    }
  }
  function segOf(i){
    var b = S.list[i], seg = S.recVoice.segments;
    for(var k = 0; k < seg.length; k++) if(seg[k].sec === b.sec && seg[k].n === b.n) return seg[k];
    return null;
  }
  function indexOf(sec, n){ for(var i = 0; i < S.list.length; i++) if(S.list[i].sec === sec && S.list[i].n === n) return i; return -1; }
  function timeOf(i){
    var b = S.list[i], seg = S.recVoice.segments;
    for(var k = 0; k < seg.length; k++) if(seg[k].sec === b.sec && seg[k].n === b.n) return seg[k].t;
    return null;
  }

  // ---- device voice: one sentence at a time (long utterances stop early in some browsers) ----
  var token = 0;
  function sentences(t){
    // a sentence ends at . ! or ? followed by a space and a capital, a digit or a quote (so not inside 54.01 or a.m.)
    var out = [], re = /\S.*?(?:[.!?]+["”’)]*(?=\s+[A-Z0-9"“‘(])|$)/g, m;
    while((m = re.exec(t)) && m[0]){
      var p = m[0], off = m.index + (p.length - p.replace(/^\s+/, '').length);
      p = p.trim(); if(!p) continue;
      while(p.length > 220){
        var cut = p.lastIndexOf(',', 220); cut = cut > 80 ? cut + 1 : 220;
        out.push({t: p.slice(0, cut), off: off});
        var rest = p.slice(cut); off += cut + (rest.length - rest.replace(/^\s+/, '').length); p = rest.trim();
      }
      if(p) out.push({t: p, off: off});
    }
    return out;
  }
  // the block's spoken words with where each starts in the spoken text, and their page words
  function spokenWords(b){
    if(b.sw) return b.sw;
    var sw = [], re = /\S+/g, m, text = speakable(b.text);
    while((m = re.exec(text))) sw.push({w: m[0], at: m.index});
    sw.text = text; sw.map = align(sw.map(function(x){ return x.w; }), domWords(b));
    return (b.sw = sw);
  }
  // characters a second the device voice speaks at 1x, learned from each sentence it finishes (for voices that do not
  // report each word, the highlight moves at this pace instead)
  var CPS = 14;
  function speakFrom(i, fromWord){
    if(!synth) return;
    var my = ++token;
    // stop only what is still speaking (a tap, a skip): moving on to the next paragraph needs no stop, and a stop is
    // what makes Safari drop the next sentence
    var busy = synth.speaking || synth.pending;
    if(busy) synth.cancel();
    S.i = i; paint();
    var b = S.list[i]; if(!b){ S.playing = false; paint(); return; }
    var sw = spokenWords(b), base = fromWord && sw[fromWord] ? sw[fromWord].at : 0;
    var parts = sentences(sw.text.slice(base)), k = 0, timer = null;
    if(fromWord) markWord(b, sw.map[fromWord]);
    var wordAt = function(at){ var wi = 0; while(wi + 1 < sw.length && sw[wi + 1].at <= at) wi++; return wi; };
    var next = function(){
      clearInterval(timer);
      if(my !== token || !S) return;
      if(k >= parts.length){
        setTimeout(function(){ if(my === token && S && S.playing) speakFrom(i + 1); }, b.kind === 'text' ? 250 : 450);
        return;
      }
      say(parts[k++], 0);
    };
    var say = function(part, tries){
      var u = new SpeechSynthesisUtterance(part.t), started = 0, sent = Date.now(), heard = false;
      if(S.voice){ u.voice = S.voice; u.lang = S.voice.lang; } else u.lang = 'en-US';
      u.rate = S.rate;
      u.onstart = function(){
        if(my !== token) return;
        started = Date.now();
        markWord(b, sw.map[wordAt(base + part.off)]);
        // no word reports from this voice: move the highlight at its speaking pace
        clearInterval(timer);
        timer = setInterval(function(){
          if(my !== token || !S || !S.playing){ clearInterval(timer); return; }
          if(heard) return;
          var c = (Date.now() - started) / 1000 * CPS * S.rate;
          if(c < part.t.length) markWord(b, sw.map[wordAt(base + part.off + c)]);
        }, 120);
      };
      // the word being said, where the voice reports it (most do; some do not, or stop after a restart)
      u.onboundary = function(e){
        if(my !== token || (e.name && e.name !== 'word')) return;
        heard = true;
        markWord(b, sw.map[wordAt(base + part.off + e.charIndex)]);
      };
      u.onend = function(){
        if(my !== token) return;
        // Safari can drop a sentence spoken straight after a cancel and report it finished at once: say it again
        if(!started && Date.now() - sent < 250 && tries < 2){ setTimeout(function(){ if(my === token) say(part, tries + 1); }, 200); return; }
        var secs = started ? (Date.now() - started) / 1000 : 0;
        if(secs > 1 && part.t.length > 20){ var c = part.t.length / secs / S.rate; if(c > 6 && c < 30) CPS = CPS * 0.6 + c * 0.4; }
        next();
      };
      u.onerror = function(e){ if(my === token && e.error !== 'interrupted' && e.error !== 'canceled') next(); };
      synth.speak(u);
    };
    // after a stop, a short pause first: speaking at once is what Safari drops
    if(busy) setTimeout(function(){ if(my === token && S) next(); }, 150); else next();
  }

  // ---- the space bar plays and pauses while the player is open (not while typing, or on a focused button,
  // which the space bar already presses) ----
  // the arrow keys skip back or forward 10 seconds, and with Shift to the previous or next paragraph
  document.addEventListener('keydown', function(e){
    if(!S || e.ctrlKey || e.metaKey || e.altKey || !/^( |ArrowLeft|ArrowRight)$/.test(e.key)) return;
    var t = e.target;
    if(t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName))) return;
    if(e.key === ' ' && t && /^(BUTTON|A|SUMMARY)$/.test(t.tagName)) return;
    e.preventDefault();   // not the page scroll
    if(e.key === ' ') S.playing ? pause() : play();
    else if(e.shiftKey) jumpBlock(e.key === 'ArrowLeft' ? -1 : 1);
    else skip(e.key === 'ArrowLeft' ? -10 : 10);
  });
  // 10 seconds of the recording; with the device voice, about as much text (it has no clock to seek)
  function skip(secs){
    if(S.mode === 'rec'){
      var d = S.audio.duration || S.recVoice.duration || 0;
      S.audio.currentTime = Math.max(0, Math.min(d ? d - 0.5 : Infinity, S.audio.currentTime + secs));
      paint(); return;
    }
    var b = S.list[S.i], sw = spokenWords(b), wi = 0;
    var cur = 0; if(S.at != null){ for(var k = 0; k < sw.length; k++) if(sw.map[k] >= S.at){ cur = sw[k].at; break; } }
    var to = cur + secs * CPS * S.rate;
    if(to < 0){ if(S.i > 0){ S.playing = true; speakFrom(S.i - 1); } else { S.playing = true; speakFrom(S.i); } return; }
    if(to >= sw.text.length){ if(S.i + 1 < S.list.length){ S.playing = true; speakFrom(S.i + 1); } return; }
    while(wi + 1 < sw.length && sw[wi + 1].at <= to) wi++;
    S.playing = true; speakFrom(S.i, wi);
  }
  function jumpBlock(dir){
    var i = Math.max(0, Math.min(S.list.length - 1, S.i + dir));
    if(i === S.i) return;
    S.i = i;
    if(S.mode === 'rec'){ var t = timeOf(i); if(t != null) S.audio.currentTime = t; paint(); }
    else if(S.playing) speakFrom(i); else paint();
  }

  // ---- tap a word to read from there (while the player is open) ----
  function caretAt(x, y){
    if(document.caretPositionFromPoint){ var p = document.caretPositionFromPoint(x, y); return p && {node: p.offsetNode, offset: p.offset}; }
    if(document.caretRangeFromPoint){ var r = document.caretRangeFromPoint(x, y); return r && {node: r.startContainer, offset: r.startOffset}; }
    return null;
  }
  function readFrom(i, d){
    S.i = i;
    if(S.mode === 'rec'){
      var seg = segOf(i); if(!seg) return;
      var t = seg.t;
      if(seg.w && seg.w.length){
        if(!seg.map) seg.map = align(seg.w.map(function(x){ return x[1]; }), domWords(S.list[i]));
        for(var s = 0; s < seg.w.length; s++) if(seg.map[s] >= d){ t = seg.t + seg.w[s][0] / 100; break; }
      }
      S.audio.currentTime = Math.max(0, t - 0.05);
      if(!S.playing) play(); else paint();
    } else {
      var sw = spokenWords(S.list[i]), from = 0;
      for(var k = 0; k < sw.length; k++) if(sw.map[k] >= d){ from = k; break; }
      S.playing = true; speakFrom(i, from);
    }
  }
  document.addEventListener('click', function(e){
    if(!S || e.button !== 0 || e.target.closest('a, button, select, input, summary, label, #player')) return;
    var sel = window.getSelection ? getSelection() : null; if(sel && !sel.isCollapsed) return;
    var i = -1;
    for(var j = 0; j < S.list.length; j++) if(S.list[j].el && S.list[j].el.contains(e.target)) i = j;
    if(i < 0) return;
    var dw = domWords(S.list[i]), d = 0, hit = e.target.closest && e.target.closest('span.w');
    if(!hit){   // between words: the word at the point tapped, or the next one
      var pos = caretAt(e.clientX, e.clientY), nd = pos && pos.node;
      hit = nd && (nd.nodeType === 1 ? nd : nd.parentElement).closest('span.w');
      if(!hit && nd && nd.nodeType === 3){ var nx = nd.nextSibling; while(nx && !(nx.nodeType === 1 && nx.classList.contains('w'))) nx = nx.nextSibling; hit = nx; }
    }
    for(var k = 0; k < dw.length; k++) if(dw[k].el === hit){ d = k; break; }
    readFrom(i, d);
  });

  // ---- controls ----
  function play(){
    if(!S) return;
    S.playing = true;
    if(S.mode === 'rec'){
      var t = timeOf(S.i);
      if(t != null && Math.abs(S.audio.currentTime - t) > 2 && !S.audio.currentTime) S.audio.currentTime = t;
      var pr = S.audio.play(); if(pr && pr.catch) pr.catch(function(){ S.playing = false; paint(); });
    } else speakFrom(S.i);
    paint();
  }
  function halt(){ token++; if(synth) synth.cancel(); if(S && S.audio) S.audio.pause(); }
  function pause(){ if(!S) return; S.playing = false; halt(); paint(); }
  function jumpSection(dir){
    var cur = S.list[S.i] ? S.list[S.i].sec : '', i = S.i;
    if(dir < 0){
      // back to this section's start, or the one before if already near its start
      var start = i; while(start > 0 && S.list[start - 1].sec === cur) start--;
      if(i - start <= 1 && start > 0){ var p = start - 1, s2 = S.list[p].sec; while(p > 0 && S.list[p - 1].sec === s2) p--; start = p; }
      i = start;
    } else { while(i < S.list.length && S.list[i].sec === cur) i++; if(i >= S.list.length) return; }
    S.i = i;
    if(S.mode === 'rec'){ var t = timeOf(i); if(t != null) S.audio.currentTime = t; paint(); }
    else if(S.playing) speakFrom(i); else paint();
  }
  function stop(){
    halt();
    if(S && S.audio){ S.audio.removeAttribute('src'); S.audio.load(); }
    S = null; mark(null); lastEl = null; markWord(null); backBtn();
    var p = $('player'); if(p) p.hidden = true;
    document.body.classList.remove('listening');
  }

  function start(key, intro, rec){
    stop();
    bar();
    S = {key: key, list: blocks(intro), i: 0, playing: false, rec: rec, rate: +(store.get('nl:rate') || 1), audio: null};
    if(RATES.indexOf(S.rate) < 0) S.rate = 1;
    $('plRate').value = String(S.rate);
    var saved = store.get('nl:voice');
    choose(rec ? (saved && saved.indexOf('rec:') === 0 ? saved : 'rec:' + rec.voices[0].voice) : (saved && saved.indexOf('dev:') === 0 ? saved : 'dev:'));
    fillVoices();
    $('player').hidden = false; document.body.classList.add('listening');
    if('mediaSession' in navigator){
      try {
        navigator.mediaSession.metadata = new MediaMetadata({title: intro || 'Daily Newsletter', artist: 'Daily Newsletter'});
        navigator.mediaSession.setActionHandler('play', play); navigator.mediaSession.setActionHandler('pause', pause);
        navigator.mediaSession.setActionHandler('nexttrack', function(){ jumpSection(1); }); navigator.mediaSession.setActionHandler('previoustrack', function(){ jumpSection(-1); });
      } catch(e){}
    }
    play();
  }

  // ---- the Listen button under the edition's summary ----
  function setup(key, intro){
    stop();
    var wrap = $('listenwrap'); if(!wrap) return;
    wrap.innerHTML = '';
    var list = blocks(intro);
    if(list.length < 3 || (!synth && !window.Audio)) return;
    var mins = Math.max(1, Math.round(words(list) / 165));
    wrap.innerHTML = '<button type="button" id="listenBtn" class="listen"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5v14l12-7z"/></svg>Listen</button><span class="listen-m" id="listenMeta">About ' + mins + ' min</span>';
    var rec = null;
    fetch('data/audio/' + key + '.json', {cache: 'no-cache'}).then(function(r){ return r.ok ? r.json() : null; }).then(function(m){
      if(!m || !m.voices || !m.voices.length) return;
      rec = m;
      $('listenMeta') && ($('listenMeta').textContent = Math.max(1, Math.round(m.voices[0].duration / 60)) + ' min');
    }).catch(function(){});
    $('listenBtn').addEventListener('click', function(){
      if(S && S.key === key){ S.playing ? pause() : play(); return; }
      if(!rec && !synth){ return; }
      start(key, intro, rec);
    });
    if(synth && synth.onvoiceschanged !== undefined) synth.onvoiceschanged = function(){ if(S) fillVoices(); };
  }

  window.Listen = {setup: setup, stop: stop, speakable: speakable};
})();
