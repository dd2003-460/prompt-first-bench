# N53: LRU 缓存中对象年龄分布：在稳态下，LRU 缓存中对象的年龄分布近似为指数分布，平均年龄 = T_avg = C_total / (R * S_avg_cac

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

LRU 缓存中对象年龄分布：在稳态下，LRU 缓存中对象的年龄分布近似为指数分布，平均年龄 = T_avg = C_total / (R * S_avg_cached)，其中 C_total=128GB，R 为总请求率，S_avg_cached 为缓存中对象的平均大小，需计算 S_avg_cached = ∫_{k=1}^{K} S(k) dk / K。

## Corrected Claim

在稳态下，LRU缓存中对象的年龄分布形态取决于访问模式（如Zipf分布），平均年龄可近似表示为 T_avg ≈ C_total / (R * S_avg_cached)，其中 S_avg_cached 需根据具体访问模型计算。

## Evidence

[质询]LRU缓存中对象的年龄分布通常不服从指数分布，而是取决于访问模式（如Zipf分布下，年龄分布往往呈现幂律或更复杂的形态，而非简单的指数衰减）；此外，平均年龄的公式 T_avg = C_total / (R * S_avg_cached) 在量纲上虽然看似合理（容量/请求率/大小 = 时间），但其物理意义依赖于特定的稳态假设和访问模型，并非LRU的通用第一性原理结论。 | 先验知识/题面给定，逻辑校验通过，但经验事实（具体分布形态和公式适用性）缺乏来源支持且存在理论争议

## Search Query

LRU cache object age distribution steady state
