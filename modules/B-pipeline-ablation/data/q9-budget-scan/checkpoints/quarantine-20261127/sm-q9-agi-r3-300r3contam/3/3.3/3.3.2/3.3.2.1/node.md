# N153: Crossref API 对预印本（arXiv/bioRxiv）的收录覆盖率 C_preprint 约为 0.7-0.85，导致仅基于 Crossref 的 D

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N60

## Claim

Crossref API 对预印本（arXiv/bioRxiv）的收录覆盖率 C_preprint 约为 0.7-0.85，导致仅基于 Crossref 的 DOI 匹配召回率 R_crossref = P(DOI exists) * C_preprint；若 P(DOI exists)=1.0，则 R_crossref ≈ 0.7-0.85

## Corrected Claim

Crossref API 对预印本（arXiv/bioRxiv）的收录覆盖率 C_preprint 通常在 0.7-0.9 之间波动（取决于具体年份和平台），导致仅基于 Crossref 的 DOI 匹配召回率 R_crossref 受此限制。

## Evidence

[质询]Crossref 对 arXiv 和 bioRxiv 的收录覆盖率并非固定为 0.7-0.85，而是随时间动态变化且存在显著差异（例如 arXiv 早期论文覆盖率较低，近期较高；bioRxiv 覆盖率通常低于 arXiv），该数值范围缺乏精确的统计支撑，属于经验估计值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Crossref API coverage arxiv preprint DOI registration rate statistics 2024
