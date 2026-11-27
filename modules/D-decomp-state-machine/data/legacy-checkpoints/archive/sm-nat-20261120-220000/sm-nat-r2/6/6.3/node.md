# N51: 在C/S_total >> 1且无更新失效的理想条件下，LRU对前1%热门对象的字节命中率下界为 1 - (1 - 0.0963) * (S_tail_byte

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

在C/S_total >> 1且无更新失效的理想条件下，LRU对前1%热门对象的字节命中率下界为 1 - (1 - 0.0963) * (S_tail_bytes / S_total_bytes)，需结合大小分布计算具体值。

## Corrected Claim

在C/S_total >> 1且无更新失效的理想条件下，LRU对前1%热门对象的字节命中率下界为 1 - (1 - 0.0963) * (S_tail_bytes / S_total_bytes)，需结合大小分布计算具体值。

## Evidence

先验知识/题面给定，逻辑校验通过
