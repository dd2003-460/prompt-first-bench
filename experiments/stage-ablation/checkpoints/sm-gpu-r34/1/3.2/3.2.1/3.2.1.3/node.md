# N139: Qwen3-27B 的 head_dim 参数值为 128（由 hidden_size 1024 / num_attention_heads 8 推导或直接从 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N38

## Claim

Qwen3-27B 的 head_dim 参数值为 128（由 hidden_size 1024 / num_attention_heads 8 推导或直接从 config 读取），需确认是否所有层均使用相同 head_dim

## Corrected Claim

Qwen3-27B 的 head_dim 参数值需查阅官方 config 确认；若 hidden_size 为 1024 且 num_attention_heads 为 8，则 head_dim 为 128，但该 hidden_size 数值存疑，建议核实实际 hidden_size（通常 27B 模型 hidden_size 远大于 1024）。

## Evidence

[质询]数值量级与常见大模型架构直觉不符：Qwen3-27B 作为 27B 参数量的模型，其 hidden_size 通常远大于 1024（例如 Qwen2-7B 的 hidden_size 为 3584，27B 级别通常在 4000-5000 左右）。若 hidden_size 仅为 1024，则参数量难以达到 27B（除非层数极多或 FFN 极宽，但这不符合常规 Transformer 设计）。此外，num_attention_heads 为 8 对于 27B 模型也偏少（通常 32-64 头）。因此，'hidden_size 1024' 这一前提极可能是错误的，导致推导出的 head_dim=128 虽然数学上自洽（1024/8=128），但基于错误的前提。 | 来源 [3] 提及 Qwen3-27B 但未提供具体 config 参数；其他来源无关。逻辑上 1024/8=128 成立，但经验事实（hidden_size 数值）缺乏来源支持且与常规大模型架构直觉冲突，无法验证 hidden_size 是否为 1024。

## Search Query

Qwen3-27B head_dim 128 hidden_size 1024

## Retrieval Sources

- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'http://arxiv.org/abs/2405.14224v2', 'type': 'arxiv', 'title': 'DiM: Diffusion Mamba for Efficient High-Resolution Image Synthesis'}
- {'url': 'http://arxiv.org/abs/2608.13681v1', 'type': 'arxiv', 'title': 'Fine-Tuning Qwen3-27B for C-to-Rust Code Translation: A Three-Stage Curriculum o'}
- {'url': 'http://arxiv.org/abs/1610.01832v1', 'type': 'arxiv', 'title': 'Epiphany-V: A 1024 processor 64-bit RISC System-On-Chip'}
