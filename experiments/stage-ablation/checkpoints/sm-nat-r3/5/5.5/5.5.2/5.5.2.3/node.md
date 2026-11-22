# N255: 集中更新工作点下的字节加权命中率折损因子 D_concentrated = 1 - (0.891 * P_invalid_head * S_head_byte_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

集中更新工作点下的字节加权命中率折损因子 D_concentrated = 1 - (0.891 * P_invalid_head * S_head_byte_share) / (S_total_byte_share)，其中 S_head_byte_share 为头部10%对象占总字节量的比例，需基于 Pareto(α=1.1) 分布计算具体数值。

## Corrected Claim

集中更新工作点下的字节加权命中率折损因子 D_concentrated = 1 - (0.891 * P_invalid_head * S_head_byte_share) / (S_total_byte_share)，其中 S_head_byte_share 为头部10%对象占总字节量的比例，需基于 Pareto(α=1.1) 分布计算具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过
