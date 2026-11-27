# N26: LFU相较于LRU的理论增益上限源于频率排序避免缓存低频大对象，增益上限ΔH = H_LFU - H_LRU，其中H_LFU = ∑_{i∈F} (h_i * 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LFU相较于LRU的理论增益上限源于频率排序避免缓存低频大对象，增益上限ΔH = H_LFU - H_LRU，其中H_LFU = ∑_{i∈F} (h_i * s_i) / ∑_{i=1}^{N} (h_i * s_i)，F为LFU驻留集合（按频率排序）。

## Corrected Claim

LFU相较于LRU的优势在于通过频率排序优先保留高频访问对象，从而在访问模式符合幂律分布等场景下提升缓存命中率。具体的命中率增益取决于访问模式，通常定义为 H = Hits / Total Requests，而非简单的加权频率比。

## Evidence

[质询]该公式将命中率（Hit Rate）定义为加权频率/总加权频率，这在数学上仅当所有对象访问频率相等或特定条件下才等价于传统命中率（命中次数/总请求次数）。此外，'理论增益上限'这一表述缺乏严谨的数学推导支持，通常LFU与LRU的性能差异取决于访问模式（如Zipf分布），而非简单的频率排序公式差值。 | 来源[1]仅定性描述了LRU和LFU的区别（LRU看最近访问，LFU看频率），未提供具体的命中率计算公式或理论增益上限的数学定义，属于间接支持/无关。该公式逻辑上自洽（作为某种加权指标的定义），但作为'命中率'的标准定义存在口径混淆风险，且缺乏来源直接支持。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2069556046839001951&rut=7d58a4a126ac95d842e1a792f5b31de9d44ec9b6d2a091d938002417e9278387', 'type': 'ddg', 'title': '吃透Redis缓存核心：淘汰策略、LRU/LFU区别与四大缓存问题全解'}
