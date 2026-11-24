# N205: 混合策略长尾区域公有云部分带宽成本计算：Cost_Tail_Cloud = Tail_Region_Traffic_TB * Public_Cloud_Pric

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

混合策略长尾区域公有云部分带宽成本计算：Cost_Tail_Cloud = Tail_Region_Traffic_TB * Public_Cloud_Price_Per_TB，其中Tail_Region_Traffic_TB = 2TB * 0.2 = 0.4TB，Public_Cloud_Price_Per_TB取阿里云阶梯价¥0.24/GB（首档），则Cost_Tail_Cloud ≈ 0.4 * 1024 * 0.24 ≈ ¥98.3/天

## Corrected Claim

混合策略长尾区域公有云部分带宽成本计算：Cost_Tail_Cloud = Tail_Region_Traffic_TB * Public_Cloud_Price_Per_TB，其中Tail_Region_Traffic_TB = 2TB * 0.2 = 0.4TB，Public_Cloud_Price_Per_TB取阿里云阶梯价¥0.24/GB（首档），则Cost_Tail_Cloud ≈ 0.4 * 1024 * 0.24 ≈ ¥98.3/天

## Evidence

先验知识/题面给定，逻辑校验通过：0.4TB * 1024GB/TB * 0.24¥/GB = 98.304¥，计算无误且量级合理。
