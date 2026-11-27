# N51: 卖家期望收益函数展开：$E[U_s] = E[P_{sell}] - C_{hold} - \lambda E[T_{sale}]$。其中 $E[P_{sell

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

卖家期望收益函数展开：$E[U_s] = E[P_{sell}] - C_{hold} - \lambda E[T_{sale}]$。其中 $E[P_{sell}] = \int P \cdot f(P|P_{ask}) dP$，$E[T_{sale}] = \int T \cdot g(T|P_{ask}) dT$。在信息不对称下，$f(P|P_{ask})$ 为截断正态分布，均值 $\mu_{sell} \approx P_{ask} \cdot (1 - \epsilon_{neg})$，其中 $\epsilon_{neg}$ 为议价折损率（约 5-10%）。

## Corrected Claim

卖家期望收益函数展开：$E[U_s] = E[P_{sell}] - C_{hold} - \lambda E[T_{sale}]$。其中 $E[P_{sell}] = \int P \cdot f(P|P_{ask}) dP$，$E[T_{sale}] = \int T \cdot g(T|P_{ask}) dT$。在信息不对称下，$f(P|P_{ask})$ 为截断正态分布，均值 $\mu_{sell} \approx P_{ask} \cdot (1 - \epsilon_{neg})$，其中 $\epsilon_{neg}$ 为议价折损率（约 5-10%）。

## Evidence

先验知识/题面给定，逻辑校验通过
