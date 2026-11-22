# N269: 本地工作站场景下的 C_downtime 计算：假设故障平均修复时间 (MTTR) 为 24 小时 (含等待备件或远程支持)，期间推理任务中断导致的机会成本为 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N78

## Claim

本地工作站场景下的 C_downtime 计算：假设故障平均修复时间 (MTTR) 为 24 小时 (含等待备件或远程支持)，期间推理任务中断导致的机会成本为 0 (无 SLA 罚款)，但需计入工程师排查与重新部署的时间成本；若工程师时薪为 $50，则 C_downtime ≈ 2h * $50 = $100/次，加上数据恢复时间 1h，总计 $150/次。

## Corrected Claim

本地工作站场景下的 C_downtime 计算：假设故障平均修复时间 (MTTR) 为 24 小时 (含等待备件或远程支持)，期间推理任务中断导致的机会成本为 0 (无 SLA 罚款)，但需计入工程师排查与重新部署的时间成本；若工程师时薪为 $50，则 C_downtime ≈ 2h * $50 = $100/次，加上数据恢复时间 1h，总计 $150/次。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程（2h * $50 + 1h * $50 = $150）与假设条件（MTTR 24h 但仅计入人工成本 3h）在逻辑上自洽，数值量级合理。

## Search Query

local workstation GPU failure downtime cost engineer time deployment recovery
