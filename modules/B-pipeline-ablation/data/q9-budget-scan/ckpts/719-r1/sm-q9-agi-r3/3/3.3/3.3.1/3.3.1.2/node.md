# N193: 草稿模型耗时比 β 的量化：在 V100 上测量 Qwen3.8-27B 草稿模型（若为同架构小模型）生成 4 tokens 的耗时与主模型生成 1 token

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N55

## Claim

草稿模型耗时比 β 的量化：在 V100 上测量 Qwen3.8-27B 草稿模型（若为同架构小模型）生成 4 tokens 的耗时与主模型生成 1 token 的耗时之比，预期 β = 0.3 ± 0.1，用于计算 Speedup 公式中的分子项。

## Corrected Claim

在 V100 上使用 Qwen3.8-27B 作为主模型进行推测解码时，若选用同架构的小模型作为草稿模型，生成 4 tokens 的耗时与主模型生成 1 token 的耗时之比（β）预计显著小于 1（具体数值需根据草稿模型规模实测确定，参考值可能在 0.2-0.5 区间），用于计算加速比。

## Evidence

[质询]该陈述包含具体的经验数值（β=0.3±0.1）和特定硬件/模型组合（V100, Qwen3.8-27B），属于经验事实。参考来源[1]虽然涉及Qwen3.8-27B在V100上的部署，但摘要中未提及“草稿模型”、“Speculative Decoding”或具体的“β比值”数据，无法直接支持该特定量化结论。此外，Qwen3.8-27B作为主模型时，其“同架构小模型”草稿模型的耗时比受具体小模型大小、量化精度及vLLM版本影响极大，0.3这一数值缺乏通用性，需具体实验支撑。 | 逻辑上，草稿模型通常比主模型小，生成多token的耗时与主模型生成单token耗时之比小于1是合理的（逻辑自洽）。但来源[1]仅涵盖Qwen3.8-27B的基础部署与基准测试，未提供Speculative Decoding中草稿模型耗时比β的具体实测数据，属于间接相关但无直接支持的经验事实。

## Search Query

Qwen3.8-27B draft model inference latency ratio V100

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2072074634476909289&rut=d97b6d9efd23719ef153d2ef7ccd044b4627c803640d57d09052962666bf48ca', 'type': 'ddg', 'title': 'Qwen3.8-27B 实测：V100 上的部署要点与 Q4/Q8 全量基准'}
