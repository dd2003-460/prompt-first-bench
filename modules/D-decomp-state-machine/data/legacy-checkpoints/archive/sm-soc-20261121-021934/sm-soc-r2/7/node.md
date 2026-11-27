# N56: ‘成交周期变短’的统计定义需区分‘中位数成交周期 T_median’与‘平均成交周期 T_mean’；在高挂价策略下，由于长尾未成交商品被剔除出‘成交’样本，T

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

‘成交周期变短’的统计定义需区分‘中位数成交周期 T_median’与‘平均成交周期 T_mean’；在高挂价策略下，由于长尾未成交商品被剔除出‘成交’样本，T_median 可能显著低于 T_mean，需验证数据中是否仅统计了已成交子集导致的幸存者偏差（Survivorship Bias），其偏差幅度 ΔBias ≈ (N_total - N_dealt)/N_dealt * T_untreated。

## Corrected Claim

‘成交周期变短’的统计定义需区分‘中位数成交周期 T_median’与‘平均成交周期 T_mean’；在高挂价策略下，由于长尾未成交商品被剔除出‘成交’样本，T_median 可能显著低于 T_mean，需验证数据中是否仅统计了已成交子集导致的幸存者偏差（Survivorship Bias）。

## Evidence

[质询]公式 ΔBias ≈ (N_total - N_dealt)/N_dealt * T_untreated 缺乏统计学依据，量纲和逻辑均不成立。幸存者偏差导致 T_mean 被低估（或高估，取决于分布），但偏差幅度并非由未成交数量与成交数量的比值乘以未成交时间简单得出，该公式属于臆造的伪定量关系。 | 来源[1]仅定义中位数，未涉及幸存者偏差或成交周期统计；公式推导存在硬逻辑错误（量纲/因果混淆），无法从第一性原理推出。

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Median&rut=f87d35ace58e0fd558b6b20c67908aa639709410f0c71260ae7dbbf6ea07630e', 'type': 'ddg', 'title': 'Median - Wikipedia'}
