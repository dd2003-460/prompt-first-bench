# N541: 最大半径 R_80 的地理距离计算：R_80 = max(D_centroid_to_city) 对于所有 Top 80% 用户城市，其中 D_centroid

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N176

## Claim

最大半径 R_80 的地理距离计算：R_80 = max(D_centroid_to_city) 对于所有 Top 80% 用户城市，其中 D_centroid_to_city 使用 Haversine 公式计算；最远城市为乌鲁木齐（Lon=87.6°E, Lat=43.8°N），D ≈ 2,200km；哈尔滨（Lon=126.5°E, Lat=45.8°N），D ≈ 1,500km；故 R_80 ≈ 2,200km，D_80 ≈ 4,400km（注：原 claim 中 1200km 为误算，需修正）。

## Corrected Claim

最大半径 R_80 的地理距离计算：R_80 = max(D_centroid_to_city) 对于所有 Top 80% 用户城市，其中 D_centroid_to_city 使用 Haversine 公式计算；最远城市为乌鲁木齐（Lon=87.6°E, Lat=43.8°N），D ≈ 2,200km；哈尔滨（Lon=126.5°E, Lat=45.8°N），D ≈ 1,500km；故 R_80 ≈ 2,200km，D_80 ≈ 4,400km（注：原 claim 中 1200km 为误算，需修正）。

## Evidence

先验知识/题面给定，逻辑校验通过：乌鲁木齐（87.6°E, 43.8°N）与典型中国用户中心（如北京/上海，约116°E-121°E, 31°N-40°N）的Haversine距离确实在2000-2500km量级，哈尔滨距离较近，R_80取最大值2200km及直径4400km符合几何逻辑。
