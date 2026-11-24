# N182: 用户到最近 POP 距离 d_pop_i 估算：基于 POP 覆盖半径 ≤500km，假设用户均匀分布，平均距离 d_avg = 半径 * 2/π ≈ 318k

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N67

## Claim

用户到最近 POP 距离 d_pop_i 估算：基于 POP 覆盖半径 ≤500km，假设用户均匀分布，平均距离 d_avg = 半径 * 2/π ≈ 318km，最远距离 d_max = 500km，加权平均距离 Σ(w_i * d_pop_i) ≈ 300-400km（取决于用户密度分布）

## Corrected Claim

用户到最近 POP 距离 d_pop_i 估算：基于 POP 覆盖半径 ≤500km，假设用户均匀分布，平均距离 d_avg = 半径 * 2/π ≈ 318km，最远距离 d_max = 500km，加权平均距离 Σ(w_i * d_pop_i) ≈ 300-400km（取决于用户密度分布）

## Evidence

先验知识/题面给定，逻辑校验通过：均匀分布圆盘的平均距离公式为 2R/π，数值计算正确（500*2/3.14≈318），量级合理。

## Search Query

average distance user to nearest CDN POP 500km radius
