# arXiv Submission Checklist

## Metadata

| Field | Value |
|-------|-------|
| **Title** | Prompt-First Research: Stage Ablation of a 1-Loop Pipeline in an LLM Agent (27B, No Tool Access) |
| **Authors** | [成璐 — fill in] |
| **Abstract** | (copy from paper-draft.md, ~250 words) |
| **Comments** | 11 arms × 5 questions × 3 reps = 165 runs. Code and data available at github.com/dd2003-460/prompt-first-bench |
| **Subjects** | cs.CL (primary), cs.AI (secondary), cs.LG (tertiary) |
| **Keywords** | prompt engineering; ablation study; LLM evaluation; research agents; uncertainty calibration |
| **License** | CC BY 4.0 |
| **Version** | v1 |
| **DOI** | (auto-assigned on submission) |

## File Checklist

- [x] `paper-draft.md` — cleaned, all internal refs removed, citations verified
- [ ] Figures: none required (all results are tables)
- [ ] Supplementary: `repro/` directory (prompts + gold answers + README)
- [ ] Data: `raw-data-full-perdim.json`, `hetero-judge-s6s7-results.json`, `bootstrap-cis.json`

## Pre-Submission Verification

- [x] All 31 references cited in body
- [x] All §refs point to existing sections
- [x] Statistical claims carry qualifiers (aggregation, n, judge family)
- [x] No [REDACTED]/TODO/FIXME placeholders
- [x] Word count: ~6,874 (within 4k–8k range)
- [x] Paired test updated to n=15 (S7V vs S7)
- [x] Language pass: no double words, consistent terminology
- [ ] LaTeX compilation (pandoc not installed locally — use arXiv's own converter or online)
- [ ] Author affiliations filled in
- [ ] ORCID iDs added

## Submission Steps

1. Convert markdown → LaTeX (or use pandoc for PDF)
2. Upload to https://arxiv.org/submission
3. Fill metadata form with values above
4. Select categories: cs.CL, cs.AI, cs.LG
5. Agree to license terms
6. Submit → wait for moderation (typically 1–3 business days)

## Post-Submission

- [ ] Monitor arxiv.org abs page for moderation status
- [ ] Share link on Twitter/X + relevant subreddits
- [ ] Add citation to related open-source project READMEs
