# N226: 双样本比例差异检验的合并比例 p_pool = (x_high + x_low) / (n_high + n_low)，其中 x_i = n_i * CVR_i

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

双样本比例差异检验的合并比例 p_pool = (x_high + x_low) / (n_high + n_low)，其中 x_i = n_i * CVR_i，用于计算标准误 SE_diff = sqrt(p_pool(1-p_pool)(1/n_high + 1/n_low))。

## Corrected Claim

双样本比例差异检验的合并比例 p_pool = (x_high + x_low) / (n_high + n_low)，其中 x_i = n_i * CVR_i，用于计算标准误 SE_diff = sqrt(p_pool(1-p_pool)(1/n_high + 1/n_low))。

## Evidence

先验知识/题面给定，逻辑校验通过
