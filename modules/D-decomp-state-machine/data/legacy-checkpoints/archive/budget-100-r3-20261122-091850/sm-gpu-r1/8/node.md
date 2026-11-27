# N32: NVIDIA RTX 4090 24GB 显存无法在 BF16 (54GB) 或 FP8 (27GB) 下完整加载 Qwen3-27B 权重而不进行 Offlo

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

NVIDIA RTX 4090 24GB 显存无法在 BF16 (54GB) 或 FP8 (27GB) 下完整加载 Qwen3-27B 权重而不进行 Offload。在 W4 量化 (13.5GB 权重) 下，加上 8GB KV Cache (32K) 和 ~4GB 激活/开销，总计 ~25.5GB，超出 24GB 显存限制，必须使用 CPU Offload 或更激进的量化 (如 W3)，导致性能下降 >50%。因此，单张 RTX 4090 不满足 32K 上下文且无硬性延迟约束下的‘最佳’性价比，除非接受极慢的生成速度。

## Corrected Claim

NVIDIA RTX 4090 24GB 显存无法在 BF16 (54GB) 或 FP8 (27GB) 下完整加载 Qwen3-27B 权重而不进行 Offload。在 W4 量化 (13.5GB 权重) 下，加上 8GB KV Cache (32K) 和 ~4GB 激活/开销，总计 ~25.5GB，超出 24GB 显存限制，必须使用 CPU Offload 或更激进的量化 (如 W3)，导致性能下降 >50%。因此，单张 RTX 4090 不满足 32K 上下文且无硬性延迟约束下的‘最佳’性价比，除非接受极慢的生成速度。

## Evidence

检索失败: no sources from any channel (all 5 failed)
