# N62: 在 LRU 策略下，T_avg_resident 由缓存容量 C_norm 和请求热度分布 β 决定，近似公式为 T_avg_resident ≈ (C_nor

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

在 LRU 策略下，T_avg_resident 由缓存容量 C_norm 和请求热度分布 β 决定，近似公式为 T_avg_resident ≈ (C_norm / (1 - C_norm)) * (1/λ_avg) * (1/β)，代入 C_norm=0.119, β=0.9, λ_avg=500/day，计算得 T_avg_resident ≈ 0.0029 天（约 4.2 分钟），失效折扣因子约为 0.99997，对命中率影响可忽略不计。

## Corrected Claim

在 LRU 策略下，T_avg_resident 由缓存容量 C_norm 和请求热度分布 β 决定，近似公式为 T_avg_resident ≈ (C_norm / (1 - C_norm)) * (1/λ_avg) * (1/β)，代入 C_norm=0.119, β=0.9, λ_avg=500/day，计算得 T_avg_resident ≈ 0.0003 天（约 0.43 分钟），失效折扣因子约为 0.999999，对命中率影响可忽略不计。

## Evidence

父节点级核验未通过：有冗余（子节点2和子节点3存在逻辑冗余。子节点2旨在通过修正T_avg_resident来重新评估失效折扣因子，而子节点3旨在计算最终命中率，但其核心步骤依赖于P_invalid_LRU的计算，这与子节点2中的折扣因子计算本质上是同一物理量（失效概率/折扣）的不同表述或重复推导。此外，子节点2中列举不同T_avg_resident取值（0.01, 0.1）属于参数敏感性分析，应作为子节点1中修正因子K_size确定后的后续步骤，而非独立的正交分解项。）

## Search Query

LRU cache average residence time formula Pareto distribution
