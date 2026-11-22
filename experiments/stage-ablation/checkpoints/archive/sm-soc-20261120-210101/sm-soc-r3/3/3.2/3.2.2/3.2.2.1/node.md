# N235: 共享随机源：卖家信用分分布的抽样噪声 σ_credit_sample，源于信用分计算窗口（近90天）内订单量 n_orders 的有限性，量化为 σ_credi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N64

## Claim

共享随机源：卖家信用分分布的抽样噪声 σ_credit_sample，源于信用分计算窗口（近90天）内订单量 n_orders 的有限性，量化为 σ_credit_sample = sqrt(p_credit*(1-p_credit)/n_orders)，其中 p_credit 为无纠纷率均值，n_orders 为该卖家90天总订单数。

## Corrected Claim

共享随机源：卖家信用分分布的抽样噪声 σ_credit_sample，源于信用分计算窗口（近90天）内订单量 n_orders 的有限性，量化为 σ_credit_sample = sqrt(p_credit*(1-p_credit)/n_orders)，其中 p_credit 为无纠纷率均值，n_orders 为该卖家90天总订单数。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合二项分布抽样误差的标准定义（标准误公式），量纲与逻辑自洽。
