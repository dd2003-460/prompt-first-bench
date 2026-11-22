# N137: INT4 (AWQ) 量化中 group_size=128 时的 Scale/Zero-point 参数总显存开销为 0.844 GB，计算式为 (27e9 /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

INT4 (AWQ) 量化中 group_size=128 时的 Scale/Zero-point 参数总显存开销为 0.844 GB，计算式为 (27e9 / 128) * 2 bytes * 2 (scale+zero) / 1e9。

## Corrected Claim

INT4 (AWQ) 量化中 group_size=128 时的 Scale/Zero-point 参数总显存开销为 0.844 GB，计算式为 (27e9 / 128) * 2 bytes * 2 (scale+zero) / 1e9。

## Evidence

先验知识/题面给定，逻辑校验通过：计算式 (27e9 / 128) * 2 * 2 / 1e9 = 0.84375 GB，四舍五入为 0.844 GB，数值与逻辑均正确。
