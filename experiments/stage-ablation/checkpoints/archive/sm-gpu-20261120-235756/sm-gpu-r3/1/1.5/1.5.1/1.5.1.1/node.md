# N163: INT8 权重的每通道 (Per-Channel) 量化存储开销：Scale 和 Zero-point 每通道存储 2 bytes (FP16)，Qwen3-2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

INT8 权重的每通道 (Per-Channel) 量化存储开销：Scale 和 Zero-point 每通道存储 2 bytes (FP16)，Qwen3-27B 有约 1000 个线性层，每层输出维度约 4096，总 Scale/Zero-point 开销约为 1000 * 4096 * 2 bytes * 2 (Scale+Zero) = 16.4 MB，相比 27.18GB 权重仅增加 0.06%，可忽略不计。

## Corrected Claim

INT8 权重的每通道 (Per-Channel) 量化存储开销：Scale 和 Zero-point 每通道存储 2 bytes (FP16)，Qwen3-27B 有约 1000 个线性层，每层输出维度约 4096，总 Scale/Zero-point 开销约为 1000 * 4096 * 2 bytes * 2 (Scale+Zero) = 16.4 MB，相比 27.18GB 权重仅增加 0.06%，可忽略不计。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构中线性层数量（约1000个）及输出维度（约4096）符合27B参数规模模型的典型配置；Per-Channel量化中Scale和Zero-point通常以FP16存储（各2字节），计算 1000 * 4096 * 2 * 2 = 16,384,000 bytes ≈ 16.4 MB，数值量级与算术逻辑均正确；16.4MB 相对于 27.18GB (约27,180,000 KB) 的占比约为 0.06%，结论合理。

## Search Query

INT8 per-channel quantization scale zero-point storage overhead calculation
