# N112: RTX 4090 (24GB) 在 INT8 量化下运行 Qwen3-27B 的显存占用为 27GB (权重) + 4.09GB (KV Cache) + 1.

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

RTX 4090 (24GB) 在 INT8 量化下运行 Qwen3-27B 的显存占用为 27GB (权重) + 4.09GB (KV Cache) + 1.5GB (框架) = 32.59GB，超出 24GB 显存限制，故单卡部署不可行；若采用 2×4090 张量并行，总显存 48GB，单卡负载 16.3GB，可行但需 PCIe 5.0 互联。

## Corrected Claim

RTX 4090 (24GB) 在 INT8 量化下运行 Qwen3-27B 时，权重占用约 13.5GB，加上 KV Cache 和框架开销，总显存需求可能超过 24GB，单卡部署可能不可行；若采用 2×4090 张量并行，总显存 48GB，单卡负载约 16.3GB，可行但需高速互联。

## Evidence

[质询]KV Cache 占用 4.09GB 的数值缺乏上下文（如序列长度、Batch Size），属于经验估算值，且不同推理框架（如 vLLM, TensorRT-LLM）的显存开销差异较大，1.5GB 框架开销亦为粗略估计；此外，24GB 显存通常无法容纳 27GB 权重，即使量化后权重约 13.5GB (INT8)，加上 KV Cache 和激活值，单卡 24GB 确实紧张，但具体数值 32.59GB 的构成细节（特别是 KV Cache 和框架开销）缺乏精确来源支持，属于经验事实。 | 经验事实，逻辑自洽但缺来源支持；INT8 量化下 27B 模型权重约 13.5GB，加上 KV Cache 和框架开销，单卡 24GB 确实可能不足，但具体数值 32.59GB 为估算值，无直接来源支持。
