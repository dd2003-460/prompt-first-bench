# N22: RTO 经济代价 = 业务中断损失率 * T_RTO + 加速恢复额外资源成本；业务中断损失率需基于温数据日均价值估算，公式：C_RTO = (L_hourly

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

RTO 经济代价 = 业务中断损失率 * T_RTO + 加速恢复额外资源成本；业务中断损失率需基于温数据日均价值估算，公式：C_RTO = (L_hourly * T_RTO_hours) + C_expedited，其中 L_hourly 为每小时业务损失（¥/h），C_expedited 为临时扩容/加班成本 [knowledge]

## Corrected Claim

RTO 经济代价 = 业务中断损失率 * T_RTO + 加速恢复额外资源成本；业务中断损失率需基于温数据日均价值估算，公式：C_RTO = (L_hourly * T_RTO_hours) + C_expedited，其中 L_hourly 为每小时业务损失（¥/h），C_expedited 为临时扩容/加班成本 [knowledge]

## Evidence

先验知识/题面给定，逻辑校验通过：RTO经济代价由中断期间的业务损失（损失率×时间）和为缩短RTO产生的额外资源成本构成，符合经济学基本原理及灾备成本模型定义。
