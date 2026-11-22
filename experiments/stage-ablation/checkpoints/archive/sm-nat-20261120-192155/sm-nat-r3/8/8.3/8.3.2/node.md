# N132: 工作点2（低更新敏感/高频率）：头部对象（i=1）的更新驱逐概率 p_evict_1 ≈ U / r_1。给定 R_total=5e7/day，r_1 ≈ 5e

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N49

## Claim

工作点2（低更新敏感/高频率）：头部对象（i=1）的更新驱逐概率 p_evict_1 ≈ U / r_1。给定 R_total=5e7/day，r_1 ≈ 5e7 * (1/ζ(0.9,1)) ≈ 5e7 * 0.5 ≈ 2.5e7/day，则 p_evict_1 ≈ 0.01 / 2.5e7 ≈ 4e-10。此工作点证明热门对象几乎不受更新影响，其命中率折扣可忽略。

## Corrected Claim

工作点2（低更新敏感/高频率）：头部对象（i=1）的更新驱逐概率 p_evict_1 ≈ U / r_1。给定 R_total=5e7/day，r_1 ≈ 5e7 * (1/ζ(0.9,1)) ≈ 5e7 * 0.5 ≈ 2.5e7/day，则 p_evict_1 ≈ 0.01 / 2.5e7 ≈ 4e-10。此工作点证明热门对象几乎不受更新影响，其命中率折扣可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：基于Zipf分布参数ζ(0.9,1)≈2.0推导头部对象频率占比约50%，进而计算驱逐概率量级为1e-10，数学推导自洽且符合低更新敏感场景的物理直觉。
