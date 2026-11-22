# N231: RTX 3090 (24GB) 运行 FP8 精度 Qwen3-27B (28.2GB) 的显存缺口为 4.2 GB，必须启用 CPU Offload 或降低上

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N108

## Claim

RTX 3090 (24GB) 运行 FP8 精度 Qwen3-27B (28.2GB) 的显存缺口为 4.2 GB，必须启用 CPU Offload 或降低上下文至 24K 以下才可行。

## Corrected Claim

RTX 3090 (24GB) 运行 FP8 精度 Qwen3-27B (28.2GB) 存在约 4.2 GB 显存缺口，通常需启用 CPU Offload 或限制上下文长度（具体阈值取决于框架和KV Cache大小）才能稳定运行。

## Evidence

[质询]显存需求计算过于简化，未考虑KV Cache动态增长及框架开销，且'必须'降低上下文至24K以下的阈值缺乏严谨推导，不同推理框架（如vLLM, llama.cpp）对显存管理策略不同，可能导致实际可行上下文长度差异较大。 | 经验事实，逻辑自洽但缺来源支持；RTX 3090 24GB显存小于模型权重28.2GB，确实存在显存缺口，需Offload或限制上下文，但具体阈值24K为经验估算值，非绝对物理限制。
