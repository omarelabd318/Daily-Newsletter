# The lead image (paper mode)

The site has three looks: light, dark and paper (a printed front page). In paper mode the lead story carries an
image above it. Give each daily edition one when a suitable image exists; go without when it does not.

- **Only images the newsletter has the right to publish.** A credit is not a license: never use a photo from a news
  outlet, an agency (Reuters, AP, AFP, Getty) or a social post. Use `lead_image.py search "name or place"`, which lists
  openly licensed photos (CC BY, CC BY-SA, CC0, public domain) from Openverse, many of them from the photo services
  of governments and international bodies. The search times out at times: try twice, then go without.
- **It must show what the caption says.** Pick a photo of the person or place the lead story is about, check its
  title and source page, and write the caption from what the source says it shows: who, where and, when it is not
  from the event itself, that it is earlier ("on an earlier visit", "in 2025"). Open the credit with "File photo:"
  then. Never imply a photo shows the day's event when it does not, and never use a look-alike or a generic scene
  as if it were the place.
- **Attach it** with `lead_image.py use DATE IMAGE_URL --caption ... --alt ... --credit ... --source PAGE_URL
  --license "CC BY 2.0"`. It saves `editions/img/DATE.jpg` and records the caption, credit, license and source on
  the edition in `editions/index.json`; commit both with the edition. `lead_image.py remove DATE` takes it off.
- **No photo:** leave the edition without one. Do not substitute a chart yet.
- Not for stories about deaths, accidents or crimes unless the photo is of the place or an official involved, and
  never a picture of victims.
