# N55: 云对象存储RTO代价 = 1e-6 * 1h * Hourly_Business_Impact，其中P_DataLoss_Event=1e-6/年（多AZ冗余）

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

云对象存储RTO代价 = 1e-6 * 1h * Hourly_Business_Impact，其中P_DataLoss_Event=1e-6/年（多AZ冗余），RTO_Hours=1h（多AZ切换时间），计算结果约为$0.1/年

## Corrected Claim

云对象存储RTO代价 = 1e-6 * 1h * Hourly_Business_Impact，其中P_DataLoss_Event=1e-6/年（多AZ冗余），RTO_Hours=1h（多AZ切换时间），计算结果约为$0.1/年

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合风险成本计算逻辑（概率×恢复时间×业务影响），数值量级（1e-6 * 1 * 100000 = 0.1）计算正确，多AZ架构下RTO为1小时及极低数据丢失概率符合工程常识。
