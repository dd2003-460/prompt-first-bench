# N250: 利润率 Margin 下降对 GMV 的边际贡献系数：ΔGMV/ΔMargin = -Q * P * (1 - Margin)，其中 Q 为成交量，P 为平均售

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N80

## Claim

利润率 Margin 下降对 GMV 的边际贡献系数：ΔGMV/ΔMargin = -Q * P * (1 - Margin)，其中 Q 为成交量，P 为平均售价，Margin 为利润率；假设 Q 和 P 不变，Margin 下降 5% 导致 GMV 下降约 5% * Q * P * (1 - Margin)。

## Corrected Claim

利润率 Margin 下降对净利润（Net Profit）的边际贡献系数：ΔProfit/ΔMargin = Q * P，其中 Profit = GMV * Margin = Q * P * Margin。假设 Q 和 P 不变，Margin 下降 5% 导致净利润下降约 5% * Q * P。

## Evidence

[质询]概念混淆与量纲错误：GMV（Gross Merchandise Value，商品交易总额）通常定义为 成交量(Q) × 平均售价(P)，即 GMV = Q * P。利润率(Margin)的变化并不直接改变 GMV 的数值，而是改变净利润或毛利额。陈述中声称 'Margin 下降导致 GMV 下降' 在标准商业定义下是逻辑错误的，因为 Margin 是派生指标（(P-C)/P），其变化源于成本 C 或价格 P 的变化，而非独立变量。若 P 不变，Margin 下降意味着成本上升，GMV 保持不变；若 P 下降导致 Margin 下降，则 GMV 下降的原因是 P 的变化，而非 Margin 本身。公式 ΔGMV/ΔMargin = -Q * P * (1 - Margin) 在量纲和因果逻辑上均不成立，因为 GMV 对 Margin 的导数在 Q, P 固定时为 0。 | 逻辑校验失败：GMV 定义为 Q*P，与 Margin 无直接函数依赖关系（在 Q, P 不变假设下），陈述存在根本性的概念混淆和逻辑矛盾。
