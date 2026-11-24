# N78: 3年TCO中硬件/云存储费用的折旧与递增模型：对于本地方案（NVMe/HDD），成本为一次性资本支出(CapEx)按3年直线折旧或按实际残值计算；对于云方案，成

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

3年TCO中硬件/云存储费用的折旧与递增模型：对于本地方案（NVMe/HDD），成本为一次性资本支出(CapEx)按3年直线折旧或按实际残值计算；对于云方案，成本为运营支出(OpEx)随数据量逐年递增，公式为 Cost_cloud_3y = Σ(t=1 to 3) [Data_Size(t) × Price_per_TB_per_year]，其中 Data_Size(t) = 500TB × (1+g)^(t-1)。

## Corrected Claim

3年TCO中硬件/云存储费用的折旧与递增模型：对于本地方案（NVMe/HDD），成本为一次性资本支出(CapEx)按3年直线折旧或按实际残值计算；对于云方案，成本为运营支出(OpEx)随数据量逐年递增，公式为 Cost_cloud_3y = Σ(t=1 to 3) [Data_Size(t) × Price_per_TB_per_year]，其中 Data_Size(t) = 500TB × (1+g)^(t-1)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cloud storage TCO calculation formula capex opex depreciation
