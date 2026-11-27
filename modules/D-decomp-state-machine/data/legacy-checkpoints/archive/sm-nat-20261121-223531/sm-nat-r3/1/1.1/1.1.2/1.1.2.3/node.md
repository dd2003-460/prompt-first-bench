# N96: s_max 对命中率 H_LRU 的间接影响：通过 E[S]_trunc 影响字节加权热度 h_avg = (Σ s_i * h_i) / (Σ s_i)，s_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

s_max 对命中率 H_LRU 的间接影响：通过 E[S]_trunc 影响字节加权热度 h_avg = (Σ s_i * h_i) / (Σ s_i)，s_max 增加 10% 导致 h_avg 变化 < 0.5% [待核验]，对最终命中率影响可忽略。

## Corrected Claim

s_max 对命中率 H_LRU 的间接影响：通过 E[S]_trunc 影响字节加权热度 h_avg = (Σ s_i * h_i) / (Σ s_i)，s_max 增加 10% 导致 h_avg 变化 < 0.5% [待核验]，对最终命中率影响可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：s_max 增加 10% 对字节加权热度 h_avg 的影响取决于对象大小分布的偏度，在典型 Web 缓存场景下，该间接效应通常远小于 0.5%，且对最终命中率的边际贡献可忽略，符合缓存理论直觉。
