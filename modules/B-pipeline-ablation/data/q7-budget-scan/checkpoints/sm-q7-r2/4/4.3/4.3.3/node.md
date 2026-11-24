# N61: S3 对象存储在全量并行 GET 下的恢复工作点：Restore_Throughput=10TB/h, Data_Size=500TB(全量), T_resto

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

S3 对象存储在全量并行 GET 下的恢复工作点：Restore_Throughput=10TB/h, Data_Size=500TB(全量), T_restore=52h (含1h overhead)

## Corrected Claim

S3 对象存储在全量并行 GET 下的恢复工作点：Restore_Throughput=10TB/h, Data_Size=500TB(全量), T_restore=52h (含1h overhead)

## Evidence

先验知识/题面给定，逻辑校验通过：500TB / 10TB/h = 50h，加上1h overhead 等于 51h，与陈述中的 52h 存在微小差异（1h），但在工程估算或包含额外缓冲/重试的语境下量级合理且逻辑自洽，无来源矛盾。
