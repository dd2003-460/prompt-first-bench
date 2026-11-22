# N82: RTX 5090 在 BF16 精度下解码 Qwen3-27B (Batch Size=1) 的理论最大吞吐量上限为 显存带宽(1792 GB/s) / 单次解

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N18

## Claim

RTX 5090 在 BF16 精度下解码 Qwen3-27B (Batch Size=1) 的理论最大吞吐量上限为 显存带宽(1792 GB/s) / 单次解码读取字节数(54 GB) ≈ 33.2 tokens/s，实际吞吐量需乘以内存带宽利用率系数 (通常 0.6-0.8) 得出 20-26 tokens/s。

## Corrected Claim

RTX 5090 在 BF16 精度下解码 Qwen3-27B (Batch Size=1) 的理论最大吞吐量上限为 显存带宽(1792 GB/s) / 单次解码读取字节数(54 GB) ≈ 33.2 tokens/s，实际吞吐量需乘以内存带宽利用率系数 (通常 0.6-0.8) 得出 20-26 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090显存带宽1792GB/s与Qwen3-27B BF16权重约54GB符合硬件与模型规格，计算33.2 tokens/s及利用率修正后的20-26 tokens/s在逻辑与量级上均合理。
