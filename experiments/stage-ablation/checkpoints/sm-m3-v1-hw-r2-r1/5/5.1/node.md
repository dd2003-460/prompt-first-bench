# N24: 长上下文衰减曲线未知区：Qwen3.8-27B 在 128k-262k token 区间的信息保持率（Retrieval Accuracy）尚未公开基准，预估从

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

长上下文衰减曲线未知区：Qwen3.8-27B 在 128k-262k token 区间的信息保持率（Retrieval Accuracy）尚未公开基准，预估从 95% 线性衰减至 70%，需通过 Needle-in-a-Haystack 测试验证

## Corrected Claim

Qwen3.8-27B 在 128k-262k token 区间的信息保持率（Retrieval Accuracy）缺乏公开的标准化基准数据，其具体衰减曲线需通过 Needle-in-a-Haystack 等测试进行实证验证，目前仅有基于长上下文性能的一般性推测，无确切数值。

## Evidence

[质询]该陈述包含具体的经验性预测数值（95%线性衰减至70%），这属于未经证实的经验假设，而非可从第一性原理推导的数学或物理事实；且参考来源仅涉及上下文长度配置（256K/1M）及部署方法，完全未提供关于信息保持率（Retrieval Accuracy）的具体基准数据或衰减曲线证据。 | 来源[1][2][3]仅确认了Qwen3.8-27B支持256K-1M上下文的技术可行性，但未提供任何关于128k-262k区间信息保持率的具体数值或衰减趋势，属于经验事实且缺乏来源支持。

## Search Query

Qwen3.8 27B long context retrieval accuracy 128k 256k needle in haystack benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/ONE_SIX_MIX/article/details/163801085&rut=6232c869106d9b2db39a83444dbcec5ad37d48304861216778a5dad4efac157f', 'type': 'ddg', 'title': 'llama-server 部署 Qwen3.8-27B：真正开启 512K 上下文，突破 256K 截断'}
- {'url': 'https://blog.csdn.net/gitblog_01045/article/details/152195953&rut=19cfddfde1c211de4ceffa3ca34ddf91e16ccedc4db8c1316404559d63de3442', 'type': 'ddg', 'title': 'Qwen3.8-27B-FP8 超长上下文实战：如何用 YaRN 把 262K 扩展到 1M tokens？-CSDN博客'}
- {'url': 'https://iqilian.com/learn/qwen38-1m-haishi-262144/&rut=e6351728e1a04c87ee3a136c389c111cd582806b3038cf2ae64da4f0410ef894', 'type': 'ddg', 'title': 'Qwen3.8-27B 的上下文长度：256K、262144 还是 1M，四处口径'}
