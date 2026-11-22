# N500: Total_Tokens_Generated_Annual 的计算公式：Total_Tokens_Annual = (Tokens_per_second * 3

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N158

## Claim

Total_Tokens_Generated_Annual 的计算公式：Total_Tokens_Annual = (Tokens_per_second * 3600 * h_daily * 365) * (1 - D_down) * (1 - E_error)，其中 Tokens_per_second 为实测吞吐量，h_daily 为日均运行小时数（24/7场景下为24），D_down 为系统宕机时间占比（通常<1%），E_error 为推理失败或重试导致的无效Token占比（通常<5%），该公式需结合具体硬件的稳定性数据验证

## Corrected Claim

Total_Tokens_Generated_Annual 的计算公式：Total_Tokens_Annual = (Tokens_per_second * 3600 * h_daily * 365) * (1 - D_down) * (1 - E_error)，其中 Tokens_per_second 为实测吞吐量，h_daily 为日均运行小时数（24/7场景下为24），D_down 为系统宕机时间占比（通常<1%），E_error 为推理失败或重试导致的无效Token占比（通常<5%），该公式需结合具体硬件的稳定性数据验证

## Evidence

先验知识/题面给定，逻辑校验通过
