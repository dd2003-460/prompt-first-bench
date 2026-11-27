# N129: 下游投影1：基础锚定系数 α_anchor_base 的量化，定义为 α_anchor_base = 0.3 + 0.1 * (F_exp / F_max)，其

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N32

## Claim

下游投影1：基础锚定系数 α_anchor_base 的量化，定义为 α_anchor_base = 0.3 + 0.1 * (F_exp / F_max)，其中 F_max 为品类平均最大曝光频次，表示在无额外信息干扰下的最低锚定强度。

## Corrected Claim

下游投影1：基础锚定系数 α_anchor_base 的量化，定义为 α_anchor_base = 0.3 + 0.1 * (F_exp / F_max)，其中 F_max 为品类平均最大曝光频次，表示在无额外信息干扰下的最低锚定强度。

## Evidence

先验知识/题面给定，逻辑校验通过
