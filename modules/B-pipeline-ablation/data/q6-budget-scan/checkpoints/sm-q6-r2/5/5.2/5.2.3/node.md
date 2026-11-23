# N77: TTL 对回源率的影响：p_miss(TTL) = p_miss_base * (1 + (TTL_opt/TTL)^δ)，其中 p_miss_base 为基准

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

TTL 对回源率的影响：p_miss(TTL) = p_miss_base * (1 + (TTL_opt/TTL)^δ)，其中 p_miss_base 为基准回源率，TTL_opt 为最优 TTL，δ 为回源敏感度（通常 0.5-1.5）

## Corrected Claim

TTL 对回源率的影响：p_miss(TTL) = p_miss_base * (1 + (TTL_opt/TTL)^δ)，其中 p_miss_base 为基准回源率，TTL_opt 为最优 TTL，δ 为回源敏感度（通常 0.5-1.5）

## Evidence

先验知识/题面给定，逻辑校验通过
