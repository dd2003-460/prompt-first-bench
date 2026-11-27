# N180: 竞品逆向工程的代理指标：若无法获取一手数据，使用公开爬虫数据计算竞品平台（如闲鱼、转转）上高溢价商品（P_ask > 1.2*P_market）的平均曝光时长 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

竞品逆向工程的代理指标：若无法获取一手数据，使用公开爬虫数据计算竞品平台（如闲鱼、转转）上高溢价商品（P_ask > 1.2*P_market）的平均曝光时长 T_exposure_high 与基准商品 T_exposure_base 的比值 R = T_exposure_high / T_exposure_base，假设 β_platform ≈ ln(R) / ln(1.2) - 1，需验证该比值是否在 0.25-0.35 区间。

## Corrected Claim

竞品逆向工程的代理指标：若无法获取一手数据，使用公开爬虫数据计算竞品平台（如闲鱼、转转）上高溢价商品（P_ask > 1.2*P_market）的平均曝光时长 T_exposure_high 与基准商品 T_exposure_base 的比值 R = T_exposure_high / T_exposure_base，假设 β_platform ≈ ln(R) / ln(1.2) - 1，需验证该比值是否在 0.25-0.35 区间。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

competitive platform exposure time high premium items benchmark ratio reverse engineering
