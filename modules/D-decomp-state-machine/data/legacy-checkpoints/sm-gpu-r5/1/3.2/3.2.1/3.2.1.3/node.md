# N139: Qwen3-27B 的 head_dim 参数值为 128（由 hidden_size 1024 / num_attention_heads 8 推导或直接从 

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N38

## Claim

Qwen3-27B 的 head_dim 参数值为 128（由 hidden_size 1024 / num_attention_heads 8 推导或直接从 config 读取），需确认是否所有层均使用相同 head_dim

## Corrected Claim

Qwen3-27B 的 hidden_size 远大于 1024（通常约为 4096 或更高），head_dim 通常为 128，但 num_attention_heads 应相应调整（如 32 或更多），而非 8。需查阅官方 config.json 确认具体数值。

## Evidence

[质询]数值量级与常见大模型架构直觉不符：Qwen3-27B 作为 27B 参数量的模型，其 hidden_size 通常远大于 1024（例如 Qwen2-7B 的 hidden_size 为 3584，27B 级别通常在 4000-5000 左右）。若 hidden_size 仅为 1024，则模型参数量将极小，与 27B 的命名严重矛盾。此外，head_dim 为 128 且 num_heads 为 8 意味着 hidden_size 必须是 1024，这与 27B 模型的典型配置（如 hidden_size 4096, num_heads 32, head_dim 128）存在巨大差异，极可能是将小模型（如 Qwen2-0.5B 或类似小参数量模型）的配置误植到了 27B 上，或者混淆了 hidden_size 与 head_dim 的关系。 | 来源 [2] 提及 Qwen3-27B 但未提供具体架构参数；来源 [1] 和 [3] 与 Qwen 模型架构无关。基于大语言模型参数量与 hidden_size 的经验关系（经验事实），27B 模型的 hidden_size 不可能仅为 1024，因此该陈述中的数值前提（hidden_size 1024）极大概率错误，导致推导出的 head_dim 结论不可靠。

## Search Query

Qwen3-27B head_dim 128 hidden_size 1024

## Retrieval Sources

- {'url': 'http://arxiv.org/abs/2405.14224v2', 'type': 'arxiv', 'title': 'DiM: Diffusion Mamba for Efficient High-Resolution Image Synthesis'}
- {'url': 'http://arxiv.org/abs/2608.13681v1', 'type': 'arxiv', 'title': 'Fine-Tuning Qwen3-27B for C-to-Rust Code Translation: A Three-Stage Curriculum o'}
- {'url': 'http://arxiv.org/abs/1610.01832v1', 'type': 'arxiv', 'title': 'Epiphany-V: A 1024 processor 64-bit RISC System-On-Chip'}
