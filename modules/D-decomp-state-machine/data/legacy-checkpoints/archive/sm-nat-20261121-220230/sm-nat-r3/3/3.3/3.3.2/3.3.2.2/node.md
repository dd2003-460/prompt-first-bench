# N181: LRU 失效折扣因子的重新评估：若 T_avg_resident 修正为 0.01 天（考虑大小修正），则失效折扣因子 (1 - 0.01 * 0.01) = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

LRU 失效折扣因子的重新评估：若 T_avg_resident 修正为 0.01 天（考虑大小修正），则失效折扣因子 (1 - 0.01 * 0.01) = 0.9999，对命中率影响仍可忽略；若 T_avg_resident 修正为 0.1 天，则折扣因子 = 0.999，需确定修正后的 T_avg_resident 以量化影响。

## Corrected Claim

LRU 失效折扣因子的重新评估：若 T_avg_resident 修正为 0.01 天（考虑大小修正），则失效折扣因子 (1 - 0.01 * 0.01) = 0.9999，对命中率影响仍可忽略；若 T_avg_resident 修正为 0.1 天，则折扣因子 = 0.999，需确定修正后的 T_avg_resident 以量化影响。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（1-0.0001=0.9999, 1-0.01=0.999），量级判断符合直觉（小概率失效对命中率影响微小），无外部来源矛盾。

## Search Query

LRU invalidation discount factor residence time correction
