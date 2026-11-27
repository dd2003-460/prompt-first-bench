# N165: 量化热门小对象（S < Median, R > Top 10%）在 LRU 缓存中的实际驻留占比 P_hot_small，与独立假设下的理论占比 P_indep

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N64

## Claim

量化热门小对象（S < Median, R > Top 10%）在 LRU 缓存中的实际驻留占比 P_hot_small，与独立假设下的理论占比 P_indep 之差 ΔP = P_hot_small - P_indep，该差值直接转化为命中率提升项

## Corrected Claim

量化热门小对象在LRU缓存中的实际驻留占比与独立假设下的理论占比之差，通常与命中率提升存在正相关关系，但具体转化系数取决于工作负载特征和缓存替换策略细节。

## Evidence

[质询]该陈述将复杂的缓存行为简化为简单的差值转化，忽略了LRU缓存中对象大小对驱逐策略的非线性影响以及工作负载的动态特性，属于经验性工程结论而非第一性原理可推导的数学恒等式。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

LRU cache hit rate correlation object size popularity negative correlation quantification
