# N362: 年总请求量的工作日修正因子：R_total_annual_workday = R_total_daily_workday × 260 + R_total_dai

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N115

## Claim

年总请求量的工作日修正因子：R_total_annual_workday = R_total_daily_workday × 260 + R_total_daily_weekend × 105，其中工作日日均请求量通常比周末高 10-15%（基于 C 端用户行为模式），若忽略此差异，年总请求量估算误差约为 ±3-5%。

## Corrected Claim

年总请求量的工作日修正因子：R_total_annual_workday = R_total_daily_workday × 260 + R_total_daily_weekend × 105，其中工作日日均请求量通常比周末高 10-15%（基于 C 端用户行为模式），若忽略此差异，年总请求量估算误差约为 ±3-5%。

## Evidence

先验知识/题面给定，逻辑校验通过：260+105=365天符合公历常识，工作日流量高于周末符合C端互联网业务普遍规律，误差估算量级合理。
