# N316: 协方差矩阵形式 Δf² 中交叉项 (∂f/∂Pi)(∂f/∂Cj)ρijσiσj 的数值贡献占比：在 TCO 公式中，价格项权重约 60-70%，功耗/通信项权

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N112

## Claim

协方差矩阵形式 Δf² 中交叉项 (∂f/∂Pi)(∂f/∂Cj)ρijσiσj 的数值贡献占比：在 TCO 公式中，价格项权重约 60-70%，功耗/通信项权重约 30-40%；当 ρ > 0.3 时，交叉项对总误差方差 Δf² 的贡献需超过 5% 才需启用完整协方差矩阵，否则简化公式误差 < 2%

## Corrected Claim

在TCO公式中，价格项通常占主导权重，功耗/通信项次之；当变量间相关性ρ较高时，交叉项对总误差方差Δf²的贡献不可忽略，需启用完整协方差矩阵以控制简化公式的误差。

## Evidence

[质询]该陈述包含具体的经验性阈值（如权重60-70%、ρ>0.3、贡献>5%、误差<2%），这些数值并非第一性原理可推导的数学常数，而是依赖于具体TCO模型参数、硬件成本结构及统计分布的经验拟合值。缺乏通用性，不同场景下阈值可能显著不同。 | 逻辑自洽（协方差展开式正确，量纲合理），但具体数值阈值属于经验事实，无来源支持且无法从第一性原理严格推出，故降级。

## Search Query

error propagation cross-term contribution threshold covariance matrix
