# N64: 信用-价格相关性量化：计算高挂价组（P > P_ref * 1.15）与低挂价组的卖家平均信用分差值 ΔCredit = Mean(Credit_high) -

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N15

## Claim

信用-价格相关性量化：计算高挂价组（P > P_ref * 1.15）与低挂价组的卖家平均信用分差值 ΔCredit = Mean(Credit_high) - Mean(Credit_low)，并计算皮尔逊相关系数 r = Corr(P_deviation, Seller_Credit)。若 r > 0.3 且 ΔCredit > 0，支持卖家利用高信用背书支撑高价的假设。

## Corrected Claim

信用-价格相关性量化方法：通过计算高挂价组与低挂价组的卖家平均信用分差值 ΔCredit 及皮尔逊相关系数 r = Corr(P_deviation, Seller_Credit) 来检验卖家是否利用高信用背书支撑高价。若实证数据显示 r > 0.3 且 ΔCredit > 0，则支持该假设。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别处理了数据噪声（抽样误差）、数据清洗（新卖家剔除）和统计混杂（品类控制），三者关注点不同且互不重叠。虽然子节点2中提到的'假设高挂价组中新卖家占比为15%'是一个具体数值，但它作为数据清洗规则的背景条件，与子节点1的噪声量化公式和子节点3的相关性校正逻辑在功能上是正交的，不构成冗余。）

## Search Query

second hand marketplace seller credit score vs listing price correlation
