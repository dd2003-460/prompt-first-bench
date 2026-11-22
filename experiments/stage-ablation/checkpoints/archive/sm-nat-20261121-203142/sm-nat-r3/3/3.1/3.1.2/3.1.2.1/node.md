# N119: LFU 驻留分布偏移量化：f_R(r|s)_LFU 相比 f_R(r|s)_LRU 在 s < s_median 且 r > r_median 区域的概率质量增

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N45

## Claim

LFU 驻留分布偏移量化：f_R(r|s)_LFU 相比 f_R(r|s)_LRU 在 s < s_median 且 r > r_median 区域的概率质量增加量 ΔP_hot_small，需通过模拟 10 万对象在 128GB 缓存下的驻留状态统计得出，预期 ΔP 在 5-15% 区间

## Corrected Claim

LFU 驻留分布相比 LRU 在 s < s_median 且 r > r_median 区域的概率质量通常会有所增加（ΔP_hot_small > 0），具体增量取决于工作负载特征及缓存配置，需通过模拟统计得出。

## Evidence

[质询]该陈述包含具体的经验性数值区间（5-15%）和特定的模拟参数（10万对象、128GB缓存），属于经验事实而非第一性原理可推导的数学性质。在缺乏具体工作负载特征（如Zipf指数、对象大小分布）的情况下，断言一个固定的概率质量增加区间缺乏普适性，且无来源支持该特定数值范围。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且数值区间依赖具体模拟条件，无法从第一性原理严格推出固定值）

## Search Query

LFU vs LRU cache hit rate simulation Pareto distribution negative correlation
