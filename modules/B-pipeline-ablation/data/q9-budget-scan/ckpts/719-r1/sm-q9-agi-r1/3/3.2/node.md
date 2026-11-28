# N14: 在 max-num-seqs=8 并发设置下，KV Cache (FP8) 占用显存占比与最大可容纳序列长度的关系，以及因显存溢出导致的 OOM (Out-of

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

在 max-num-seqs=8 并发设置下，KV Cache (FP8) 占用显存占比与最大可容纳序列长度的关系，以及因显存溢出导致的 OOM (Out-of-Memory) 触发阈值。

## Corrected Claim

在 max-num-seqs=8 并发设置下，KV Cache (FP8) 占用显存随最大可容纳序列长度增加而线性增长，当总显存需求超过可用显存时触发 OOM，具体阈值取决于模型架构及硬件配置。

## Evidence

[质询]该陈述包含具体的经验参数（max-num-seqs=8, FP8, 具体OOM阈值），属于经验事实，无法从第一性原理直接推出，且参考来源未提供针对此特定配置的具体数值或阈值，存在缺乏直接证据支持的风险。 | 来源[1]间接支持KV Cache显存随并发和序列长度动态增长的基本逻辑，但未提供max-num-seqs=8及FP8下的具体OOM阈值数据，属经验事实缺直接来源支持。

## Search Query

vLLM KV cache memory usage FP8 concurrent sequences OOM threshold V100

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1984939680643452933&rut=8f7f41e10e6bccd7bbcaa702b39b42bdb7d0b0dd68e1697a3ee89efab63af159', 'type': 'ddg', 'title': '模型推理时KV Cache显存如何计算，和用户并发有什么关系？'}
