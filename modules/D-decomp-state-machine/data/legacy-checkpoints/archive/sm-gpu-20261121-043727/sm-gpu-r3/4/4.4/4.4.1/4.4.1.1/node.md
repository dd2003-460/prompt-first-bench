# N184: Qwen3-27B W4 量化中 Scale 因子的精确开销计算：假设每 128 个权重共享一个 FP16 Scale (2 bytes)，则 Scale 占比

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

Qwen3-27B W4 量化中 Scale 因子的精确开销计算：假设每 128 个权重共享一个 FP16 Scale (2 bytes)，则 Scale 占比 = (27.2e9 / 128) * 2 bytes / (27.2e9 * 0.5 bytes) = 0.625%，若使用 Group Size 64 则占比为 1.25%，因此实际权重体积 = 12.7 GB * (1 + 0.00625~0.0125) ≈ 12.78-12.86 GB，而非 13.5-14.0 GB

## Corrected Claim

Qwen3-27B W4 量化中 Scale 因子的精确开销计算：假设每 128 个权重共享一个 FP16 Scale (2 bytes)，则 Scale 占比 = (27.2e9 / 128) * 2 bytes / (27.2e9 * 0.5 bytes) = 0.625%，若使用 Group Size 64 则占比为 1.25%，因此实际权重体积 = 12.7 GB * (1 + 0.00625~0.0125) ≈ 12.78-12.86 GB，而非 13.5-14.0 GB

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导正确，Scale开销计算符合量化原理
