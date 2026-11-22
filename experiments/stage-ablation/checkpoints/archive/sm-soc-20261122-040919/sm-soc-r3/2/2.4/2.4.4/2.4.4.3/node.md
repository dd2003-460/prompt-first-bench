# N237: 下游投影2：偏导数的统计显著性检验统计量 t_stat。t_stat = (∂E/∂ŵ_signal) / SE(∂E/∂ŵ_signal)，其中 SE(∂

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N64

## Claim

下游投影2：偏导数的统计显著性检验统计量 t_stat。t_stat = (∂E/∂ŵ_signal) / SE(∂E/∂ŵ_signal)，其中 SE(∂E/∂ŵ_signal) 由 N125 的 Var(ŵ_signal) 和模型参数的协方差矩阵计算得出。若 |t_stat| > 2.576 (对应 p<0.01 双尾)，则判定平台为关键驱动者。具体 SE 数值需代入 N125 的方差值及回归系数标准误计算。

## Corrected Claim

下游投影2：偏导数的统计显著性检验统计量 t_stat。t_stat = (∂E/∂ŵ_signal) / SE(∂E/∂ŵ_signal)，其中 SE(∂E/∂ŵ_signal) 由 N125 的 Var(ŵ_signal) 和模型参数的协方差矩阵计算得出。若 |t_stat| > 2.576 (对应 p<0.01 双尾)，则判定平台为关键驱动者。具体 SE 数值需代入 N125 的方差值及回归系数标准误计算。

## Evidence

先验知识/题面给定，逻辑校验通过：t统计量定义符合统计学标准，2.576对应双尾0.01显著性水平正确，SE计算逻辑自洽。
