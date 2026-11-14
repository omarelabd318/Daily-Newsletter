# Attribution in the text

- **Name the outlet** whenever a claim is attributed: "according to Reuters", "Ahram Online reported",
  "per Bloomberg". A search result that summarises a story is not the source; credit the outlet behind it.
- **General credits** such as "according to news bulletins" or "market reports suggest" are fine when the
  point rests on more than one outlet. Never use them to stand in for a single source. The checker flags
  them only as a reminder to make sure several outlets back the point.
- **Attribute only where it adds something:** an exclusive, a disputed or unconfirmed claim, a forecast or
  an estimate, or a figure that differs between sources. Well-established facts need no credit in the text;
  the Sources list covers them.
- **Usually one credit per item:** if a point rests on several outlets, credit the main one, or use a
  general credit such as "according to news bulletins", and let the Sources list carry the rest. About
  10 to 20 credits in an edition reads naturally. The checker blocks publishing above 25 credits, when
  more than half the stories in a section carry a credit, or when one outlet is credited in more than half
  of a section's stories; it warns at 3 or more credits in one item.
- **EnterpriseAM and CairoScene are trusted, not the backbone:** treat both as very good, credible sources with
  strong stories, and use them freely, but check their stories against other outlets where they carry them too,
  and keep the two together under a third of the edition's sourced items (the checker warns above that). Never
  leave out a good story from either to balance the count: add strong stories from other outlets instead. Write
  in your own words so the edition never reads like a rewrite of either. Each story is still judged on its own
  merit and placed in the section where it belongs.
- **Spread the wire and world sources:** no other single outlet should carry more than about six of the
  edition's Sources links (EnterpriseAM and CairoScene fall under the one-third rule above instead). World and regional stories come from many outlets (Reuters, AP,
  AFP, BBC, the Financial Times, Bloomberg, The National, Asharq Al-Awsat, Al-Monitor, Al Jazeera and others):
  keep every story that deserves its place, but take it from the outlet with the fullest report, or the one
  closest to the news, rather than defaulting to one site, and check it against a second. Al Jazeera is a
  credible source for the region, but its own editorial line on Gulf and regional politics is one more reason
  to pair it with another outlet. The checker warns when one outlet passes six links.
- **Reuters via Yahoo Finance:** Yahoo Finance (finance.yahoo.com, and yahoo.com/news) republishes Reuters wire
  stories in full and free to read, marked "Reuters" at the top. It is Reuters' own reporting, word for word, so it
  is as reliable as Reuters itself: one of the most dependable sources there is for markets, economies, companies
  and world news. Use it freely, above all when reuters.com asks for a login or will not open. Credit Reuters in the
  text ("according to Reuters") and in Sources write `Reuters (via Yahoo Finance)` with the Yahoo link. It counts as
  Reuters, not Yahoo, for the six-links rule. The same goes for other wire stories Yahoo carries (AP, AFP): credit
  the agency. Yahoo's own articles and its contributor or partner pieces (Motley Fool, Zacks, Investopedia and the
  like) are not wire reporting: treat those as the outlet that wrote them. Summary services such as Finimize, which
  rewrite Reuters or Bloomberg stories, are leads only: find and cite the original.
- **FactIQ (connector, when the run has it, the mcp__factiq__ tools):** a read-only service of official statistics
  and filings. Use it where it holds the figure: Suez Canal, Bab el-Mandeb and Hormuz shipping (daily transits and
  cargo tonnage from IMF PortWatch, two to three weeks behind) for Suez, Red Sea and Iran-war stories; US data
  (payrolls, CPI, GDP from BLS and BEA, Treasury yields) and what Fed, ECB, Bank of England and other central bankers
  said, with quotes, for Global Markets; Brent, gold and FX as a second source for the currency table; company
  filings and earnings calls for a big company story; the IMF's forecasts for Egypt (yearly, marked as projections).
  It has no Egyptian news, EGX prices, monthly Egyptian figures or Central Bank of Egypt statements, and its
  dollar-pound rate is a market rate, not the central bank's: those stay with the usual sources. Credit the
  underlying source (IMF PortWatch, the BLS, the company's filing) with the link FactIQ returns, never FactIQ itself;
  log each lookup as a page (`research_log.py DATE newsletter page factiq:<what>`); without the connector, carry on.
- **Variety by adding, not dropping:** go through the whole EnterpriseAM edition (on weekdays) and
  CairoScene, and consider every item. Variety comes from adding strong stories from other outlets
  alongside them, never from leaving out a good EnterpriseAM or CairoScene story to balance the count.
- **Read EnterpriseAM with its script, not a web fetch:** on weekdays run
  `python3 .claude/skills/daily-newsletter/read_enterprise.py`. It prints the whole AM edition: every story
  in full with its own link, the smaller items inside each story (under their own subheadings), Today at a
  glance and the calendar. A web fetch only returns a summary, which can drop items and has no story
  links. Use a web fetch of https://enterpriseam.com/egypt/am-edition/ only if the script fails.
- **How research runs:** EnterpriseAM (on weekdays) and CairoScene are read in full on every run, as a
  core part of research, alongside many searches across many other outlets: Egyptian, regional and
  international. Neither comes first and neither is a fallback. Pick the day's stories from everything
  together, on merit, so the wider research shapes the edition as much as those two do.
- **Link each story's own page** in Sources, one link per story, for EnterpriseAM and CairoScene as for
  everyone else (for example `https://enterpriseam.com/egypt/2026/10/25/...`), not the homepage or the
  edition page. `enterpriseam.com/egypt/am-edition/` always shows the latest edition, so it points to the
  wrong day later. For items that appear only in the edition or on the homepage, use one line for that
  page and say how many items it was used for, for example
  `[EnterpriseAM Egypt, AM edition, 29 October 2026 (used for 3 items)](https://enterpriseam.com/egypt/am-edition/)`.
- **Dependence check:** the checker warns when EnterpriseAM and CairoScene make up more than a third of
  the links in Sources. The answer is wider research for more strong stories, never cutting a good one.
- **Merit, not origin:** the same bar applies the other way. Include an EnterpriseAM or CairoScene story
  because it is worth a reader's time, not because of where it came from; skip their minor items as you
  would anyone's. Each section should draw on a range of outlets, and the edition should never read like
  a summary of those two.
- **Credit every outlet the same way:** keep crediting EnterpriseAM and CairoScene whenever a point comes
  from them and the credit fits; they are trusted, daily sources. The aim is that other outlets are
  named just as readily when a point comes from them, not that these two are named less.
