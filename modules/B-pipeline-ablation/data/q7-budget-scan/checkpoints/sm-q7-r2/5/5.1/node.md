# N26: 每 TB 年有效可用容量成本的归一化公式：C_norm = (C_total_annual) / (C_effective_TB * U_available)，

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

每 TB 年有效可用容量成本的归一化公式：C_norm = (C_total_annual) / (C_effective_TB * U_available)，其中 C_total_annual = C_hw + C_power + C_ops + C_RTO_annualized，C_effective_TB 为扣除冗余/开销后的净容量，U_available 为年化可用率 [knowledge]

## Corrected Claim

每 TB 年有效可用容量成本的归一化公式：C_norm = (C_total_annual) / (C_effective_TB * U_available)，其中 C_total_annual = C_hw + C_power + C_ops + C_RTO_annualized，C_effective_TB 为扣除冗余/开销后的净容量，U_available 为年化可用率 [knowledge]

## Evidence

父节点级核验未通过：不完备（子节点仅涵盖了总成本公式中的两个组成部分（C_ops 和 C_RTO），缺失了硬件成本（C_hw）、电力成本（C_power）以及分母中关键的净容量（C_effective_TB）和可用率（U_available）的定义或计算，导致无法复现父节点的归一化公式，不完备。）
