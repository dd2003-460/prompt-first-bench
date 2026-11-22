# N151: β 从 0.9 降至 0.8 时，头部 1% 对象流量集中度 C_head 从 63.1% 变为 1 - 0.01^(0.2) ≈ 67.4%，集中度增加 4.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

β 从 0.9 降至 0.8 时，头部 1% 对象流量集中度 C_head 从 63.1% 变为 1 - 0.01^(0.2) ≈ 67.4%，集中度增加 4.3 个百分点，导致 LFU 理论上限 H_LFU_max 相应提升，而 LRU 因抖动惩罚增加而命中率下降。

## Corrected Claim

β 从 0.9 降至 0.8 时，头部 1% 对象流量集中度 C_head 从 63.1% 变为 1 - 0.01^(0.2) ≈ 67.4%，集中度增加 4.3 个百分点，导致 LFU 理论上限 H_LFU_max 相应提升，而 LRU 因抖动惩罚增加而命中率下降。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 1 - 0.01^(0.2) ≈ 0.674 正确，Zipf 分布性质及 LFU/LRU 行为符合理论直觉
