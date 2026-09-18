# MeSS project page

Project website for **MeSS: City Mesh-Guided Outdoor Scene Generation with
Cross-View Consistent Diffusion**, accepted at the German Conference on Pattern
Recognition (GCPR 2026).

- Project page: https://albertchen98.github.io/mess/
- Implementation: https://github.com/Albertchen98/mess-code
- arXiv: https://arxiv.org/abs/2508.15169
- Camera-ready paper: [PDF](static/pdfs/mess-gcpr2026.pdf)
- Supplementary material: [PDF](static/pdfs/mess-gcpr2026-supp.pdf)

## Local preview

This is a static website with no build step. From the repository root:

```sh
python3 -m http.server 8000
```

Open http://localhost:8000. The page content is in `index.html`, with styling
and interactions in `static/css/index.css` and `static/js/index.js`.

## Content

The author list, affiliations, abstract, figures, and results follow the GCPR
2026 camera-ready paper. Paper figures are rasterized from the original PDFs
for browser display. The existing stylized videos are retained.

## Attribution

Based on the [Academic Project Page Template](https://github.com/eliahuhorwitz/Academic-project-page-template),
adapted from [Nerfies](https://nerfies.github.io).
The website template is licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
