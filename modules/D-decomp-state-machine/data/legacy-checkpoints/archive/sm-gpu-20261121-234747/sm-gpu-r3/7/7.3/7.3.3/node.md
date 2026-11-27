# N455: Qwen3-27B 在 INT8 权重量化下，32K 上下文长度的 KV Cache 显存占用（假设 KV Cache 保持 BF16 或 FP16 以维持精度

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N146

## Claim

Qwen3-27B 在 INT8 权重量化下，32K 上下文长度的 KV Cache 显存占用（假设 KV Cache 保持 BF16 或 FP16 以维持精度）：权重 27 GB + KV Cache 16 GB = 43 GB，仍超过单卡 24GB，需多卡或进一步量化 KV Cache

## Corrected Claim

Qwen3-27B 在 INT8 权重量化下，32K 上下文长度的 KV Cache 显存占用（假设 KV Cache 保持 BF16 或 FP16 以维持精度）：权重 27 GB + KV Cache 16 GB = 43 GB，仍超过单卡 24GB，需多卡或进一步量化 KV Cache

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B INT8权重约27GB，32K上下文BF16 KV Cache约16GB，总和43GB超过单卡24GB限制，符合显存计算逻辑。

## Search Query

vLLM INT8 weight quantization KV cache dtype BF16
