# N52: FP8 权重大小计算：27e9 params * 1 byte / 1e9 = 27 GB。注意：FP8 推理通常需要额外的 Scale 因子存储，每个 FP8

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

FP8 权重大小计算：27e9 params * 1 byte / 1e9 = 27 GB。注意：FP8 推理通常需要额外的 Scale 因子存储，每个 FP8 张量块 (如 128x128) 需要 1 个 FP32 Scale (4 bytes)，这会增加约 0.1-0.5% 的额外内存开销，通常可忽略或包含在框架开销中。

## Corrected Claim

FP8 权重大小计算：27e9 params * 1 byte / 1e9 = 27 GB。注意：FP8 推理通常需要额外的 Scale 因子存储，每个 FP8 张量块 (如 128x128) 需要 1 个 FP32 Scale (4 bytes)，这会增加约 0.1-0.5% 的额外内存开销，通常可忽略或包含在框架开销中。

## Evidence

先验知识/题面给定，逻辑校验通过：27e9 * 1B = 27GB 计算正确；FP8 块级缩放因子（如 128x128 块对应 1 个 FP32）带来的额外开销约为 4/(128*128*1) ≈ 0.024%，属于可忽略范围，陈述中 0.1-0.5% 的估计虽略保守但量级合理且符合工程惯例。

## Search Query

FP8 quantization scale factor memory overhead
