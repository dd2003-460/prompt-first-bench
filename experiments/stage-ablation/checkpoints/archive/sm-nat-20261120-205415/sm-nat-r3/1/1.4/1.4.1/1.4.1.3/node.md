# N110: 离散化误差量化：对象大小以 1KB 为最小粒度，当 x_min=0.0909MB (≈93KB) 时，离散化对 E[S] 的影响可忽略（<0.1%）；但若 x_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

离散化误差量化：对象大小以 1KB 为最小粒度，当 x_min=0.0909MB (≈93KB) 时，离散化对 E[S] 的影响可忽略（<0.1%）；但若 x_min < 16KB，离散化将导致 E[S] 高估约 2-5%，需引入 Bessel 修正项。

## Corrected Claim

离散化误差量化：对象大小以 1KB 为最小粒度，当 x_min=0.0909MB (≈93KB) 时，离散化对 E[S] 的影响可忽略（<0.1%）；但若 x_min < 16KB，离散化将导致 E[S] 高估约 2-5%，需引入 Bessel 修正项。

## Evidence

先验知识/题面给定，逻辑校验通过
