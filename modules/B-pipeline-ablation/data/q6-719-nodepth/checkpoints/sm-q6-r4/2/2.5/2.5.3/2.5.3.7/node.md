# N208: 工作点 1（高性低成）：Utilization_target = 70%，Server_BW_capacity = 25Gbps，N_servers = cei

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N64, N65, N66

## Claim

工作点 1（高性低成）：Utilization_target = 70%，Server_BW_capacity = 25Gbps，N_servers = ceil(69.3 * 24 / (25 * 0.7)) = ceil(69.3 * 24 / 17.5) = ceil(94.9) = 95 台

## Corrected Claim

工作点 1（高性低成）：Utilization_target = 70%，Server_BW_capacity = 25Gbps，N_servers = ceil(69.3 * 24 / (25 * 0.7)) = ceil(69.3 * 24 / 17.5) = ceil(94.9) = 95 台

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于带宽需求（输入参数）的推导逻辑，子节点2聚焦于服务器数量（输出结果）的计算依据及硬件约束假设。两者分别处理公式链路的‘输入端’和‘输出/约束端’，职责清晰且互不重叠，共同覆盖了父节点中所有关键数值（69.3Gbps, 70%, 25Gbps, 95台）的来源与合理性解释，无冗余。）
