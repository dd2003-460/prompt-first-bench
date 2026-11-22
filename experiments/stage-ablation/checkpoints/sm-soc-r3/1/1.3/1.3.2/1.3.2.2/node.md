# N133: 下游投影1：P90 溢价的精确计算：P90 = P_market * exp(1.2816 * σ_ln)，其中 1.2816 为标准正态分布 90 分位点。若

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

下游投影1：P90 溢价的精确计算：P90 = P_market * exp(1.2816 * σ_ln)，其中 1.2816 为标准正态分布 90 分位点。若 σ_ln = 0.2，则 P90 ≈ P_market * 1.29；若 σ_ln = 0.3，则 P90 ≈ P_market * 1.50。这解释了为何高噪声导致 P90 高出 20%-35%。

## Corrected Claim

下游投影1：P90 溢价的精确计算：P90 = P_market * exp(1.2816 * σ_ln)，其中 1.2816 为标准正态分布 90 分位点。若 σ_ln = 0.2，则 P90 ≈ P_market * 1.29；若 σ_ln = 0.3，则 P90 ≈ P_market * 1.50。这解释了为何高噪声导致 P90 高出 20%-35%。

## Evidence

先验知识/题面给定，逻辑校验通过：1.2816为标准正态分布90分位点，exp(1.2816*0.2)≈1.29，exp(1.2816*0.3)≈1.50，计算准确且逻辑自洽

## Search Query

P90 asking price calculation log-normal distribution 90th percentile premium
