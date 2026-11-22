# N101: AMD MI300X 显存带宽为 5.3 TB/s (HBM3)，运行 Qwen3-27B BF16 (54GB) + 32K 上下文 (KV 36GB + A

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23, N24, N25

## Claim

AMD MI300X 显存带宽为 5.3 TB/s (HBM3)，运行 Qwen3-27B BF16 (54GB) + 32K 上下文 (KV 36GB + Act 5GB = 95GB)，显存充足且带宽极高，理论解码吞吐 ≈ 5300 GB/s / 95GB ≈ 55.8 tokens/s，实际效率系数 0.8 下为 44.6 tokens/s。

## Corrected Claim

AMD MI300X 显存带宽为 5.3 TB/s (HBM3)，运行 Qwen3-27B BF16 (54GB) + 32K 上下文 (KV 36GB + Act 5GB = 95GB)，显存充足且带宽极高，理论解码吞吐 ≈ 5300 GB/s / 95GB ≈ 55.8 tokens/s，实际效率系数 0.8 下为 44.6 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：MI300X 5.3TB/s 带宽与 128GB HBM3 容量符合公开规格，54GB 模型+36GB KV+5GB 激活值=95GB 在 128GB 内，算术推导 5300/95≈55.8 及 0.8 效率系数计算正确。
