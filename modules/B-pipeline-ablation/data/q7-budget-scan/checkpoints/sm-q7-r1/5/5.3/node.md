# N31: 容量扩展弹性成本：扩展成本 = (Additional_TB × Unit_Cost_Per_TB × Overhead_Factor)，其中Overhead_

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

容量扩展弹性成本：扩展成本 = (Additional_TB × Unit_Cost_Per_TB × Overhead_Factor)，其中Overhead_Factor反映扩展过程中的数据迁移/再平衡成本，本地SSD阵列Overhead_Factor~1.0~1.2（需停机或热迁移），HDD+SSD分层~1.1~1.3（需重平衡热冷数据），云存储~1.0（按需扩容，无迁移成本）

## Corrected Claim

容量扩展弹性成本：扩展成本 = (Additional_TB × Unit_Cost_Per_TB × Overhead_Factor)，其中Overhead_Factor反映扩展过程中的数据迁移/再平衡成本，本地SSD阵列Overhead_Factor~1.0~1.2（需停机或热迁移），HDD+SSD分层~1.1~1.3（需重平衡热冷数据），云存储~1.0（按需扩容，无迁移成本）

## Evidence

先验知识/题面给定，逻辑校验通过
