# N321: 流量计费模式下的月度总成本 Cost_traffic_month = D_download_monthly * P_traffic_tier，其中 D_down

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

流量计费模式下的月度总成本 Cost_traffic_month = D_download_monthly * P_traffic_tier，其中 D_download_monthly = 2TB * 30 = 60TB = 61,440GB，P_traffic_tier 为对应流量阶梯的单价（如 ¥0.2/GB），计算得 Cost_traffic_month ≈ ¥12,288。

## Corrected Claim

流量计费模式下的月度总成本 Cost_traffic_month = D_download_monthly * P_traffic_tier，其中 D_download_monthly = 2TB * 30 = 60TB = 61,440GB，P_traffic_tier 为对应流量阶梯的单价（如 ¥0.2/GB），计算得 Cost_traffic_month ≈ ¥12,288。

## Evidence

先验知识/题面给定，逻辑校验通过：2TB*30=60TB，60*1024=61440GB，61440*0.2=12288，计算无误。
