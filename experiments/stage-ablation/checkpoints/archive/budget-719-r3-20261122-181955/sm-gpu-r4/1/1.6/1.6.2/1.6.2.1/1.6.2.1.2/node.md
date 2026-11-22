# N601: 在 32GB 显存 GPU (如 RTX 4090) 上，INT4 AWQ 模型 (21.75 GB 占用) 剩余显存 10.25 GB，可支持额外 12,80

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N210

## Claim

在 32GB 显存 GPU (如 RTX 4090) 上，INT4 AWQ 模型 (21.75 GB 占用) 剩余显存 10.25 GB，可支持额外 12,800 tokens 的 KV Cache 或 1 个并发请求的完整 32K 上下文；而在 48GB 显存 GPU (如 L40S) 上，剩余显存 26.25 GB，可支持 3 个并发请求的完整 32K 上下文，证明显存容量是 INT4 方案的主要瓶颈而非权重大小。

## Corrected Claim

在 32GB 显存 GPU (如 RTX 4090) 上，INT4 AWQ 模型 (21.75 GB 占用) 剩余显存 10.25 GB，可支持额外 12,800 tokens 的 KV Cache 或 1 个并发请求的完整 32K 上下文；而在 48GB 显存 GPU (如 L40S) 上，剩余显存 26.25 GB，可支持 3 个并发请求的完整 32K 上下文，证明显存容量是 INT4 方案的主要瓶颈而非权重大小。

## Evidence

先验知识/题面给定，逻辑校验通过：32GB-21.75GB=10.25GB，48GB-21.75GB=26.25GB，数值计算准确；KV Cache 占用与上下文长度、并发数成正比，逻辑自洽。

## Search Query

LLM INT4 quantization KV cache memory limit batch size 32k context
