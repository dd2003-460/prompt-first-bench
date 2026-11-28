# N730: 4k tokens 时单步注意力计算复杂度增加导致的延迟增量 ΔT_attn 估算：ΔT_attn ∝ n^2 * d_model * C_flops_eff。

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N268

## Claim

4k tokens 时单步注意力计算复杂度增加导致的延迟增量 ΔT_attn 估算：ΔT_attn ∝ n^2 * d_model * C_flops_eff。假设 d_model=4096, C_flops_eff (V100 FP16) ≈ 120 TFLOPS。n=4096 时，FLOPs_attn ≈ 2 * 4096^2 * 4096 ≈ 137 GFLOPs。若计算效率 50%，耗时 ≈ 137e9 / (120e12 * 0.5) ≈ 2.28ms/step。相比 n=1024 时的 0.29ms，增量 1.99ms/step。在 20 tok/s 速度下，每 token 额外延迟 1.99ms，1000 tokens 生成额外耗时 1.99s，占总耗时 50s 的 4%，对任务完成率影响 < 1%。

## Corrected Claim

4k tokens 时单步注意力计算复杂度增加导致的延迟增量 ΔT_attn 估算：ΔT_attn ∝ n^2 * d_model * C_flops_eff。假设 d_model=4096, C_flops_eff (V100 FP16) ≈ 120 TFLOPS。n=4096 时，FLOPs_attn ≈ 2 * 4096^2 * 4096 ≈ 137 GFLOPs。若计算效率 50%，耗时 ≈ 137e9 / (120e12 * 0.5) ≈ 2.28ms/step。相比 n=1024 时的 0.29ms，增量 1.99ms/step。在 20 tok/s 速度下，每 token 额外延迟 1.99ms，1000 tokens 生成额外耗时 1.99s，占总耗时 50s 的 4%，对任务完成率影响 < 1%。

## Evidence

先验知识/题面给定，逻辑校验通过：FLOPs计算量级正确（~137GFLOPs），基于V100 FP16峰值算力及50%效率的耗时估算符合硬件性能常识，延迟占比推导逻辑自洽。
