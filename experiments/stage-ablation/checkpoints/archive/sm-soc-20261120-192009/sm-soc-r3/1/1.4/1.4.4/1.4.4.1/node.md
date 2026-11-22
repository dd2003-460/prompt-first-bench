# N159: 买家基础支付意愿 θ_buy 的分布参数：θ_buy 服从对数正态分布 LogN(μ_log, σ_log²)，其中 μ_log 和 σ_log 需通过同类商品

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

买家基础支付意愿 θ_buy 的分布参数：θ_buy 服从对数正态分布 LogN(μ_log, σ_log²)，其中 μ_log 和 σ_log 需通过同类商品的历史成交价中位数及四分位距反推，以替代单一固定值。

## Corrected Claim

买家基础支付意愿 θ_buy 的分布参数：θ_buy 服从对数正态分布 LogN(μ_log, σ_log²)，其中 μ_log 和 σ_log 需通过同类商品的历史成交价中位数及四分位距反推，以替代单一固定值。

## Evidence

先验知识/题面给定，逻辑校验通过：对数正态分布常用于建模支付意愿等正偏态经济变量，且利用中位数和四分位距反推分布参数是标准的统计推断方法，逻辑自洽。
