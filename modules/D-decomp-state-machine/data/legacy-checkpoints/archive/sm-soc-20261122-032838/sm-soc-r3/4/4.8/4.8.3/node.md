# N89: 构建'净效应取决于替代平台竞争强度'的博弈模型。设本平台 GMV 变化为 $\Delta GMV_1$，替代平台 GMV 变化为 $\Delta GMV_2$。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

构建'净效应取决于替代平台竞争强度'的博弈模型。设本平台 GMV 变化为 $\Delta GMV_1$，替代平台 GMV 变化为 $\Delta GMV_2$。若竞争强度 $C_{comp}$ 高（替代品多），用户流失率 $\lambda_{churn}$ 对价格透明化的敏感度更高，$\Delta GMV_1$ 为负值幅度扩大；若 $C_{comp}$ 低（垄断），用户无替代选择，$\lambda_{churn} \approx 0$，GMV 下降主要源于单价降低，幅度较小。需定义 $C_{comp}$ 的量化指标（如 HHI 指数）以确定阈值。

## Corrected Claim

构建'净效应取决于替代平台竞争强度'的博弈模型。设本平台 GMV 变化为 $\Delta GMV_1$，替代平台 GMV 变化为 $\Delta GMV_2$。若竞争强度 $C_{comp}$ 高（替代品多），用户流失率 $\lambda_{churn}$ 对价格透明化的敏感度更高，$\Delta GMV_1$ 为负值幅度扩大；若 $C_{comp}$ 低（垄断），用户无替代选择，$\lambda_{churn} \approx 0$，GMV 下降主要源于单价降低，幅度较小。需定义 $C_{comp}$ 的量化指标（如 HHI 指数）以确定阈值。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点中的三个核心逻辑环节：竞争强度量化（HHI定义）、中间机制函数（流失率敏感度）、最终结果计算（GMV净效应及临界点）。三者逻辑链条清晰，无重复或矛盾，且完整覆盖了父节点提出的建模需求。）

## Search Query

market competition intensity impact on platform GMV price transparency
