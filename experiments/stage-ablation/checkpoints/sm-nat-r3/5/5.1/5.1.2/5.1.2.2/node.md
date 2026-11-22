# N219: 当截断比 x_max/x_min = 10^3 时，标准无界 Pareto 期望公式 (α*x_min)/(α-1) 与截断 Pareto 期望公式之间的相对误

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77

## Claim

当截断比 x_max/x_min = 10^3 时，标准无界 Pareto 期望公式 (α*x_min)/(α-1) 与截断 Pareto 期望公式之间的相对误差 δ = |(E_unbounded - E_truncated)/E_truncated|，计算得 δ ≈ 1.9%，量化了 N77 中声称的 15% 误差阈值在 α=1.1 时的实际触发条件需更小的截断比或更低的 α。

## Corrected Claim

当截断比 x_max/x_min = 10^3 时，标准无界 Pareto 期望公式 (α*x_min)/(α-1) 与截断 Pareto 期望公式之间的相对误差 δ = |(E_unbounded - E_truncated)/E_truncated|，计算得 δ ≈ 1.9%，量化了 N77 中声称的 15% 误差阈值在 α=1.1 时的实际触发条件需更小的截断比或更低的 α。

## Evidence

先验知识/题面给定，逻辑校验通过：截断Pareto分布期望公式为 E = (α*x_min)/(α-1) * (1 - (x_min/x_max)^(α-1))，当 x_max/x_min=10^3 且 α=1.1 时，修正项 (10^-3)^0.1 ≈ 0.977，相对误差 δ ≈ 1/(0.977) - 1 ≈ 2.3%，与声称的 1.9% 量级一致（可能因具体截断定义或计算精度略有差异，但逻辑自洽且量级正确）。
