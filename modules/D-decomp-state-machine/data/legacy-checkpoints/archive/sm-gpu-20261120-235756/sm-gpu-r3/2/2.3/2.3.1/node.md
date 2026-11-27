# N61: RTX 4090 (24GB) 显存带宽 1008 GB/s，A100 80GB SXM (2039 GB/s)，H100 80GB SXM (3350 GB/

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

RTX 4090 (24GB) 显存带宽 1008 GB/s，A100 80GB SXM (2039 GB/s)，H100 80GB SXM (3350 GB/s)，RTX 5090 (32GB) 显存带宽 1792 GB/s，这些数值直接决定单卡推理吞吐上限，需结合模型精度和上下文长度计算实际 Tokens/s。

## Corrected Claim

RTX 4090 (24GB) 显存带宽 1008 GB/s，A100 80GB SXM (2039 GB/s)，H100 80GB SXM (3350 GB/s)，RTX 5090 (32GB) 显存带宽 1792 GB/s，这些数值直接决定单卡推理吞吐上限，需结合模型精度和上下文长度计算实际 Tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 (1008 GB/s), A100 SXM (2039 GB/s), H100 SXM (3350 GB/s), RTX 5090 (1792 GB/s) 均为业界公认的标准硬件规格，数值量级与物理直觉一致，且显存带宽确实是单卡推理吞吐的关键瓶颈之一。
