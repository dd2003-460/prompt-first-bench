# N278: 计算 MI300X (FP8) 的 Weight_Size：27.2B 参数 * 1 byte (FP8) = 27.2 GB。加上 Scale 因子 (5%)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N102

## Claim

计算 MI300X (FP8) 的 Weight_Size：27.2B 参数 * 1 byte (FP8) = 27.2 GB。加上 Scale 因子 (5%)，实际占用 ≈ 28.6 GB。

## Corrected Claim

计算 MI300X (FP8) 的 Weight_Size：27.2B 参数 * 1 byte (FP8) = 27.2 GB。加上 Scale 因子 (5%)，实际占用 ≈ 28.6 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27.2B参数在FP8下每参数1字节，基础大小为27.2GB；加上5%的Scale因子开销（27.2 * 0.05 = 1.36GB），总占用约为28.56GB，四舍五入为28.6GB，计算逻辑自洽且数值量级合理。
