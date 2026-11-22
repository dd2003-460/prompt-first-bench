# N109: EPYC 9654 (128核, 3TB DDR5) 的内存带宽为 3TB * 2 (DDR5 双通道) * 4800 MT/s * 1 (8通道) / 8 ≈

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N23

## Claim

EPYC 9654 (128核, 3TB DDR5) 的内存带宽为 3TB * 2 (DDR5 双通道) * 4800 MT/s * 1 (8通道) / 8 ≈ 2.304 TB/s，Qwen3-27B W4 权重 13.5GB，理论最大解码吞吐量为 2304 / 13.5 ≈ 170.7 tokens/s（假设无其他瓶颈）。

## Corrected Claim

EPYC 9654 配备 12 通道 DDR5-4800，理论内存带宽约为 460.8 GB/s。Qwen3-27B W4 权重约 13.5GB，但解码吞吐量受限于计算单元（FLOPS）和 KV Cache 带宽，不能简单通过内存带宽除以权重大小得出 170.7 tokens/s。

## Evidence

[质询]计算逻辑存在严重错误：1. 内存带宽公式错误，DDR5 带宽计算应为 通道数 * 速率 * 字节数，而非乘以容量（3TB）；2. 吞吐量计算错误，将带宽（TB/s）除以权重大小（GB）得到的单位是 GB/s，而非 tokens/s，且未考虑模型架构（如 KV Cache 大小、计算瓶颈等），该推导在物理和工程上均不成立。 | 逻辑校验失败：带宽计算误用容量参数，吞吐量推导量纲错误且忽略计算瓶颈，属于硬逻辑错误。
