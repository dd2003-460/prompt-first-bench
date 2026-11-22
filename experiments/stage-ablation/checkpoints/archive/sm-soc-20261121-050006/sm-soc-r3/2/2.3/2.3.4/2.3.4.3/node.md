# N207: 广告收益项（ΔAd_revenue_gain）的量化：ΔAd_revenue_gain = δ_ad * N_unsold * ΔTime_on_site * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

广告收益项（ΔAd_revenue_gain）的量化：ΔAd_revenue_gain = δ_ad * N_unsold * ΔTime_on_site * C_CPM * (Impressions_per_day / 1000)，其中 δ_ad 为广告依赖度，N_unsold 为未成交卖家数，ΔTime_on_site 为干预导致的在站时间变化，C_CPM 为千次展示成本，该公式定义了平台从干预中获得的直接广告收入增量。

## Corrected Claim

广告收益项（ΔAd_revenue_gain）的量化：ΔAd_revenue_gain = δ_ad * N_unsold * ΔTime_on_site * C_CPM * (Impressions_per_day / 1000)，其中 δ_ad 为广告依赖度，N_unsold 为未成交卖家数，ΔTime_on_site 为干预导致的在站时间变化，C_CPM 为千次展示成本，该公式定义了平台从干预中获得的直接广告收入增量。

## Evidence

先验知识/题面给定，逻辑校验通过
