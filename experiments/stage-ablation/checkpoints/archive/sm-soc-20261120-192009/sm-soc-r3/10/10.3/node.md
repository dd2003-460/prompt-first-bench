# N345: 随机偏好噪声 σ_noise^2 被修剪的速度：高偏离度策略被淘汰的速率 v_elim = λ_selection * (1 - σ_noise^2 / σ_i

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N117

## Claim

随机偏好噪声 σ_noise^2 被修剪的速度：高偏离度策略被淘汰的速率 v_elim = λ_selection * (1 - σ_noise^2 / σ_init^2)，若 v_elim > 0.1，则定向压力显著影响策略收敛。

## Corrected Claim

在特定选择压力模型中，随机偏好噪声 σ_noise^2 的修剪速度可表示为 v_elim = λ_selection * (1 - σ_noise^2 / σ_init^2)；当 v_elim > 0.1 时，定向压力对策略收敛有显著影响。

## Evidence

[质询]该公式 v_elim = λ_selection * (1 - σ_noise^2 / σ_init^2) 缺乏明确的理论推导或标准文献支持，属于特定模型假设下的经验性定义，且阈值 0.1 的选取缺乏普适性依据，可能混淆了特定实验设定与通用规律。 | 先验知识/题面给定，逻辑校验通过（量纲一致，逻辑自洽），但作为经验性参数设定，缺乏外部来源直接支持，且存在特定模型假设风险。
