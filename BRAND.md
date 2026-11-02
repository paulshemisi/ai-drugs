# AI D.R.U.G.S. — Brand directives

## Concept

Fake sample-pack cover. Provocation at the entrance, proof at the exit.
Everything visual is cold, clinical, black and gold. The name already provokes; the rest must stay sober.

## Palette

| Role | Hex |
|---|---|
| Background | `#0A0A0A` |
| Surface | `#141414` |
| Gold (only accent) | `#C9A227` |
| Off-white (text, sticker) | `#F2EFE6` |

No other color. No gradients, no glow.

## Typography

- Titles: Georgia (serif, bold). Fallback: Times New Roman.
- Code and labels: Courier New. Preferred if installed: JetBrains Mono.
- Labels in caps with wide letter-spacing (2 to 3 px). Titles and taglines in sentence case.

## Voice

Short, clinical, no hype. Never promise results the benchmark does not show.
Approved lines:

- Hallucinations are raw material.
- Generate wildly. Keep only what passes tests.
- Verified on exit.
- Tests pass or it doesn't ship.

## Imagery rules

- Abstract golden dust only. No syringes, pills, white powder, or realistic drug imagery.
- The trance is an eye with a spiral, never a person.
- Sticker "HALLUCINATIONS INSIDE. / VERIFIED ON EXIT" is the single off-white element on a cover.

## Files

| File | Size | Use |
|---|---|---|
| `assets/banner.svg` | 1280×640 | Top of README |
| `assets/social-card.svg` | 1200×630 | Open Graph / social preview (export to PNG) |
| `assets/logo.svg` | 512×512 | Avatar, favicon, PyPI logo |
| `assets/phases.svg` | 1230×410 | README, docs, slides |

## Export to PNG

GitHub social preview and most platforms need PNG, not SVG.

```bash
# Option 1: librsvg (macOS: brew install librsvg)
rsvg-convert -w 1200 -h 630 assets/social-card.svg -o assets/social-card.png
rsvg-convert -w 512  -h 512 assets/logo.svg        -o assets/logo.png
rsvg-convert -w 1280 -h 640 assets/banner.svg      -o assets/banner.png

# Option 2: Inkscape
inkscape assets/social-card.svg --export-type=png --export-width=1200 --export-filename=assets/social-card.png
```

Fonts must be installed on the machine that exports. If Georgia or Courier New are missing, text falls back and widths change. Check the PNG before publishing.

## Favicon sizes

```bash
for s in 16 32 48 180; do rsvg-convert -w $s -h $s assets/logo.svg -o assets/logo-$s.png; done
```

## GitHub setup

1. Repo name: `ai-drugs`. Description: `Generate wildly. Keep only what passes tests.`
2. Topics: `llm`, `python`, `code-generation`, `generative-ai`, `sampling`, `verification`, `open-source`.
3. Settings → General → Social preview → upload `social-card.png`.
4. Pin the repo on your profile. Use `logo.png` as the org or repo avatar.

## Image-generation prompt (for a richer hero illustration)

> Flat vector sticker illustration, pure black background #0A0A0A, single gold color #C9A227 plus off-white #F2EFE6 only. A stylized retro robot head in profile, leaning forward over a thin table, its nozzle-like snout hovering above a thin line of golden dust. Spiral eye made of concentric gold rings. Faint concentric halo circles behind the head, tiny floating 0 and 1 characters. Sample-pack cover composition, thin gold border, no text, no realistic drug paraphernalia, no gradients, no glow, high contrast, minimal.

Negative prompt: syringe, pill, white powder, smoke, human face, neon, gradient, 3D render.

## Social copy

- Tagline: Stop fixing hallucinations. Start distilling them.
- Launch post: "Hallucinations are raw material. AI D.R.U.G.S. generates wildly, then keeps only what compiles and passes your tests. Open source."
- First comment (always): link to the benchmark protocol. Without numbers, do not post.
