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
  var WORDS = [['YTD','year to date'],['YoY','year on year'],['EGX30','E G X thirty'],['EGX70','E G X seventy'],['EGX100','E G X one hundred'],
    ['S&P 500','S and P five hundred'],['S&P','S and P'],['CBE','C B E'],['IMF','I M F'],['GDP','G D P'],['OPEC+','OPEC plus'],
    ['Q1','the first quarter'],['Q2','the second quarter'],['Q3','the third quarter'],['Q4','the fourth quarter']];
  var NUM = '(\\d[\\d,]*(?:\\.\\d+)?)';
  function esc(re){ return re.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }
  function speakable(t){
    t = t.replace(new RegExp('\\bEGP\\s?' + NUM + '\\s?(tn|bn|mn|m|k)?\\b', 'g'), function(m, n, u){ return n + (u ? ' ' + UNITS[u] : '') + ' pounds'; });
    t = t.replace(new RegExp('\\$' + NUM + '\\s?(tn|bn|mn|m|k)\\b', 'g'), function(m, n, u){ return n + ' ' + UNITS[u] + ' dollars'; });
    t = t.replace(new RegExp('\\$' + NUM + '(?:\\s(trillion|billion|million|thousand))?', 'g'), function(m, n, u){ return n + (u ? ' ' + u : '') + ' dollars'; });
    t = t.replace(new RegExp('\\b' + NUM + '\\s?bps?\\b', 'g'), '$1 basis points');
    t = t.replace(new RegExp(NUM + '\\s?%', 'g'), '$1 percent');
    t = t.replace(/\s?°C\b/g, ' degrees');
    t = t.replace(/\b(\d{1,2}(?::\d\d)?)\s?(am|pm)\b/g, function(m, h, ap){ return h + (ap === 'am' ? ' a.m.' : ' p.m.'); });
    t = t.replace(/(\d)\s?[–—-]\s?(\d)/g, '$1 to $2');
    t = t.replace(/\b(\d{1,2}) (Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\b/g, '$2 $1');
    t = t.replace(/(^|[^\w.])([+−-])(\d)/g, function(m, pre, s, d){ return pre + (s === '+' ? 'plus ' : 'minus ') + d; });
    Object.keys(MONTHS).forEach(function(k){ t = t.replace(new RegExp('\\b' + k + '\\.?(?= \\d)', 'g'), MONTHS[k]); });
    WORDS.forEach(function(w){ t = t.replace(new RegExp('(^|[^\\w&])' + esc(w[0]) + '(?![\\w&])', 'g'), '$1' + w[1]); });
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
    p.innerHTML = '<div class="pl-in">'
      + '<button type="button" class="pl-b" data-a="prev" aria-label="Previous section"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 5h2v14H6zM20 5v14L9 12z"/></svg></button>'
      + '<button type="button" class="pl-b pl-play" data-a="play" aria-label="Pause"></button>'
      + '<button type="button" class="pl-b" data-a="next" aria-label="Next section"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16 5h2v14h-2zM4 5v14l11-7z"/></svg></button>'
      + '<div class="pl-now"><b id="plSec"></b><span id="plTime"></span><input id="plSeek" type="range" min="0" max="1000" value="0" aria-label="Position"></div>'
      + '<select id="plRate" aria-label="Speed">' + RATES.map(function(r){ return '<option value="' + r + '"' + (r === 1 ? ' selected' : '') + '>' + r + '×</option>'; }).join('') + '</select>'
      + '<select id="plVoice" aria-label="Voice"></select>'
      + '<button type="button" class="pl-b pl-x" data-a="close" aria-label="Stop listening"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.4 5 5 6.4 10.6 12 5 17.6 6.4 19 12 13.4 17.6 19 19 17.6 13.4 12 19 6.4 17.6 5 12 10.6z"/></svg></button>'
      + '</div>';
    document.body.appendChild(p);
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
      var f = this.value / 1000;
      if(S.mode === 'rec' && S.audio.duration) S.audio.currentTime = f * S.audio.duration;
      else { S.i = Math.min(S.list.length - 1, Math.floor(f * S.list.length)); if(S.playing) speakFrom(S.i); else paint(); }
    });
    return p;
  }

  function fillVoices(){
    var sel = $('plVoice'); if(!sel || !S) return;
    var html = '';
    if(S.rec) html += '<optgroup label="Natural voice">' + S.rec.voices.map(function(v){ return '<option value="rec:' + v.voice + '">' + v.name + '</option>'; }).join('') + '</optgroup>';
    var dv = deviceVoices();
    if(dv.length) html += '<optgroup label="This device">' + dv.map(function(v){ return '<option value="dev:' + v.voiceURI.replace(/"/g, '&quot;') + '">' + v.name.replace(/</g, '') + '</option>'; }).join('') + '</optgroup>';
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
    lastEl = el;
    if(!el) return;
    el.classList.add('reading');
    var r = el.getBoundingClientRect();
    if(follow && (r.top < 80 || r.bottom > innerHeight - 110)) el.scrollIntoView({block: 'center', behavior: 'smooth'});
  }
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
      $('plTime').textContent = fmt(t / S.rate) + ' / ' + fmt(d / S.rate);
      $('plSeek').value = d ? Math.round(t / d * 1000) : 0;
    } else {
      var left = words(S.list.slice(S.i)) / (165 * S.rate) * 60;
      $('plTime').textContent = 'About ' + Math.max(1, Math.round(left / 60)) + ' min left';
      $('plSeek').value = Math.round(S.i / S.list.length * 1000);
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
    var out = [], parts = t.match(/[^.!?]+(?:[.!?]+["”’)]*|$)\s*/g) || [t];
    parts.forEach(function(p){ p = p.trim(); if(!p) return; while(p.length > 220){ var cut = p.lastIndexOf(',', 220); cut = cut > 80 ? cut + 1 : 220; out.push(p.slice(0, cut)); p = p.slice(cut).trim(); } out.push(p); });
    return out;
  }
  function speakFrom(i){
    if(!synth) return;
    var my = ++token;
    synth.cancel();
    S.i = i; paint();
    var b = S.list[i]; if(!b){ S.playing = false; paint(); return; }
    var parts = sentences(speakable(b.text)), k = 0;
    var next = function(){
      if(my !== token || !S) return;
      if(k >= parts.length){
        setTimeout(function(){ if(my === token && S && S.playing) speakFrom(i + 1); }, b.kind === 'text' ? 250 : 450);
        return;
      }
      var u = new SpeechSynthesisUtterance(parts[k++]);
      if(S.voice){ u.voice = S.voice; u.lang = S.voice.lang; } else u.lang = 'en-US';
      u.rate = S.rate;
      u.onend = next; u.onerror = function(e){ if(e.error !== 'interrupted' && e.error !== 'canceled') next(); };
      synth.speak(u);
    };
    next();
  }

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
    S = null; mark(null); lastEl = null;
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
    choose(saved && (saved.indexOf('dev:') === 0 || rec) ? saved : (rec ? 'rec:' + rec.voices[0].voice : 'dev:'));
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
      $('listenMeta') && ($('listenMeta').textContent = Math.max(1, Math.round(m.voices[0].duration / 60)) + ' min · natural voice');
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
