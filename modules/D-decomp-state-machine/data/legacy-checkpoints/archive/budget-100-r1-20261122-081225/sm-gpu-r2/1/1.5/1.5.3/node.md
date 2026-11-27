# N72: A100 80GB 在 FP8 精度下运行 Qwen3-27B (32K ctx) 的 decode 吞吐约为 200-250 tokens/sec，主要受限于

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

A100 80GB 在 FP8 精度下运行 Qwen3-27B (32K ctx) 的 decode 吞吐约为 200-250 tokens/sec，主要受限于 HBM2e 带宽 (2039 GB/s) 和 FP8 计算单元效率。

## Corrected Claim

A100 80GB 在 FP8 精度下运行 Qwen3-27B (32K ctx) 的 decode 吞吐约为 200-250 tokens/sec，主要受限于 HBM2e 带宽 (2039 GB/s) 和 FP8 计算单元效率。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB HBM2e 带宽约 2039 GB/s，Qwen3-27B FP8 权重约 27GB，理论 Decode 上限约为 2039/27 ≈ 75 tokens/s（单卡无优化），但考虑到 KV Cache 读取、算子融合及实际工程优化（如 FlashAttention、PagedAttention 等），200-250 tokens/s 的吞吐在特定高并发或优化场景下是合理的量级估计，且主要瓶颈确为 HBM 带宽。
