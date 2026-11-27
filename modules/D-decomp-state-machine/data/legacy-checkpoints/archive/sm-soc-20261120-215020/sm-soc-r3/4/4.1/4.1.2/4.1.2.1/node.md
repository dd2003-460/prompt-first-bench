# N148: 滑动窗口机制下滞后时间 $T_{lag}$ 的解析解：$T_{lag} = \frac{W}{2}$，其中 $W$ 为窗口长度（天）。若 $W=30$ 天，则 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

滑动窗口机制下滞后时间 $T_{lag}$ 的解析解：$T_{lag} = \frac{W}{2}$，其中 $W$ 为窗口长度（天）。若 $W=30$ 天，则 $T_{lag}=15$ 天；若市场日均涨幅为 $g$，则滞后导致的相对误差为 $\epsilon_{lag} = g \times T_{lag}$。

## Corrected Claim

滑动窗口机制下滞后时间 $T_{lag}$ 的解析解：$T_{lag} = \frac{W}{2}$，其中 $W$ 为窗口长度（天）。若 $W=30$ 天，则 $T_{lag}=15$ 天；若市场日均涨幅为 $g$，则滞后导致的相对误差为 $\epsilon_{lag} = g \times T_{lag}$。

## Evidence

先验知识/题面给定，逻辑校验通过：滑动窗口平均滞后时间确为窗口长度的一半，线性近似误差公式符合基本数学推导。

## Search Query

sliding window average lag time formula market price
