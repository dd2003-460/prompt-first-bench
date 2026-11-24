# N307: 公有云CDN日级P99延迟劣化量化的计算：日级P99增量 = $\phi_{switch} \times (L_{suboptimal} - L_{optima

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N115, N116, N117

## Claim

公有云CDN日级P99延迟劣化量化的计算：日级P99增量 = $\phi_{switch} \times (L_{suboptimal} - L_{optimal}) \times (T_{switch}/T_{day})$，其中$T_{day}$=86400s。若$\phi_{switch}=0.5$，$\Delta L=30ms$，$T_{switch}=120s$，则日级P99增量 = $0.5 \times 30 \times (120/86400) \approx 0.21ms$。

## Corrected Claim

公有云CDN日级P99延迟劣化量化的计算：日级P99增量 = $\phi_{switch} \times (L_{suboptimal} - L_{optimal}) \times (T_{switch}/T_{day})$，其中$T_{day}$=86400s。若$\phi_{switch}=0.5$，$\Delta L=30ms$，$T_{switch}=120s$，则日级P99增量 = $0.5 \times 30 \times (120/86400) \approx 0.21ms$。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲一致（无量纲系数 × 时间 × 无量纲时间比 = 时间），数值计算 0.5 * 30 * (120/86400) = 0.2083... ≈ 0.21ms 准确无误。
