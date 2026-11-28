# N184: 学科覆盖的最小样本量 n_k ≥ 15 的统计功效验证：在 α=0.05, Power=0.8 条件下，检测中等效应量 (d=0.5) 的双样本 t-test 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

学科覆盖的最小样本量 n_k ≥ 15 的统计功效验证：在 α=0.05, Power=0.8 条件下，检测中等效应量 (d=0.5) 的双样本 t-test 所需最小样本量为 n=64/组，因此 n_k=15 仅能检测极大效应量 (d>1.2)，对于细微的质量差异检验力不足，建议提升至 n_k ≥ 30 或使用非参数检验。

## Corrected Claim

学科覆盖的最小样本量 n_k ≥ 15 的统计功效验证：在 α=0.05, Power=0.8 条件下，检测中等效应量 (d=0.5) 的双样本 t-test 所需最小样本量为 n=64/组，因此 n_k=15 仅能检测极大效应量 (d>1.2)，对于细微的质量差异检验力不足，建议提升至 n_k ≥ 30 或使用非参数检验。

## Evidence

先验知识/题面给定，逻辑校验通过：根据双样本t检验功效分析标准公式，α=0.05, Power=0.8, d=0.5时每组需约64人；n=15时仅能检测d≈1.2以上的极大效应量，结论符合统计学原理。

## Search Query

power analysis t-test minimum sample size medium effect size 0.8 power
