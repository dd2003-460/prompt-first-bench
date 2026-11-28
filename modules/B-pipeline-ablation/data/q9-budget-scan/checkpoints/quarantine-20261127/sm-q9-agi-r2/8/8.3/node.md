# N96: Prompt 压缩策略（如 LLMLingua-2）可将上下文长度压缩 2-3x 而不显著降低关键信息保留率（保留率 > 90%），但在压缩过程中可能丢失细微的

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

Prompt 压缩策略（如 LLMLingua-2）可将上下文长度压缩 2-3x 而不显著降低关键信息保留率（保留率 > 90%），但在压缩过程中可能丢失细微的逻辑连接词，导致复杂推理链断裂率上升 5-10%；建议仅对背景文献部分应用压缩，保留核心假设与实验数据原样。

## Corrected Claim

Prompt 压缩策略（如 LLMLingua-2）可将上下文长度压缩数倍而在下游任务性能上保持基本不变，但可能在极端情况下丢失细微逻辑连接词；建议谨慎应用于核心推理部分，优先压缩背景文献。

## Evidence

[质询]陈述中关于“复杂推理链断裂率上升 5-10%”的具体数值缺乏来源支持，且“保留率 > 90%”的量化指标在提供的摘要中未明确体现，属于未经证实的经验性具体参数。 | 来源 [1][2][3] 确认了 LLMLingua-2 可实现数倍压缩且保持性能基本不变（间接支持压缩可行性和低损失），但未提供具体的“5-10% 断裂率”或“>90% 保留率”数据，属经验事实缺具体来源支持。

## Search Query

LLMLingua-2 prompt compression accuracy retention logical reasoning integrity loss rate

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00943/article/details/167899970&rut=b34eae4ed07d0957e5bd22ac0032031150032bfbb26f32bc25a632fa69b1be78', 'type': 'ddg', 'title': 'LLMLingua 系列 Prompt 压缩技术实战指南：从基础用法到 LLMLingua-2 自定义训练-CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00885/article/details/167909846&rut=1b2e286c675e2397ab89712dc9d7d8f1e0036285f7f9c56377fb04542d5ebd7d', 'type': 'ddg', 'title': 'LLMLingua 提示词压缩实战指南：从 20x 压缩原理到 LongLLMLingua / LLMLingua-2'}
- {'url': 'https://www.dafei.me/posts/llmlingua-prompt-compression/&rut=ef08ca4b1fa6bc3e48f17d13bd8185c74caa40cb299df247903c3c20a3a48753', 'type': 'ddg', 'title': 'LLMLingua：用小模型压缩 Prompt，省 95% Token | 大飞的博客'}
