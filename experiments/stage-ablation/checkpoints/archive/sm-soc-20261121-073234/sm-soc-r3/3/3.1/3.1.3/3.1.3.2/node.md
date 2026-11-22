# N203: w_3 (Freshness权重) 的衰减函数形式：通常为指数衰减 Freshness_i = exp(-λ * age_days)，其中 λ 为衰减系数。需量

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

w_3 (Freshness权重) 的衰减函数形式：通常为指数衰减 Freshness_i = exp(-λ * age_days)，其中 λ 为衰减系数。需量化 λ 的取值：若 λ 过小，旧商品持续占据高曝光；若 λ 过大，新商品未获足够曝光即被挤出。需通过用户停留时长数据校准 λ。

## Corrected Claim

w_3 (Freshness权重) 的衰减函数形式：通常为指数衰减 Freshness_i = exp(-λ * age_days)，其中 λ 为衰减系数。需量化 λ 的取值：若 λ 过小，旧商品持续占据高曝光；若 λ 过大，新商品未获足够曝光即被挤出。需通过用户停留时长数据校准 λ。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

freshness decay function ranking algorithm e-commerce lambda coefficient
