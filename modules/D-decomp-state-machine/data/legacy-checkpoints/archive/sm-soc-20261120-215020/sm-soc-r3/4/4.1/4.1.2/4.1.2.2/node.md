# N149: EWMA 机制下滞后时间 $T_{lag}$ 的解析解：$T_{lag} = \frac{1-\alpha}{\alpha}$，其中 $\alpha$ 为平滑因

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

EWMA 机制下滞后时间 $T_{lag}$ 的解析解：$T_{lag} = \frac{1-\alpha}{\alpha}$，其中 $\alpha$ 为平滑因子。若 $\alpha=0.1$，则 $T_{lag}=9$ 天；若 $\alpha=0.2$，则 $T_{lag}=4$ 天。相比滑动窗口，EWMA 对近期波动响应更快。

## Corrected Claim

EWMA 机制下滞后时间 $T_{lag}$ 的解析解：$T_{lag} = \frac{1-\alpha}{\alpha}$，其中 $\alpha$ 为平滑因子。若 $\alpha=0.1$，则 $T_{lag}=9$ 天；若 $\alpha=0.2$，则 $T_{lag}=4$ 天。相比滑动窗口，EWMA 对近期波动响应更快。

## Evidence

先验知识/题面给定，逻辑校验通过：EWMA 的滞后时间公式 T_lag = (1-α)/α 是时间序列分析中的标准定义，数值计算正确（0.9/0.1=9, 0.8/0.2=4），且 EWMA 相比固定窗口对近期变化响应更快的特性符合其指数衰减权重分布的逻辑。

## Search Query

exponentially weighted moving average lag time alpha formula
