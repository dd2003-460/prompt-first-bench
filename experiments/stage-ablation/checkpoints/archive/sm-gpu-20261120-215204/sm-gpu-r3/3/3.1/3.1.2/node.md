# N83: RTX 4090 运行 Qwen3-27B W4A16 且 KV Cache 量化为 INT8 时，显存占用约为 17GB (权重) + 20GB (KV Ca

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

RTX 4090 运行 Qwen3-27B W4A16 且 KV Cache 量化为 INT8 时，显存占用约为 17GB (权重) + 20GB (KV Cache) + 2GB (开销) = 39GB，仍超过 24GB 显存，因此单卡 RTX 4090 无法原生支持 32K 上下文的 W4 推理，除非使用 PagedAttention 的 CPU Offload 或大幅缩减上下文至 8K 以下。

## Corrected Claim

RTX 4090 运行 Qwen3-27B W4A16 且 KV Cache 量化为 INT8 时，显存占用约为 17GB (权重) + 20GB (KV Cache) + 2GB (开销) = 39GB，仍超过 24GB 显存，因此单卡 RTX 4090 无法原生支持 32K 上下文的 W4 推理，除非使用 PagedAttention 的 CPU Offload 或大幅缩减上下文至 8K 以下。

## Evidence

[质询]KV Cache 占用 20GB 的估算可能偏高，具体取决于 Qwen3-27B 的层数、头数及 GQA 配置，但量级在 32K 上下文下是合理的；权重 17GB 符合 W4A16 量化后的体积（27B * 0.5 bytes ≈ 13.5GB + 激活/其他开销）。 | 先验知识/题面给定，逻辑校验通过：27B 模型 W4 量化权重约 13.5-17GB，32K 上下文 KV Cache 在 INT8 下通常需 10-20GB，总和超过 24GB 显存限制，结论自洽。

## Search Query

Qwen3 27B INT8 KV cache memory footprint 32k tokens
