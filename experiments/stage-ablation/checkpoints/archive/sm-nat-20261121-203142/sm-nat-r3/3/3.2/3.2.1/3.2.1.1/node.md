# N117: 缓存覆盖率 C/M 的计算：C=128GB，M = N_obj × E[S] = 100,000 × (1.1/0.1) × x_min = 110,000 ×

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

缓存覆盖率 C/M 的计算：C=128GB，M = N_obj × E[S] = 100,000 × (1.1/0.1) × x_min = 110,000 × x_min；需设定 x_min（如 1KB）以计算 M ≈ 110GB，进而 C/M ≈ 1.16（注意若 M<C 则覆盖率为100%）

## Corrected Claim

缓存覆盖率 C/M 的计算：C=128GB，M = N_obj × E[S] = 100,000 × (1.1/0.1) × x_min = 110,000 × x_min；需设定 x_min（如 1KB）以计算 M ≈ 110GB，进而 C/M ≈ 1.16（注意若 M<C 则覆盖率为100%）

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 100,000 * 11 = 1,100,000 正确，1,100,000 KB = 110 GB 正确，128/110 ≈ 1.16 正确，且包含 M<C 时的边界条件说明，逻辑自洽。
