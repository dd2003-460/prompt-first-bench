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

父节点级核验未通过：非正交, 不完备（子节点与父节点主题严重错位。父节点讨论的是'RTO经济代价'（涉及业务损失率、加速恢复成本等财务指标），而所有4个子节点均详细描述了'HDD/SSD RAID重建的技术细节'（带宽、盘数、物理结构、技术耗时）。子节点完全未覆盖父节点中关于'业务中断损失率估算'或'加速恢复额外资源成本'的内容，属于答非所问。此外，子节点内部存在逻辑重叠，例如节点2和节点3都在讨论HDD层的重建参数和过程，可以合并。）
