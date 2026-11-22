# N11: 高性低成工作点：更新率 1%/天 对LRU有效命中率的衰减，失效对象比例 p_invalid = 0.01，有效命中率 H_effective = H_stea

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

高性低成工作点：更新率 1%/天 对LRU有效命中率的衰减，失效对象比例 p_invalid = 0.01，有效命中率 H_effective = H_steady * (1 - p_invalid * f_refill)，其中 f_refill 为重填充失败率，假设 f_refill=0.5，则 H_effective ≈ H_steady * 0.995

## Corrected Claim

高性低成工作点：更新率 1%/天 对LRU有效命中率的衰减，失效对象比例 p_invalid = 0.01，有效命中率 H_effective = H_steady * (1 - p_invalid * f_refill)，其中 f_refill 为重填充失败率，假设 f_refill=0.5，则 H_effective ≈ H_steady * 0.995

## Evidence

先验知识/题面给定，逻辑校验通过：根据公式 H_effective = H_steady * (1 - p_invalid * f_refill)，代入 p_invalid=0.01 和 f_refill=0.5，计算得 1 - 0.01 * 0.5 = 1 - 0.005 = 0.995，数值推导完全自洽。
