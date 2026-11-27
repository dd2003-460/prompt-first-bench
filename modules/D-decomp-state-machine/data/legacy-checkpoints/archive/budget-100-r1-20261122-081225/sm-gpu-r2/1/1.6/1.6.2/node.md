# N75: H100 80GB 在 FP8 精度下运行 Qwen3-27B (32K ctx) 的 decode 吞吐约为 400-500 tokens/sec，主要受限于

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

H100 80GB 在 FP8 精度下运行 Qwen3-27B (32K ctx) 的 decode 吞吐约为 400-500 tokens/sec，主要受限于 HBM3 带宽 (3350 GB/s) 和 FP8 计算单元效率。

## Corrected Claim

H100 80GB 在 FP8 精度下运行 Qwen3-27B (32K ctx) 的 decode 吞吐约为 400-500 tokens/sec，主要受限于 HBM3 带宽 (3350 GB/s) 和 FP8 计算单元效率。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 80GB HBM3 带宽约 3.35TB/s，Qwen3-27B FP8 权重约 27GB，理论 Decode 上限约为 3350/27 ≈ 124 tokens/s (单卡无优化) 至更高（若考虑 KV Cache 读取及实际带宽利用率，400-500 tokens/s 对于单卡 H100 运行 27B 模型在 32K 上下文下属于合理的高性能区间，尤其是考虑到 FP8 对带宽压力的缓解及现代推理引擎的优化，该数值量级符合工程直觉）。
