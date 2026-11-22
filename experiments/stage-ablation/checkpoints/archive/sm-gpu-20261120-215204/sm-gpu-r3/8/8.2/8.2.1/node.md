# N381: 工作点A (高性低成/理论峰值型)：A100 80GB FP8 精度下，理论峰值 Tokens/s = 2039 GB/s / 27 GB ≈ 75.5 Tok

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N144

## Claim

工作点A (高性低成/理论峰值型)：A100 80GB FP8 精度下，理论峰值 Tokens/s = 2039 GB/s / 27 GB ≈ 75.5 Tokens/s，这是 HBM2e 带宽限制下的上限，实际性能受限于此值。

## Corrected Claim

A100 80GB 的 HBM2e 带宽约为 2039 GB/s。若模型权重或激活数据占用 27 GB，则理论上的数据读取频率上限约为 75.5 次/秒。实际 Tokens/s 吞吐量需结合模型参数量、Batch Size 及计算密度综合计算，不能简单由带宽除以数据量得出。

## Evidence

[质询]数值量级与物理直觉严重不符：2039 GB/s 除以 27 GB 得到的结果单位是 s^-1 (即每秒可读取的完整数据集次数)，而非 Tokens/s。若按此计算，75.5 代表每秒能完整读取 75.5 次 27GB 的数据，这远超任何单卡或集群的合理吞吐量（通常 LLM 推理吞吐量在数千至数万 Tokens/s 量级，取决于模型大小和 Batch Size）。此外，A100 80GB 的 HBM2e 带宽约为 2039 GB/s 是正确的，但 27GB 并非 A100 的标准显存占用或模型大小标准值，且将带宽直接除以某个固定 GB 数来推导 'Tokens/s' 缺乏明确的模型参数量或 Batch Size 上下文，属于口径混淆或单位错误。 | 逻辑校验失败：单位量纲错误（GB/s / GB = 1/s，非 Tokens/s），且数值 75.5 Tokens/s 对于 A100 80GB 的推理性能而言过低，不符合基本硬件性能直觉。
