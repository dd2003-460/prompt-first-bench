# N197: Apple M3 Ultra 的最大统一内存容量预计为 256 GB (基于 M2 Ultra 192GB 上限及 LPDDR5X 颗粒密度提升趋势)，需验证该

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N61

## Claim

Apple M3 Ultra 的最大统一内存容量预计为 256 GB (基于 M2 Ultra 192GB 上限及 LPDDR5X 颗粒密度提升趋势)，需验证该容量是否足以容纳 Qwen3-27B BF16 权重 (~54GB) 及 32K 上下文 KV Cache (~4-8GB)。

## Corrected Claim

Apple M3 Ultra 的最大统一内存容量预计为 256 GB（基于趋势推测，待官方确认），该容量在理论上足以容纳 Qwen3-27B BF16 权重 (~54GB) 及 32K 上下文 KV Cache (~4-8GB)。

## Evidence

[质询]该陈述包含具体的硬件规格预测（M3 Ultra 256GB）和模型资源估算（Qwen3-27B 54GB），属于经验事实。参考来源 [1] 是一篇关于 3D 空间多模态记忆的学术论文，与 Apple 芯片硬件规格及 LLM 部署完全无关，无法提供外部支持。此外，M3 Ultra 的具体内存上限在发布前属于推测，且 Qwen3-27B 的具体参数量及 BF16 权重大小需依据官方发布数据，当前陈述基于趋势推测，缺乏确凿来源。 | 参考来源 [1] 与事实主题无关（无可用外部证据）。逻辑上，256GB 内存容纳 54GB 权重及 8GB KV Cache 在算术上成立，但作为经验事实（硬件规格/模型参数），因缺乏直接来源支持，依据经验事实排除条款降级。

## Search Query

Apple M3 Ultra max unified memory 256GB specs

## Retrieval Sources

- {'url': 'http://arxiv.org/abs/2503.16413v1', 'type': 'arxiv', 'title': 'M3: 3D-Spatial MultiModal Memory'}
