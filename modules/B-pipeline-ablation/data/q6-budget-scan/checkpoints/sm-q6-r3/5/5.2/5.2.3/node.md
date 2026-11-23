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

父节点级核验通过：正交+完备+无冗余（子节点覆盖了父节点公式中所有关键参数（p_miss_base, TTL_opt, δ）的定义、计算依据及物理含义，同时扩展了多对象类型的加权处理和成本优化求解条件。各子节点分别针对不同类型的对象特性、参数推导逻辑、成本模型构成和求解方法，逻辑上相互独立且互补，无重复或矛盾。）
