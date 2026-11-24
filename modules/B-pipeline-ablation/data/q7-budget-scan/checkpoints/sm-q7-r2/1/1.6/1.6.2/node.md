# N54: HDD+SSD分层RTO代价 = 1e-4 * 4h * Hourly_Business_Impact，其中P_DataLoss_Event=1e-4/年（HD

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

HDD+SSD分层RTO代价 = 1e-4 * 4h * Hourly_Business_Impact，其中P_DataLoss_Event=1e-4/年（HDD机械故障率较高），RTO_Hours=4h（热数据SSD无重建延迟，冷数据HDD重建时间>6h但可异步），计算结果约为$40/年

## Corrected Claim

HDD+SSD分层RTO代价 = 1e-4 * 4h * Hourly_Business_Impact，其中P_DataLoss_Event=1e-4/年（HDD机械故障率较高），RTO_Hours=4h（热数据SSD无重建延迟，冷数据HDD重建时间>6h但可异步），计算结果约为$40/年

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合风险成本计算逻辑（概率×时间×单位损失），数值量级（1e-4/年故障率、4小时RTO）在工程常识范围内，且source为knowledge，无需外部来源支持。
