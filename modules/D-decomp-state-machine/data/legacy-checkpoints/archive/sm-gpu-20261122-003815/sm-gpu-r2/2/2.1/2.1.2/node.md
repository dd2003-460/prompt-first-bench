# N72: Qwen3-27B 的注意力头数 (num_attention_heads) 为 40 个（基于 Qwen2.5-32B 的 40 头配置推断，需核实 Qwen

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

Qwen3-27B 的注意力头数 (num_attention_heads) 为 40 个（基于 Qwen2.5-32B 的 40 头配置推断，需核实 Qwen3 具体数值）。

## Corrected Claim

Qwen3-27B 的注意力头数 (num_attention_heads) 推测为 40 个（参考 Qwen2.5-32B 配置），但需查阅 Qwen3-27B 官方 config.json 以确认具体数值。

## Evidence

[质询]该陈述基于Qwen2.5-32B的架构参数（40头）进行推断，但Qwen3系列（包括27B）可能采用了不同的架构设计或参数配置，且参考来源均指向Qwen3.6/3.8版本，未提供Qwen3-27B的具体num_attention_heads数值，存在版本混淆和推断错误的风险。 | 参考来源[1][2][3]均讨论Qwen3.6或Qwen3.8-27B的架构，未直接提及Qwen3-27B的注意力头数；逻辑上40头对于27B模型是合理的量级（类似Qwen2.5-32B），但缺乏直接来源支持，属于经验事实且缺来源直接确认。

## Search Query

Qwen3-27B num_attention_heads head_dim config.json

## Retrieval Sources

- {'url': 'https://freedom-lwx.github.io/llm-architecture-handbook/04_Qwen3.6-27B/&rut=491048fbd02524bd361edaffe1d0de87ffd29f2609913dd907f9f50dc16b0f37', 'type': 'ddg', 'title': '04 · Qwen3.6-27B - 大模型架构学习手册'}
- {'url': 'https://www.happyrock.cloud/zh-cn/blog/2026-08-16_qwen3.8-27b/&rut=a2de2f5a5509fc2ff24d66748221cd21a8f8716aeb0d29798b057acc064170dc', 'type': 'ddg', 'title': 'Qwen3.8-27B混合注意力架构深度解析：48层Gated DeltaNet + 16层Attention如何让270亿参数模型跑在消费级 ...'}
- {'url': 'https://blog.csdn.net/liu8485/article/details/164724304&rut=b7c08168b53b511f68674c156d96aa9524b8914fb42107a4a9b9b614dca3f054', 'type': 'ddg', 'title': 'Qwen3.8-27B 混合注意力拆解：48 层线性 + 16 层全注意力，75 万 token KV 显存打到 1/4'}
