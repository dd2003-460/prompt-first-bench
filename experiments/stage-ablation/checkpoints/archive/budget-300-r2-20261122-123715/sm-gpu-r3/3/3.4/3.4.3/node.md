# N78: 故障成本模型 C_failure = P_fail * (C_repair + C_downtime)，其中 C_repair 为维修/更换硬件成本（消费级卡通

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

故障成本模型 C_failure = P_fail * (C_repair + C_downtime)，其中 C_repair 为维修/更换硬件成本（消费级卡通常直接报废，数据中心卡可保修更换），C_downtime 为停机损失（本地工作站通常无 SLA 罚款，但需计算重新部署/数据恢复的时间成本 * 时薪）。

## Corrected Claim

故障成本模型 C_failure = P_fail * (C_repair + C_downtime)，其中 C_repair 为维修/更换硬件成本（消费级卡通常直接报废，数据中心卡可保修更换），C_downtime 为停机损失（本地工作站通常无 SLA 罚款，但需计算重新部署/数据恢复的时间成本 * 时薪）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的 C_repair（按硬件等级区分）和 C_downtime（特定场景），维度清晰无重叠；C_failure 中的 P_fail 虽未单独列出子节点，但通常作为独立概率参数处理，且 C_downtime 已覆盖时间成本，逻辑上完备。）
