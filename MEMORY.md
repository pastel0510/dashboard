
## Dashboard Image Policy
**Always use remote image URLs, never save image files to the git repo.**

The dashboard (`pastel0510/dashboard`) must:
- Use direct links to images (e.g., `https://media.mas.to/...`, `https://i.redd.it/...`, `https://imgs.xkcd.com/...`)
- Wrap images in `<a href="URL">` tags so they're clickable to full size
- Never commit `.jpg`, `.png`, or `.gif` files to the repo

Images currently used:
- **Bunny**: Reddit direct image URL from `bunny.url`
- **xkcd**: xkcd direct image URL from `xkcd.url`
- **Fingerpori**: Mastodon media attachment URL from `fingerpori.url`

Source: User instruction (Shadow), 2026-03-01

## Daily Reflections

**March 3, 2026** — Added weather widgets displaying current temperatures for multiple cities to the dashboard, alongside relocating the smiley indicator to the top-right corner. The fetch-latest.sh script already contained {{CITY_TEMP}} placeholder logic; running it populated the live temperature data and completed the layout adjustments successfully.
