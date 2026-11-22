# N106: 代理指标‘点击率对价格偏离度的二阶导数’的操作性定义：$\frac{\partial^2 CTR}{\partial D^2} = \frac{CTR(D+\D

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

代理指标‘点击率对价格偏离度的二阶导数’的操作性定义：$\frac{\partial^2 CTR}{\partial D^2} = \frac{CTR(D+\Delta) - 2CTR(D) + CTR(D-\Delta)}{\Delta^2}$。若该二阶导数显著为负（p < 0.05），则证明流量对价格偏离度存在边际递减效应，支持 $k$ 随 $D$ 增大而减小的假设；若接近零，则假设 $k$ 为常数。

## Corrected Claim

代理指标‘点击率对价格偏离度的二阶导数’的操作性定义：$\frac{\partial^2 CTR}{\partial D^2} = \frac{CTR(D+\Delta) - 2CTR(D) + CTR(D-\Delta)}{\Delta^2}$。若该二阶导数显著为负（p < 0.05），则证明流量对价格偏离度存在边际递减效应，支持 $k$ 随 $D$ 增大而减小的假设；若接近零，则假设 $k$ 为常数。

## Evidence

先验知识/题面给定，逻辑校验通过：中心差分公式是二阶导数的标准数值近似，且二阶导数为负在数学上严格对应边际递减效应，逻辑自洽。
