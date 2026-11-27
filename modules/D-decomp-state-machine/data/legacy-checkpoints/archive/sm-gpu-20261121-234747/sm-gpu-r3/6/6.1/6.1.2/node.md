# N428: Qwen3-27B的num_hidden_layers具体数值需从HuggingFace官方config.json中提取，预期值约为32（基于27B参数规模估算

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N138

## Claim

Qwen3-27B的num_hidden_layers具体数值需从HuggingFace官方config.json中提取，预期值约为32（基于27B参数规模估算），该值直接决定KV Cache总层数和权重总层数，影响显存占用和计算量。

## Corrected Claim

Qwen3-27B的num_hidden_layers具体数值需从HuggingFace官方config.json中提取，该值直接决定KV Cache总层数和权重总层数，影响显存占用和计算量。

## Evidence

[质询]该陈述包含具体的硬件/模型架构参数（num_hidden_layers=32），属于经验事实。虽然27B模型通常对应32层左右（如Llama-3-70B为80层，Qwen2-72B为80层，但Qwen2-7B为28层，Qwen2-14B为48层，Qwen2-32B为64层，Qwen2-72B为80层；Qwen3系列具体配置需查证，且不同模型家族层数设计不同，不能仅凭参数量简单线性估算为32，例如Qwen2-72B是80层，Qwen2-32B是64层，27B若为32层则每层参数量极大，不符合常规Transformer设计比例，更可能是48或64层左右，或者该数值纯属猜测且未经验证）。此外，来源缺失导致无法确认具体数值。 | 经验事实，逻辑自洽但缺来源支持。num_hidden_layers是具体模型配置参数，属于经验事实，不能仅从第一性原理推出。由于检索无可用来源，且27B模型层数估算存在不确定性（不同架构设计差异大），无法直接验证为32，故降级。

## Search Query

Qwen3-27B config.json num_hidden_layers
