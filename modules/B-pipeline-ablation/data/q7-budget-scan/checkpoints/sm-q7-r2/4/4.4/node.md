# N22: RTO 经济代价 = 业务中断损失率 * T_RTO + 加速恢复额外资源成本；业务中断损失率需基于温数据日均价值估算，公式：C_RTO = (L_hourly

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

RTO 经济代价 = 业务中断损失率 * T_RTO + 加速恢复额外资源成本；业务中断损失率需基于温数据日均价值估算，公式：C_RTO = (L_hourly * T_RTO_hours) + C_expedited，其中 L_hourly 为每小时业务损失（¥/h），C_expedited 为临时扩容/加班成本 [knowledge]

## Corrected Claim

RTO 经济代价 = 业务中断损失率 * T_RTO + 加速恢复额外资源成本；业务中断损失率需基于温数据日均价值估算，公式：C_RTO = (L_hourly * T_RTO_hours) + C_expedited，其中 L_hourly 为每小时业务损失（¥/h），C_expedited 为临时扩容/加班成本 [knowledge]

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点内容与父节点主题严重不符（父节点为RTO经济代价公式，子节点均为RAID重建技术细节），且子节点间存在逻辑包含关系（如带宽定义与时间计算重叠），未覆盖父节点中的'业务中断损失率'和'加速恢复成本'等核心要素。）
