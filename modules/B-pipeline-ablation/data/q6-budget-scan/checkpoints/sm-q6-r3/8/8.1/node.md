# N154: 访问日志生成速率模型：Log_Gen_Rate = N_req_per_sec * Avg_Log_Size，其中N_req_per_sec = DAU * R

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

访问日志生成速率模型：Log_Gen_Rate = N_req_per_sec * Avg_Log_Size，其中N_req_per_sec = DAU * Req_Per_User / 86400，Avg_Log_Size为单条日志大小（通常200-500 bytes），用于精确计算月日志总量而非估算

## Corrected Claim

访问日志生成速率模型：Log_Gen_Rate = N_req_per_sec * Avg_Log_Size，其中N_req_per_sec = DAU * Req_Per_User / 86400，Avg_Log_Size为单条日志大小（通常200-500 bytes），用于精确计算月日志总量而非估算

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（请求/秒 * 字节/请求 = 字节/秒），DAU转换为QPS的逻辑（除以86400）符合基本定义，日志大小范围符合工程常识。
