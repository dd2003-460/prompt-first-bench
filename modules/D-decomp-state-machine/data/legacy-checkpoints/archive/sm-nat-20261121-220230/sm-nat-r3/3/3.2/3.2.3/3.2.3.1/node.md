# N174: 中热度对象（λ_i ∈ [50, 1000]）在 LRU 队列中的平均驻留时间 T_resident 的解析计算：基于堆栈距离模型，T_resident = 1

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N60

## Claim

中热度对象（λ_i ∈ [50, 1000]）在 LRU 队列中的平均驻留时间 T_resident 的解析计算：基于堆栈距离模型，T_resident = 1 / (λ_i * P_eviction)，其中 P_eviction 为对象被驱逐前的概率，需结合 C_norm=0.119 和 β=0.9 计算具体数值，以验证 T_resident ≈ 1.5 天的合理性。

## Corrected Claim

中热度对象（λ_i ∈ [50, 1000]）在 LRU 队列中的平均驻留时间 T_resident 需基于堆栈距离模型和具体缓存参数进行数值模拟或更复杂的解析计算，不能简单用 T_resident = 1 / (λ_i * P_eviction) 得出固定值 1.5 天。

## Evidence

[质询]公式 T_resident = 1 / (λ_i * P_eviction) 在量纲和逻辑上存在严重缺陷：λ_i 通常指访问频率（次/时间），P_eviction 是概率（无量纲），乘积量纲为 1/时间，倒数确实是时间，但 LRU 的驻留时间并非简单由访问频率和驱逐概率的乘积倒数决定，而是取决于堆栈距离分布和缓存大小。此外，'中热度'范围 [50, 1000] 跨度极大，平均驻留时间不可能是一个固定值 1.5 天，除非有特定的归一化或特定场景假设，但陈述中未提供足够上下文支持这一具体数值。 | 先验知识/题面给定，逻辑校验未通过：公式推导缺乏理论依据，且数值合理性存疑

## Search Query

LRU stack distance model mean residence time formula
