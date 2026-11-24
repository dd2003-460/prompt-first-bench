# N647: S3 Versioning 的存储成本：开启版本控制后，每个对象的每个版本都单独计费；若保留过去 24 小时的所有中间版本，且写入频率高，实际存储开销可能远超数

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N224

## Claim

S3 Versioning 的存储成本：开启版本控制后，每个对象的每个版本都单独计费；若保留过去 24 小时的所有中间版本，且写入频率高，实际存储开销可能远超数据量的 10%；需计算日均写入对象数 N_obj_write 与平均对象大小 S_avg，额外存储量 V_extra = Σ (N_obj_write_i * S_avg_i * Retention_Version_Count)。

## Corrected Claim

S3 Versioning 的存储成本：开启版本控制后，每个对象的每个版本都单独计费；若保留过去 24 小时的所有中间版本，且写入频率高，实际存储开销可能远超数据量的 10%；需计算日均写入对象数 N_obj_write 与平均对象大小 S_avg，额外存储量 V_extra = Σ (N_obj_write_i * S_avg_i * Retention_Version_Count)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

S3 versioning storage cost calculation multiple versions
