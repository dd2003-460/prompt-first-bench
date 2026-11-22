# N85: 工作点2（中位数修正）：使用 Pareto(α=1.1) 的中位数 S_median = x_min * 2^{1/(α-1)} ≈ 20.5KB 替代均值计算

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

工作点2（中位数修正）：使用 Pareto(α=1.1) 的中位数 S_median = x_min * 2^{1/(α-1)} ≈ 20.5KB 替代均值计算 M_total_med=2.05TB，C/M_med=0.062，该工作点反映了缓存实际驻留对象的大小分布更偏向中位数而非均值，修正后的 C/M 更低，命中率下界进一步降低至 ~0.55，揭示了均值高估了缓存效率。

## Corrected Claim

工作点2（中位数修正）：使用 Pareto(α=1.1) 的中位数 S_median = x_min * 2^{1/(α-1)} ≈ 20.5KB 替代均值计算 M_total_med=2.05TB，C/M_med=0.062，该工作点反映了缓存实际驻留对象的大小分布更偏向中位数而非均值，修正后的 C/M 更低，命中率下界进一步降低至 ~0.55，揭示了均值高估了缓存效率。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布中位数公式正确，数值量级合理，逻辑自洽
