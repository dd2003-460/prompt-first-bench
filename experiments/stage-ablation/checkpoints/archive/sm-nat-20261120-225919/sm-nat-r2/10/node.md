# N28: 理论常识（凭记忆）：LRU 在 Zipf/Pareto 分布下表现接近 LRU-OPT 的下界，且 LFU 在频率稳定时优于 LRU，但在频率突变时劣于 LRU

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

理论常识（凭记忆）：LRU 在 Zipf/Pareto 分布下表现接近 LRU-OPT 的下界，且 LFU 在频率稳定时优于 LRU，但在频率突变时劣于 LRU；通用公式 H ≈ 1 - (C/M)^β 常用于估算。

## Corrected Claim

LRU 在 Zipf/Pareto 分布下表现接近最优，LFU 在频率稳定时通常优于 LRU，但在频率突变时可能因历史频率滞后而表现不佳；命中率估算需结合具体分布模型，不存在单一的通用公式 H ≈ 1 - (C/M)^β。

## Evidence

[质询]公式 H ≈ 1 - (C/M)^β 并非通用的标准缓存命中率估算公式，其形式更接近于特定分布下的近似或经验拟合，缺乏普适性；且 LFU 在频率突变时劣于 LRU 的结论虽符合直觉，但具体表现高度依赖负载特征，并非绝对真理。 | 来源[2]支持 LRU 在 Zipf 分布下的分析，来源[1]提及 LRU 在扫描型负载下的颠簸（间接支持频率突变时的劣势），但无来源直接支持该特定通用公式，且该公式属于经验/特定模型结论，非第一性原理可严格推导的通用物理/数学定律，故降级。

## Retrieval Sources

- {'url': 'https://geek-doc.cn/concepts/cache/replacement-policies-lru&rut=a26d1fdd770a573d9abe957a30c2cf83c153dc874dc966ce3ba85b276efa38de', 'type': 'ddg', 'title': '缓存替换策略：Lru、随机、Lru 近似与自适应替换 | 极客工场'}
- {'url': 'https://www.booksci.cn/literaturecn/116452161.htm&rut=8e0cf6e0e2854e6b166e07e3bc245b0ce30f696703e1d25d4217062600df9408', 'type': 'ddg', 'title': '在Zipf请求下基于优惠券收集器的LRU缓存命中近似 - Book学术'}
- {'url': 'https://blog.csdn.net/arthur503/article/details/8513992&rut=14e87de1173f70c8af939550b07797e6108b96fb1db8bf6ca40fdffab4f50312', 'type': 'ddg', 'title': 'ZIPF分布、PARETO分布和幂律分布_zipf分布和pareto分布的关系-CSDN博客'}
