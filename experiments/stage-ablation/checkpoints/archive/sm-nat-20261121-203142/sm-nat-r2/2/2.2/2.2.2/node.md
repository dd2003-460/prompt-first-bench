# N41: Pareto(α=1.1) 下对象大小超过缓存容量 C 的概率 P(S > C) = (C / x_min)^(-1.1)，该概率直接决定 LRU 命中率的上限

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

Pareto(α=1.1) 下对象大小超过缓存容量 C 的概率 P(S > C) = (C / x_min)^(-1.1)，该概率直接决定 LRU 命中率的上限损失，因为大对象永远无法完全驻留

## Corrected Claim

Pareto(α=1.1) 下对象大小超过缓存容量 C 的概率 P(S > C) = (C / x_min)^(-1.1)，该概率直接决定 LRU 命中率的上限损失，因为大对象永远无法完全驻留

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布尾部概率公式正确，且大对象无法驻留导致LRU命中率损失的逻辑自洽
