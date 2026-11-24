# N57: 生命周期策略对有效容量成本的影响：将 80% 冷数据转入 IA/Archive 后，虽然逻辑容量不变，但单位 GB 单价下降。例如标准存储 ¥0.12/GB/月

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

生命周期策略对有效容量成本的影响：将 80% 冷数据转入 IA/Archive 后，虽然逻辑容量不变，但单位 GB 单价下降。例如标准存储 ¥0.12/GB/月，归档存储 ¥0.03/GB/月，混合后的加权平均单价 = 0.2*0.12 + 0.8*0.03 = ¥0.048/GB/月，相当于有效容量成本降低了 60%

## Corrected Claim

生命周期策略对有效容量成本的影响：将 80% 冷数据转入 IA/Archive 后，虽然逻辑容量不变，但单位 GB 单价下降。例如标准存储 ¥0.12/GB/月，归档存储 ¥0.03/GB/月，混合后的加权平均单价 = 0.2*0.12 + 0.8*0.03 = ¥0.048/GB/月，相当于有效容量成本降低了 60%

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算正确（0.2*0.12+0.8*0.03=0.048），成本降低比例计算正确（(0.12-0.048)/0.12=60%），符合存储分层定价的基本经济逻辑。

## Search Query

aws s3 lifecycle policy ia archive pricing comparison
