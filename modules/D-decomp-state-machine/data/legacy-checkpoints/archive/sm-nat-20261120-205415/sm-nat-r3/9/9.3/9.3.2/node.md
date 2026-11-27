# N226: LFU增益估算的基准工作点（ρ=-0.3, Gaussian）：假设F平均大小0.7MB，L平均大小1.3MB，H_LFU/H_LFU≈(0.7*∑h_F)/(

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N83

## Claim

LFU增益估算的基准工作点（ρ=-0.3, Gaussian）：假设F平均大小0.7MB，L平均大小1.3MB，H_LFU/H_LFU≈(0.7*∑h_F)/(1.3*∑h_L)≈0.95-0.97，ΔH≈3-5%，量化中等负相关下的增益。

## Corrected Claim

在假设F平均大小0.7MB、L平均大小1.3MB且存在中等负相关（ρ=-0.3）的特定基准工作点下，LFU相对于LRU的命中率增益估算约为3-5%（H_LFU/H_LRU≈0.95-0.97），该数值为特定假设下的估算值，需结合具体工作负载验证。

## Evidence

[质询]该陈述包含具体的经验参数（F/L平均大小、ρ值、增益百分比），属于经验事实而非第一性原理可推导内容；且参考来源仅讨论LRU/LFU自适应的必要性，未提供具体的数值估算或基准工作点数据，无法直接支持该具体数值结论。 | 逻辑上量纲和比例关系自洽（0.7/1.3 ≈ 0.54，若考虑频率分布差异，0.95-0.97的比值在特定假设下可能成立，但缺乏具体推导细节）；来源[1]主题相关但仅定性讨论，未提供具体数值支持，属于间接支持或无关，故降级。

## Search Query

LFU LRU cache hit rate ratio size distribution negative correlation 0.3 Pareto

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/679259506&rut=f013bbe63c240c69fef131a2de419b94200af7a6c469968c442400d1fc8a8540', 'type': 'ddg', 'title': 'Lru Lfu 自适应算法设计纲要 - 知乎'}
