# N57: W4 精度下的量化开销修正：W4 权重为 13.5GB，但量化过程需要存储 Scale 和 Zero-point 参数（通常 16-bit 或 32-bit 每

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10, N11, N12

## Claim

W4 精度下的量化开销修正：W4 权重为 13.5GB，但量化过程需要存储 Scale 和 Zero-point 参数（通常 16-bit 或 32-bit 每 128/256 个权重一组），额外开销约为权重大小的 0.5-1%，即 0.07-0.14GB，可忽略不计，但需确认框架是否强制使用 FP16 KV Cache（若是，则 W4 总需求仍为 28.2GB；若 KV 也量化，则显著降低）。

## Corrected Claim

W4 精度下的量化开销修正：W4 权重为 13.5GB，但量化过程需要存储 Scale 和 Zero-point 参数（通常 16-bit 或 32-bit 每 128/256 个权重一组），额外开销约为权重大小的 0.5-1%，即 0.07-0.14GB，可忽略不计，但需确认框架是否强制使用 FP16 KV Cache（若是，则 W4 总需求仍为 28.2GB；若 KV 也量化，则显著降低）。

## Evidence

先验知识/题面给定，逻辑校验通过：W4量化下Scale/Zero-point的额外开销比例（0.5-1%）及绝对值（0.07-0.14GB）计算正确，符合工程常识。
