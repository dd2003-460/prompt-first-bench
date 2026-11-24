# N209: 工作点 2（中性价比最优）：Utilization_target = 60%，Server_BW_capacity = 10Gbps，N_servers = c

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64, N65, N66

## Claim

工作点 2（中性价比最优）：Utilization_target = 60%，Server_BW_capacity = 10Gbps，N_servers = ceil(69.3 * 24 / (10 * 0.6)) = ceil(69.3 * 24 / 6) = ceil(277.2) = 278 台，平衡硬件成本与 P99 抖动容忍度

## Corrected Claim

工作点 2（中性价比最优）：Utilization_target = 60%，Server_BW_capacity = 10Gbps，N_servers = ceil(69.3 * 24 / (10 * 0.6)) = ceil(69.3 * 24 / 6) = ceil(277.2) = 278 台，平衡硬件成本与 P99 抖动容忍度

## Evidence

父节点级核验未通过：不完备（子节点分别关注硬件/计算资源瓶颈（CPU）和延迟/队列模型（P99），两者正交且无冗余。但父节点明确提到‘平衡硬件成本’，而子节点中完全缺失关于成本估算、TCO或性价比对比的分析，导致‘完备性’不足。）
