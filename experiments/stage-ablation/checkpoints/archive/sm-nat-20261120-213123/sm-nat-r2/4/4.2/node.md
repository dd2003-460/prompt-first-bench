# N18: 访问局部性优势来源量化：LFU通过频率计数抑制'一次性'大对象的缓存驻留。量化指标为'污染代价' Reduction = (LRU中被一次性对象占用的缓存空间字

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

访问局部性优势来源量化：LFU通过频率计数抑制'一次性'大对象的缓存驻留。量化指标为'污染代价' Reduction = (LRU中被一次性对象占用的缓存空间字节数 / 总缓存空间) - (LFU中对应值)。在Pareto(β=0.9)热度分布下，一次性对象占请求次数比例高但字节占比低，LFU在此维度的收益有限，主要收益来自避免频繁替换热门小对象。

## Corrected Claim

访问局部性优势来源量化：LFU通过频率计数抑制'一次性'大对象的缓存驻留。量化指标为'污染代价' Reduction = (LRU中被一次性对象占用的缓存空间字节数 / 总缓存空间) - (LFU中对应值)。在Pareto(β=0.9)热度分布下，一次性对象占请求次数比例高但字节占比低，LFU在此维度的收益有限，主要收益来自避免频繁替换热门小对象。

## Evidence

父节点级核验未通过：不完备（子节点之间存在逻辑依赖但主题正交（分别定义T_LRU、k_eff近似、D边界、H_lfu计算）。然而，父节点的核心目标是量化'污染代价 Reduction'（即LRU与LFU在一次性大对象占用缓存空间上的差异），而子节点仅提供了T_LRU、H_lfu等中间变量的公式，缺失了关键的'一次性对象占比'或'污染代价'本身的直接计算逻辑，也未明确LFU中对应值的计算方式，导致无法直接得出父节点所述的Reduction指标，完备性不足。）

## Search Query

cache pollution cost LFU frequency threshold one-time objects
