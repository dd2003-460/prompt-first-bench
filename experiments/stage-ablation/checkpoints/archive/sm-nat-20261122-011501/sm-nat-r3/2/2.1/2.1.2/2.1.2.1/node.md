# N99: Miss_Bytes_Rate 的解析表达式：Miss_Bytes_Rate = R_total * (1 - H_lru) * E[S|Miss]，其中 R_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

Miss_Bytes_Rate 的解析表达式：Miss_Bytes_Rate = R_total * (1 - H_lru) * E[S|Miss]，其中 R_total=5.79e7 req/s，E[S|Miss] 为未命中对象的大小期望，需解方程 T_res = 128GB / Miss_Bytes_Rate 与 T_res 定义闭环。

## Corrected Claim

Miss_Bytes_Rate 的解析表达式：Miss_Bytes_Rate = R_total * (1 - H_lru) * E[S|Miss]，其中 R_total=5.79e7 req/s，E[S|Miss] 为未命中对象的大小期望，需解方程 T_res = 128GB / Miss_Bytes_Rate 与 T_res 定义闭环。

## Evidence

先验知识/题面给定，逻辑校验通过
