# N48: 2×RTX 4090 (PCIe 4.0 x16, 64 GB/s) 运行 Qwen3-27B BF16 时，Tensor Parallelism 每层通信量约

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

2×RTX 4090 (PCIe 4.0 x16, 64 GB/s) 运行 Qwen3-27B BF16 时，Tensor Parallelism 每层通信量约为 2 × 27B × 2 bytes = 108 GB，理论通信延迟为 108 / 64 ≈ 1.7 秒/层，导致总解码延迟不可接受，需通过 All-Reduce 优化或降低并行度来缓解。

## Corrected Claim

2×RTX 4090 运行 Qwen3-27B BF16 时，Tensor Parallelism 每层通信量约为该层参数量×2 bytes（远小于 108GB），理论通信延迟极低，通常不是主要瓶颈，主要瓶颈在于显存带宽和计算能力。

## Evidence

[质询]数值量级严重错误：27B 参数模型 BF16 权重总大小约为 54GB，而非 108GB；且 Tensor Parallelism 每层通信量取决于该层参数量（约 27B/层数），绝非全模型参数量，108GB/层的通信量在物理上不可能。 | 逻辑校验失败：27B 模型 BF16 总权重约 54GB，陈述中 2×27B×2=108GB 计算错误且混淆了全模型与单层参数量，导致通信延迟估算完全失真。
