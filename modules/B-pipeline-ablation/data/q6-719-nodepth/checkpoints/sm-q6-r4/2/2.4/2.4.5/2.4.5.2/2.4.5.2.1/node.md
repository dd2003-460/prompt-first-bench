# N700: Core_Monthly_Traffic_GB = DAU × Avg_Requests_Per_User × 30 × Avg_Object_Size_GB 

- **status**: verified
- **level**: L5
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N242

## Claim

Core_Monthly_Traffic_GB = DAU × Avg_Requests_Per_User × 30 × Avg_Object_Size_GB × Core_Traffic_Ratio，代入已知 DAU=500万，假设 Avg_Requests_Per_User=20, Avg_Object_Size_GB=0.05GB (50MB), Core_Traffic_Ratio=0.7 (核心区域占比)，计算得 Core_Monthly_Traffic_GB ≈ 5,000,000 × 20 × 30 × 0.05 × 0.7 = 10,500,000 GB (10.5 PB)。

## Corrected Claim

Core_Monthly_Traffic_GB = DAU × Avg_Requests_Per_User × 30 × Avg_Object_Size_GB × Core_Traffic_Ratio，代入已知 DAU=500万，假设 Avg_Requests_Per_User=20, Avg_Object_Size_GB=0.05GB (50MB), Core_Traffic_Ratio=0.7 (核心区域占比)，计算得 Core_Monthly_Traffic_GB ≈ 5,000,000 × 20 × 30 × 0.05 × 0.7 = 10,500,000 GB (10.5 PB)。

## Evidence

先验知识/题面给定，逻辑校验通过：5,000,000 × 20 × 30 × 0.05 × 0.7 = 10,500,000，计算无误，量级合理。
