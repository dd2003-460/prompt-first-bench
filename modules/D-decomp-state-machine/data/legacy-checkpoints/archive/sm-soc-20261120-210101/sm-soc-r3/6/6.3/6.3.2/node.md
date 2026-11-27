# N358: 曝光重置边界条件：当降价幅度 %ΔPrice_drop < 5% 时，用户感知不到价格变化，W_reset ≈ 1.0（无重置）；当 %ΔPrice_drop 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N105

## Claim

曝光重置边界条件：当降价幅度 %ΔPrice_drop < 5% 时，用户感知不到价格变化，W_reset ≈ 1.0（无重置）；当 %ΔPrice_drop > 20% 时，触发平台'大幅降价'标签，W_reset 可能 > 1.2（曝光加权）。需分区间计算 W_reset：W_reset(ΔP<5%) = 1.0 ± 0.05，W_reset(5%≤ΔP≤20%) = 0.8 + 0.02*(ΔP-5)，W_reset(ΔP>20%) = 1.2 + 0.01*(ΔP-20)。

## Corrected Claim

曝光重置边界条件：通常存在一个价格变化感知阈值，低于该阈值时用户感知弱，W_reset 接近 1.0；高于较高阈值时可能触发平台促销标签，W_reset 大于 1.0。具体阈值和加权系数需根据特定平台数据和品类特性进行实证拟合，而非固定公式。

## Evidence

[质询]该陈述包含具体的经验性阈值（5%、20%）和精确的线性回归系数（0.02, 0.01），这些属于特定平台或特定市场环境的经验参数，无法从第一性原理或通用逻辑中严格推导出来，且不同平台/品类的感知阈值差异巨大，缺乏普适性。 | 逻辑上分段函数连续且单调性符合直觉（降价越多曝光权重越高），但具体数值系数和阈值属于经验事实，无来源支持且非第一性原理可推导，故降级。

## Search Query

price drop threshold exposure boost e-commerce platform
