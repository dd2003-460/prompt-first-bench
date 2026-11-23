# N155: 公有云日志存储单价细分：C_Log_Storage = C_Hot_Storage * V_Hot + C_Cold_Storage * V_Cold，其中V_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

公有云日志存储单价细分：C_Log_Storage = C_Hot_Storage * V_Hot + C_Cold_Storage * V_Cold，其中V_Hot为热存储数据量（通常保留7-30天，单价约¥0.1-0.3/GB/月），V_Cold为冷归档数据量（单价约¥0.01-0.05/GB/月），需根据合规保留期限（如GDPR/个保法要求6个月）计算加权成本

## Corrected Claim

公有云日志存储单价细分：C_Log_Storage = C_Hot_Storage * V_Hot + C_Cold_Storage * V_Cold，其中V_Hot为热存储数据量（通常保留7-30天，单价约¥0.1-0.3/GB/月），V_Cold为冷归档数据量（单价约¥0.01-0.05/GB/月），需根据合规保留期限（如GDPR/个保法要求6个月）计算加权成本

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合加权成本计算逻辑，热/冷存储单价量级（¥0.1-0.3 vs ¥0.01-0.05/GB/月）符合公有云市场普遍定价规律，合规保留期限描述合理。

## Search Query

cloud CDN log storage pricing hot cold tier GB month
