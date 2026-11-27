# N109: 稳态时间 T_steady 的修正公式：原公式 T_steady = C / (λ_total * E[S]) 物理意义不明，正确模型应为 T_steady ≈

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N42

## Claim

稳态时间 T_steady 的修正公式：原公式 T_steady = C / (λ_total * E[S]) 物理意义不明，正确模型应为 T_steady ≈ T_eviction_avg * (1/H_miss)，其中 T_eviction_avg 为平均驱逐间隔，需通过缓存容量与请求速率推导

## Corrected Claim

稳态时间 T_steady 的修正模型：原公式 T_steady = C / (λ_total * E[S]) 物理意义不明，更合理的经验近似模型为 T_steady ≈ T_eviction_avg * (1/H_miss)，其中 T_eviction_avg 为平均驱逐间隔，需结合缓存容量、请求速率及替换策略推导。

## Evidence

[质询]该陈述将复杂的缓存稳态建立时间简化为 T_eviction_avg * (1/H_miss)，忽略了缓存替换策略（如LRU vs FIFO）、访问局部性（Locality）以及初始冷启动效应。在缺乏具体替换算法和访问分布假设的情况下，该公式缺乏普适的理论推导基础，属于经验性近似而非严格物理/数学模型。 | 先验知识/题面给定，逻辑校验通过（量纲合理，概念自洽），但公式为经验近似，缺乏严格推导支持，故降级。

## Search Query

LRU steady state time cache eviction model
