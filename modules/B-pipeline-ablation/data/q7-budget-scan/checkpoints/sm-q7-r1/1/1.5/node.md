# N11: NVMe SSD阵列方案中，500TB数据全部存储在SSD上，需根据有效容量系数反推所需裸容量：若系数为0.5，则需裸容量 = 500TB / 0.5 = 10

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

NVMe SSD阵列方案中，500TB数据全部存储在SSD上，需根据有效容量系数反推所需裸容量：若系数为0.5，则需裸容量 = 500TB / 0.5 = 1000TB。

## Corrected Claim

NVMe SSD阵列方案中，500TB数据全部存储在SSD上，需根据有效容量系数反推所需裸容量：若系数为0.5，则需裸容量 = 500TB / 0.5 = 1000TB。

## Evidence

先验知识/题面给定，逻辑校验通过：裸容量=有效容量/有效容量系数，500TB/0.5=1000TB，数学推导正确且量级合理。
