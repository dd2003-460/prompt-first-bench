# N69: A100 40GB 在 FP8 精度下运行 Qwen3-27B (8K ctx) 的 decode 吞吐约为 120-150 tokens/sec，主要受限于 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

A100 40GB 在 FP8 精度下运行 Qwen3-27B (8K ctx) 的 decode 吞吐约为 120-150 tokens/sec，主要受限于 HBM2e 带宽 (1555 GB/s) 和 FP8 计算单元效率。

## Corrected Claim

A100 40GB 在 FP8 精度下运行 Qwen3-27B (8K ctx) 的 decode 吞吐通常在 100-200 tokens/sec 范围内，具体数值取决于 KV Cache 大小和批处理策略，主要受限于 HBM2e 带宽 (1555 GB/s) 和 FP8 计算单元效率。

## Evidence

[质询]数值量级存疑：A100 40GB 的 HBM2e 带宽通常为 1555 GB/s，但 Qwen3-27B 在 FP8 下权重约 27GB，8K 上下文 KV Cache 占用较大，Decode 阶段主要受内存带宽限制。理论峰值吞吐约为 1555 GB/s / (27GB + KV Cache Size)。若 KV Cache 较小，理论上限可能高于 150 tokens/sec；若 KV Cache 较大或存在其他开销，120-150 是合理的经验估计，但缺乏具体 KV Cache 大小和批处理大小（batch size）的明确前提，导致该数值范围缺乏严谨推导基础，属于经验性估计而非严格推导。 | 先验知识/题面给定，逻辑校验通过。A100 40GB 带宽 1555 GB/s 符合规格，FP8 下 27B 模型权重约 27GB，Decode 吞吐受带宽限制，120-150 tokens/sec 在合理经验范围内，但缺乏具体 KV Cache 和 batch size 参数支持精确数值，故降级为定性表述。
