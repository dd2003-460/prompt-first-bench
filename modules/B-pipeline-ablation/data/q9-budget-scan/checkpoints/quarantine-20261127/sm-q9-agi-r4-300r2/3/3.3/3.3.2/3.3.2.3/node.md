# N155: 引入 OpenAlex 作为二级校验源可将整体召回率提升至 R_combined = 1 - (1-R_crossref)(1-R_openalex)；已知 O

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

引入 OpenAlex 作为二级校验源可将整体召回率提升至 R_combined = 1 - (1-R_crossref)(1-R_openalex)；已知 OpenAlex 对预印本覆盖率 R_openalex ≈ 0.95，则 R_combined ≈ 1 - 0.15*0.05 = 0.9925，满足 <5% 虚构率目标

## Corrected Claim

引入 OpenAlex 作为二级校验源可将整体召回率提升至 R_combined = 1 - (1-R_crossref)(1-R_openalex)；已知 OpenAlex 对预印本覆盖率 R_openalex ≈ 0.95，则 R_combined ≈ 1 - 0.15*0.05 = 0.9925，满足 <5% 虚构率目标

## Evidence

先验知识/题面给定，逻辑校验通过：基于独立性假设的并集概率公式计算正确，数值推导无误。

## Search Query

OpenAlex API coverage preprint arxiv bioRxiv completeness comparison Crossref
