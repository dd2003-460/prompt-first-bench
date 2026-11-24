# N105: 云冷存储有效容量修正：标称400TB，云存储无本地RAID冗余，用户视角可用率系数0.95 (N20)，有效容量 = 400TB * 0.95 = 380TB，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

云冷存储有效容量修正：标称400TB，云存储无本地RAID冗余，用户视角可用率系数0.95 (N20)，有效容量 = 400TB * 0.95 = 380TB，因此每TB有效容量的年成本 = (N54+N56) / 380TB

## Corrected Claim

云冷存储有效容量修正：标称400TB，云存储无本地RAID冗余，用户视角可用率系数0.95 (N20)，有效容量 = 400TB * 0.95 = 380TB，因此每TB有效容量的年成本 = (N54+N56) / 380TB

## Evidence

先验知识/题面给定，逻辑校验通过：云存储通常无本地RAID，0.95的可用率系数符合行业经验，数学计算400*0.95=380正确。
