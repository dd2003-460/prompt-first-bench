# N314: NVIDIA H100 80GB PCIe 在 Qwen3-27B BF16 权重下的显存占用与 32K 上下文支持：权重 54GB + KV Cache (3

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

NVIDIA H100 80GB PCIe 在 Qwen3-27B BF16 权重下的显存占用与 32K 上下文支持：权重 54GB + KV Cache (32K, BF16) 8.6GB + 激活 3.0GB = 65.6GB < 80GB，余量 14.4GB，支持高并发 (Batch=4) 或 64K 上下文；其原生 FP8 Tensor Core 使得 FP8 权重方案 (27GB) 显存余量扩大至 43GB，成为高吞吐数据中心场景的首选，但 TCO 远高于消费级方案。

## Corrected Claim

NVIDIA H100 80GB PCIe 在 Qwen3-27B BF16 权重下的显存占用与 32K 上下文支持：权重 54GB + KV Cache (32K, BF16) 8.6GB + 激活 3.0GB = 65.6GB < 80GB，余量 14.4GB，支持高并发 (Batch=4) 或 64K 上下文；其原生 FP8 Tensor Core 使得 FP8 权重方案 (27GB) 显存余量扩大至 43GB，成为高吞吐数据中心场景的首选，但 TCO 远高于消费级方案。

## Evidence

检索失败: no sources from any channel (all 5 failed)
