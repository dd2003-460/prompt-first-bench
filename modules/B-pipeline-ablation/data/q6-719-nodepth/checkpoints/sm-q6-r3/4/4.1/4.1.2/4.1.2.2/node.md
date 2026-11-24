# N271: 公有云日志存储与分析成本计算：Log_Cost_Monthly = Log_Volume_Monthly × Unit_Price_Log_GB，其中 Unit

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

公有云日志存储与分析成本计算：Log_Cost_Monthly = Log_Volume_Monthly × Unit_Price_Log_GB，其中 Unit_Price_Log_GB 为云厂商日志服务单价（阿里云SLS约为¥0.2-0.5/GB/月，含索引费用），若 Log_Volume_Monthly = 3000TB，则 Log_Cost_Monthly ≈ 3000×1024×0.35 ≈ ¥1,075,200/月，远高于N94声称的5k-15k元/月，表明N94的估算可能仅针对抽样日志或压缩后数据，需明确计费口径是原始日志还是采样日志。

## Corrected Claim

公有云日志存储与分析成本计算：Log_Cost_Monthly = Log_Volume_Monthly × Unit_Price_Log_GB，其中 Unit_Price_Log_GB 为云厂商日志服务单价（阿里云SLS约为¥0.2-0.5/GB/月，含索引费用），若 Log_Volume_Monthly = 3000TB，则 Log_Cost_Monthly ≈ 3000×1024×0.35 ≈ ¥1,075,200/月，远高于N94声称的5k-15k元/月，表明N94的估算可能仅针对抽样日志或压缩后数据，需明确计费口径是原始日志还是采样日志。

## Evidence

先验知识/题面给定，逻辑校验通过：3000TB转换为GB为3,072,000GB，乘以单价0.35元/GB/月，计算结果约为1,075,200元/月，量级与逻辑均正确，且远高于5k-15k元/月的对比结论成立。
