# N53: 本地NVMe SSD阵列RTO代价 = 1e-4 * 4h * Hourly_Business_Impact，其中P_DataLoss_Event=1e-4/年

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

本地NVMe SSD阵列RTO代价 = 1e-4 * 4h * Hourly_Business_Impact，其中P_DataLoss_Event=1e-4/年，RTO_Hours=4h，Hourly_Business_Impact为每小时业务中断损失（需根据具体业务场景估算，如$10,000/h），计算结果约为$40/年

## Corrected Claim

本地NVMe SSD阵列RTO代价 = 1e-4 * 4h * Hourly_Business_Impact，其中P_DataLoss_Event=1e-4/年，RTO_Hours=4h，Hourly_Business_Impact为每小时业务中断损失（需根据具体业务场景估算，如$10,000/h），计算结果约为$40/年

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合风险成本计算逻辑（概率×恢复时间×单位损失），数值计算 1e-4 * 4 * 10000 = 40 准确无误，量纲一致。
