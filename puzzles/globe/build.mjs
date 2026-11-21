// Builds the Globe game's data (puzzles/globe/world.json) from Natural Earth's 1:50m countries (the world-atlas
// package): the shapes, simplified, as TopoJSON; each country's name, other names it goes by, and whether it can be
// guessed and be an answer; and the distance in km between the closest borders of every two guessable countries.
// Run once (the map rarely changes):  npm i world-atlas@2 d3-geo@3 topojson-client@3 topojson-simplify@3
//   then  node puzzles/globe/build.mjs  from the repo root, with that node_modules on NODE_PATH or next to it.
import { createRequire } from 'module';
import { writeFileSync } from 'fs';
const require = createRequire(process.env.NODE_PATH ? process.env.NODE_PATH + '/' : import.meta.url);
const topo = require('world-atlas/countries-50m.json');
const tc = require('topojson-client'), ts = require('topojson-simplify'), d3 = require('d3-geo');

// places that are not countries: drawn as land, never an answer; the ones people may well type are guessable
const TERR = new Set(['N. Mariana Is.', 'U.S. Virgin Is.', 'Guam', 'American Samoa', 'S. Geo. and the Is.', 'Br. Indian Ocean Ter.',
  'Saint Helena', 'Pitcairn Is.', 'Anguilla', 'Cayman Is.', 'Bermuda', 'British Virgin Is.', 'Turks and Caicos Is.', 'Montserrat',
  'Jersey', 'Guernsey', 'Isle of Man', 'Niue', 'Cook Is.', 'Aruba', 'Curaçao', 'St. Pierre and Miquelon', 'Wallis and Futuna Is.',
  'St-Martin', 'St-Barthélemy', 'Fr. S. Antarctic Lands', 'Åland', 'Faeroe Is.', 'Indian Ocean Ter.', 'Heard I. and McDonald Is.',
  'Norfolk Island', 'Ashmore and Cartier Is.', 'Antarctica', 'Sint Maarten', 'Siachen Glacier']);
const GUESS_ONLY = new Set(['Greenland', 'Puerto Rico', 'W. Sahara', 'Falkland Is.', 'New Caledonia', 'Fr. Polynesia', 'Hong Kong', 'Macao']);
const MERGE = { 'Somaliland': 'Somalia', 'N. Cyprus': 'Cyprus' };
// the name shown, then other names a player may type
const NAMES = {
  'United States of America': ['United States', 'USA', 'US', 'America', 'United States of America'],
  'United Kingdom': ['United Kingdom', 'UK', 'Britain', 'Great Britain', 'England', 'Scotland', 'Wales', 'Northern Ireland'],
  'Dem. Rep. Congo': ['DR Congo', 'Democratic Republic of the Congo', 'DRC', 'Congo-Kinshasa', 'Zaire'],
  'Congo': ['Republic of the Congo', 'Congo', 'Congo-Brazzaville'],
  'Central African Rep.': ['Central African Republic', 'CAR'],
  'Bosnia and Herz.': ['Bosnia and Herzegovina', 'Bosnia'],
  'Dominican Rep.': ['Dominican Republic'],
  'Eq. Guinea': ['Equatorial Guinea'],
  'S. Sudan': ['South Sudan'],
  'eSwatini': ['Eswatini', 'Swaziland'],
  'Macedonia': ['North Macedonia', 'Macedonia'],
  "Côte d'Ivoire": ["Côte d'Ivoire", 'Ivory Coast', "Cote d'Ivoire"],
  'Czechia': ['Czechia', 'Czech Republic'],
  'Timor-Leste': ['Timor-Leste', 'East Timor'],
  'Myanmar': ['Myanmar', 'Burma'],
  'Cabo Verde': ['Cabo Verde', 'Cape Verde'],
  'Solomon Is.': ['Solomon Islands'],
  'Marshall Is.': ['Marshall Islands'],
  'St. Vin. and Gren.': ['Saint Vincent and the Grenadines', 'St Vincent'],
  'St. Kitts and Nevis': ['Saint Kitts and Nevis', 'St Kitts'],
  'Saint Lucia': ['Saint Lucia', 'St Lucia'],
  'Antigua and Barb.': ['Antigua and Barbuda', 'Antigua'],
  'São Tomé and Principe': ['São Tomé and Príncipe', 'Sao Tome and Principe', 'Sao Tome'],
  'Vatican': ['Vatican City', 'Vatican', 'Holy See'],
  'W. Sahara': ['Western Sahara'],
  'Falkland Is.': ['Falkland Islands', 'Falklands', 'Malvinas'],
  'Fr. Polynesia': ['French Polynesia', 'Tahiti'],
  'Turkey': ['Türkiye', 'Turkey', 'Turkiye'],
  'South Korea': ['South Korea', 'Korea', 'Republic of Korea'],
  'North Korea': ['North Korea', 'DPRK'],
  'Netherlands': ['Netherlands', 'Holland'],
  'United Arab Emirates': ['United Arab Emirates', 'UAE', 'Emirates'],
  'Micronesia': ['Micronesia', 'Federated States of Micronesia'],
  'Gambia': ['Gambia', 'The Gambia'],
  'Bahamas': ['Bahamas', 'The Bahamas'],
  'Palestine': ['Palestine', 'State of Palestine'],
  'Russia': ['Russia', 'Russian Federation'],
  'Laos': ['Laos', "Lao People's Democratic Republic"],
  'Vietnam': ['Vietnam', 'Viet Nam'],
  'Syria': ['Syria', 'Syrian Arab Republic'],
  'Iran': ['Iran', 'Persia'],
  'Taiwan': ['Taiwan'],
  'Brunei': ['Brunei', 'Brunei Darussalam'],
  'Moldova': ['Moldova'],
  'Tanzania': ['Tanzania'],
  'Bolivia': ['Bolivia'],
  'Venezuela': ['Venezuela'],
};

