# N52: 最优挂价策略 $P_{ask}^*$ 的一阶条件：最大化 $E[U_s]$ 对 $P_{ask}$ 的导数为零。$\frac{\partial E[U_s]}{

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

最优挂价策略 $P_{ask}^*$ 的一阶条件：最大化 $E[U_s]$ 对 $P_{ask}$ 的导数为零。$\frac{\partial E[U_s]}{\partial P_{ask}} = (1-\epsilon_{neg}) - \lambda \frac{\partial E[T_{sale}]}{\partial P_{ask}} = 0$。若平台流量偏向高标价，$\frac{\partial E[T_{sale}]}{\partial P_{ask}} < 0$（高标价缩短周期），则 $P_{ask}^* > P_{market}$。具体地，若 $\lambda$ 较大（时间敏感型卖家），$P_{ask}^*$ 更接近 $P_{market}$；若 $\lambda$ 较小，$P_{ask}^*$ 显著高于 $P_{market}$。

## Corrected Claim

最优挂价策略 $P_{ask}^*$ 的一阶条件：最大化 $E[U_s]$ 对 $P_{ask}$ 的导数为零。$\frac{\partial E[U_s]}{\partial P_{ask}} = (1-\epsilon_{neg}) - \lambda \frac{\partial E[T_{sale}]}{\partial P_{ask}} = 0$。若平台流量偏向高标价，$\frac{\partial E[T_{sale}]}{\partial P_{ask}} < 0$（高标价缩短周期），则 $P_{ask}^* > P_{market}$。具体地，若 $\lambda$ 较大（时间敏感型卖家），$P_{ask}^*$ 更接近 $P_{market}$；若 $\lambda$ 较小，$P_{ask}^*$ 显著高于 $P_{market}$。

## Evidence

先验知识/题面给定，逻辑校验通过：一阶条件推导符合微积分基本定理，参数符号与经济学直觉（时间敏感度高则定价更接近市场）一致，无内部矛盾。
