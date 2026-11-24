# N272: API调用成本与日志成本的正交性：API_Cost_Monthly = Monthly_API_Calls × Unit_Price_API，其中 Monthl

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

API调用成本与日志成本的正交性：API_Cost_Monthly = Monthly_API_Calls × Unit_Price_API，其中 Monthly_API_Calls 由运维自动化脚本、健康检查及数据查询频率决定（通常远小于请求数，约为请求数的0.1%-1%），Unit_Price_API 为云厂商API单价（通常免费或极低，如¥0-0.01/千次），因此 API_Cost_Monthly 通常可忽略不计（<¥100/月），主要隐性成本集中在日志存储而非API调用。

## Corrected Claim

API调用成本与日志成本的正交性：API_Cost_Monthly = Monthly_API_Calls × Unit_Price_API，其中 Monthly_API_Calls 由运维自动化脚本、健康检查及数据查询频率决定（通常远小于请求数，约为请求数的0.1%-1%），Unit_Price_API 为云厂商API单价（通常免费或极低，如¥0-0.01/千次），因此 API_Cost_Monthly 通常可忽略不计（<¥100/月），主要隐性成本集中在日志存储而非API调用。

## Evidence

先验知识/题面给定，逻辑校验通过
