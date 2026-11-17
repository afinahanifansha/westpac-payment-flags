# Payment Flags — Westpac Hackathon Prototype

A clickable concept that helps customers review unusual payments, understand possible effects on bills and savings, and optionally ask a trusted person for a second opinion.

**Status:** static interaction prototype using fictional data. No live AI inference, banking APIs, payments, device location or phone-contact access. No sign-in or API keys are needed. This is a hackathon concept, not an official Westpac product.

## Try it

Open `index.html` in a modern desktop browser. For a local server, run:

```sh
python3 -m http.server 8000
```

Then open http://localhost:8000. No installation or build is required.

## Scenarios

| Scenario | Demonstration |
| --- | --- |
| Maya · Boutique | A $268 dress purchase, unusual clothing spending, estimated bill and Japan goal impact, customer choices. |
| George and David | Trusted-person pairing, a $4,800 roofing payment, optional second opinion and George’s final decision. |
| Sam · Paris | Phone-location context in Paris compared with a card transaction in Perth. |
| Smart SafeBlock | Exploratory opt-in auto-protection journey; simulated proposed functionality. |
| Flag settings | Customer preferences and thresholds. |

Use the left panel to select scenarios or jump between screens. Escape toggles recording mode; R resets; keys 1–5 select scenarios. The slider changes phone size. The George scenario displays two phones.

Direct links: `?s=maya`, `?s=margaret`, `?s=location`, `?s=auto`, `?s=settings`. Add `&rec` for recording mode. The legacy internal key `margaret` opens the George scenario; all visible names use George.

## Publish on GitHub Pages

1. Create a repository, for example `westpac-payment-flags`.
2. Upload the **contents** of this extracted folder, with `index.html` at the repository root. Do not upload just the ZIP.
3. Commit to `main`.
4. Open **Settings → Pages**. Under **Build and deployment**, select **Deploy from a branch**, choose **main** and **/(root)**, then Save.
5. Use the live URL shown on that page once publishing completes. A typical project URL is `https://YOUR-USERNAME.github.io/westpac-payment-flags/`.

Official instructions: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## Implementation

The self-contained HTML embeds its CSS, JavaScript, font and logo. JavaScript manages scenario state, view templates and click handlers. There is no backend or external runtime dependency. See [architecture](docs/ARCHITECTURE.md), [safety](docs/SAFETY.md), [demo guide](docs/DEMO.md) and [submission template](docs/SUBMISSION.md).

Run basic packaging checks with `python3 scripts/check.py`. These checks validate content and packaging; they do not replace browser testing.

## Team and submission

University: Queensland University of Technology (QUT).

Team name, member names, video URL and live prototype URL: complete [docs/SUBMISSION.md](docs/SUBMISSION.md) before submitting.

## Credits

Westpac GEL theme tokens, font and logo assets are embedded in the prototype. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). No project-wide open-source licence has been selected by the team.
