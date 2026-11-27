# N53: INT8 权重大小计算：27e9 params * 1 byte / 1e9 = 27 GB。INT8 量化通常使用 Per-Channel 或 Per-Ten

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

INT8 权重大小计算：27e9 params * 1 byte / 1e9 = 27 GB。INT8 量化通常使用 Per-Channel 或 Per-Tensor 的 Scale 和 Zero-Point，额外内存开销极小 (每个通道 8-16 bytes)。

## Corrected Claim

INT8 权重大小计算：27e9 params * 1 byte / 1e9 = 27 GB。INT8 量化通常使用 Per-Channel 或 Per-Tensor 的 Scale 和 Zero-Point，额外内存开销极小 (每个通道 8-16 bytes)。

## Evidence

先验知识/题面给定，逻辑校验通过：27e9 * 1B = 27GB 计算正确；INT8 量化元数据（Scale/Zero-Point）开销极小符合工程常识。
