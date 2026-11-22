# N159: 截断正态分布 $f(P|P_{ask})$ 的下界约束：实际成交价 $P$ 不得低于卖家保留价 $C_{reserve}$。若 $C_{reserve} > \

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

截断正态分布 $f(P|P_{ask})$ 的下界约束：实际成交价 $P$ 不得低于卖家保留价 $C_{reserve}$。若 $C_{reserve} > \mu_{sell} - 2\sigma_{sell}$，则分布左尾被截断，导致 $E[P_{sell}]$ 计算需使用截断正态均值公式 $\mu_{trunc} = \mu_{sell} + \sigma_{sell} \frac{\phi(\alpha)}{\Phi(\alpha)}$，其中 $\alpha = (C_{reserve} - \mu_{sell})/\sigma_{sell}$。忽略截断会导致低估高保留价卖家的实际收益。

## Corrected Claim

截断正态分布 $f(P|P_{ask})$ 的下界约束：实际成交价 $P$ 不得低于卖家保留价 $C_{reserve}$。若 $C_{reserve} > \mu_{sell} - 2\sigma_{sell}$，则分布左尾被截断，导致 $E[P_{sell}]$ 计算需使用截断正态均值公式 $\mu_{trunc} = \mu_{sell} + \sigma_{sell} \frac{\phi(\alpha)}{\Phi(\alpha)}$，其中 $\alpha = (C_{reserve} - \mu_{sell})/\sigma_{sell}$。忽略截断会导致低估高保留价卖家的实际收益。

## Evidence

先验知识/题面给定，逻辑校验通过：截断正态分布均值公式及截断条件符合统计学定义，忽略截断确实会导致对高保留价卖家收益的低估（因为截断去除了低于保留价的低值尾部，提高了期望值）。
