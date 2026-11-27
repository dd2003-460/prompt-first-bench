# N185: A100 80GB SXM4 的 HBM2e 显存带宽 2039 GB/s 是由 5120-bit 位宽和 1593 MHz 等效频率 (3186 MT/s) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48, N49, N50

## Claim

A100 80GB SXM4 的 HBM2e 显存带宽 2039 GB/s 是由 5120-bit 位宽和 1593 MHz 等效频率 (3186 MT/s) 计算得出 (5120/8 * 3186e6 / 1e9 ≈ 2039 GB/s)，该带宽是决定 LLM 解码阶段 (Decode) 吞吐量上限的核心参数，公式为 Throughput ≈ Bandwidth / Model_Size。

## Corrected Claim

A100 80GB SXM4 的 HBM2e 显存带宽 2039 GB/s 是由 5120-bit 位宽和 1593 MHz 等效频率 (3186 MT/s) 计算得出 (5120/8 * 3186e6 / 1e9 ≈ 2039 GB/s)，该带宽是决定 LLM 解码阶段 (Decode) 吞吐量上限的核心参数，公式为 Throughput ≈ Bandwidth / Model_Size。

## Evidence

先验知识/题面给定，逻辑校验通过：5120-bit位宽与3186 MT/s频率计算得出的2039 GB/s带宽符合A100 80GB SXM4的官方规格，且解码阶段吞吐量受显存带宽限制的逻辑成立。

## Search Query

NVIDIA A100 HBM2e bandwidth calculation 2039 GB/s
