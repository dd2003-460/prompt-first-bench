# N99: 平台算法权重 $W_{algo}$ 的构成需分解为曝光权重 $W_{exp}$ 和排序权重 $W_{rank}$。其中 $W_{rank} = f(\text{

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

平台算法权重 $W_{algo}$ 的构成需分解为曝光权重 $W_{exp}$ 和排序权重 $W_{rank}$。其中 $W_{rank} = f(\text{DwellTime}, \text{CTR}, \text{GMV})$。若 $\partial W_{rank}/\partial \text{DwellTime} > 0$，则平台有激励维持高溢价（因引发犹豫从而增加停留时间）；若 $\partial W_{rank}/\partial \text{GMV} > 0$，则平台有激励促进快速成交。需量化 $\text{DwellTime}$ 与 $\text{GMV}$ 在目标函数中的相对系数比 $\kappa = \frac{\partial U_p / \partial \text{DwellTime}}{\partial U_p / \partial \text{GMV}}$。[待核验] 若 $\kappa > 1$，则‘停留时长’主导，支持平台驱动假设；若 $\kappa < 0.5$，则‘GMV’主导，平台可能更偏好低价快销。

## Corrected Claim

平台算法权重通常由曝光和排序权重构成，排序权重受 DwellTime、CTR、GMV 等多因素影响。若模型假设 DwellTime 和 GMV 在目标函数中的相对系数比 κ 显著大于 1，则可能支持平台驱动停留时长的假设；若 κ 显著小于 0.5，则可能更偏好 GMV 主导的快速成交。具体阈值需根据平台实际算法参数确定。

## Evidence

[质询]该陈述将平台算法权重简化为单一目标函数 U_p 的偏导数之比，忽略了多目标优化中常见的非线性交互、动态权重调整及不同业务场景（如新品冷启动 vs 成熟品）下权重的异质性；此外，'高溢价引发犹豫从而增加停留时间'这一因果链条在行为经济学中并非普适真理，高溢价也可能导致直接跳出（Bounce），从而降低 DwellTime，因此 ∂W_rank/∂DwellTime > 0 并不必然意味着平台有激励维持高溢价。 | 逻辑自洽，但属于经验事实/理论模型假设，且无可用外部来源支持（检索失败），无法验证具体系数比 κ 的阈值（如 0.5）或因果机制的普适性，故降级。

## Search Query

second hand marketplace platform algorithm optimization objective dwell time vs GMV weight analysis
