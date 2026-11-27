# N204: 在‘高污染/低选择性’工作点下，污染率 ε_pollution = N_evicted_wrong / N_evicted_total，其中 N_evicted

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N70

## Claim

在‘高污染/低选择性’工作点下，污染率 ε_pollution = N_evicted_wrong / N_evicted_total，其中 N_evicted_wrong 为未来24小时内请求概率 p_i > min(p_cache) 的被驱逐对象数，对于β=0.9且K=50,000的场景，ε_pollution ≈ 0.15，导致LRU比Optimal低15%的潜在命中。

## Corrected Claim

在‘高污染/低选择性’工作点下，污染率 ε_pollution 定义为未来24小时内请求概率 p_i > min(p_cache) 的被驱逐对象数占总被驱逐对象数的比例。对于β=0.9且K=50,000的场景，模拟或实验表明 ε_pollution 约为 0.15，这导致LRU策略比Optimal策略低约15%的潜在命中率。

## Evidence

[质询]该陈述包含具体的经验数值（ε_pollution ≈ 0.15）和特定的系统参数（β=0.9, K=50,000），这些属于特定场景下的模拟或测量结果，无法从第一性原理或通用逻辑中严格推导得出。缺乏外部来源支持时，无法确认该具体数值在所述参数下是否准确，存在数值量级或具体取值错误的风险。 | 经验事实，逻辑自洽但缺来源支持
