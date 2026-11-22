# N184: 买家随机偏好噪声标准差 $\sigma_{noise}$ 的估计方法：通过同一商品在不同时间点的咨询率方差 $Var(R_{inquiry})$ 减去价格变动解

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N73

## Claim

买家随机偏好噪声标准差 $\sigma_{noise}$ 的估计方法：通过同一商品在不同时间点的咨询率方差 $Var(R_{inquiry})$ 减去价格变动解释的方差 $Var(R_{inquiry}|P)$ 得到，即 $\sigma_{noise} = \sqrt{Var(R_{inquiry}) - Var(R_{inquiry}|P)}$；若 $\sigma_{noise} > 5\%$，则启发式偏差显著。

## Corrected Claim

买家随机偏好噪声标准差 $\sigma_{noise}$ 的估计方法：通常通过回归分析残差的标准差来估计，即 $\sigma_{noise} = \sqrt{Var(R_{inquiry} - E[R_{inquiry}|P])}$；若 $\sigma_{noise}$ 相对于平均咨询率的比例超过特定阈值（如 5%），则启发式偏差显著。

## Evidence

[质询]公式存在严重的量纲和逻辑错误：方差（Variance）是标准差（Standard Deviation）的平方，不能直接相减得到标准差；且 $Var(R_{inquiry}|P)$ 是条件方差，通常 $Var(R) = E[Var(R|P)] + Var(E[R|P])$，直接相减在统计上无意义，除非特定假设下 $Var(R|P)$ 代表噪声方差，但即便如此，量纲也不匹配（左边是标准差，右边是方差的平方根，但减数若是方差则量纲错误，若减数是噪声方差则表述混淆）。此外，5% 的阈值缺乏理论依据，属于任意设定的经验值。 | 先验知识/题面给定，逻辑校验失败：方差与标准差量纲不一致，且条件方差与总方差的分解关系表述错误，导致公式在数学上不成立。