const G = topo.objects.countries.geometries;
// fold the merged parts into their country
const byName = new Map(G.map(g => [g.properties.name, g]));
for (const [part, into] of Object.entries(MERGE)) {
  const a = byName.get(part), b = byName.get(into);
  const merged = tc.mergeArcs(topo, [a, b]);
  b.type = merged.type; b.arcs = merged.arcs; G.splice(G.indexOf(a), 1);
}
// simplify (keeping shared borders shared), then quantize
let t = ts.presimplify(topo);
t = ts.simplify(t, ts.quantile(t, 0.8));   // a fifth of the points: plenty for a globe this size
t.arcs = t.arcs.map(a => a.map(p => [p[0], p[1]]));
t = tc.quantize(t, 2e4);

const R = 6371;
const out = [];
t.objects.countries.geometries.forEach(g => {
  const raw = g.properties.name, terr = TERR.has(raw), guess = !terr, names = NAMES[raw] || [raw];
  const f = tc.feature(t, g), area = d3.geoArea(f) * R * R;
  g.properties = { n: names[0] };
  if (names.length > 1) g.properties.k = names.slice(1);
  if (guess) g.properties.g = 1;
  if (guess && !GUESS_ONLY.has(raw) && area >= 1000) g.properties.a = 1;
  if (area < 3000) g.properties.s = 1;           // small: drawn with a ring so it can be seen
  delete g.id;
  out.push({ g, f, guess });
});
const guessable = out.filter(x => x.guess);
guessable.forEach((x, i) => { x.g.properties.i = i; });

// border-to-border distance: 0 for neighbours (a shared border in the topology), otherwise the closest two points
const nb = tc.neighbors(t.objects.countries.geometries);
const idxOf = new Map(t.objects.countries.geometries.map((g, i) => [g, i]));
const toV = ([lo, la]) => { const a = lo * Math.PI / 180, b = la * Math.PI / 180; return [Math.cos(b) * Math.cos(a), Math.cos(b) * Math.sin(a), Math.sin(b)]; };
const pts = guessable.map(x => { const p = []; d3.geoStream(x.f, { point(lo, la) { p.push(toV([lo, la])); }, lineStart() {}, lineEnd() {}, polygonStart() {}, polygonEnd() {}, sphere() {} }); return p; });
const cap = pts.map(p => { let c = [0, 0, 0]; p.forEach(v => { c[0] += v[0]; c[1] += v[1]; c[2] += v[2]; }); const l = Math.hypot(...c) || 1; c = c.map(z => z / l);
  let r = 0; p.forEach(v => { r = Math.max(r, Math.acos(Math.min(1, c[0] * v[0] + c[1] * v[1] + c[2] * v[2]))); }); return { c, r }; });
const N = guessable.length, D = [];
for (let i = 0; i < N; i++) for (let j = i + 1; j < N; j++) {
  const gi = guessable[i].g, gj = guessable[j].g;
  if (nb[idxOf.get(gi)].includes(idxOf.get(gj))) { D.push(0); continue; }
  let best = -2; const A = pts[i], B = pts[j];
  for (const a of A) for (const b of B) { const d = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]; if (d > best) best = d; }
  D.push(Math.round(Math.acos(Math.min(1, best)) * R));
}
const world = { topo: t, n: N, dist: D };
writeFileSync(new URL('./world.json', import.meta.url), JSON.stringify(world));
console.log('countries', out.length, 'guessable', N, 'answers', out.filter(x => x.g.properties.a).length, 'pairs', D.length);
