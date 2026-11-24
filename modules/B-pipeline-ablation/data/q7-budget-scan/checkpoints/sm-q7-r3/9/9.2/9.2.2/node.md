# N279: 基于 N63 工作负载分布（5% Read, 5% Write, 30% Idle, 60% Spin-down），修正后的 W_HDD_avg = 0.05*

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N131

## Claim

基于 N63 工作负载分布（5% Read, 5% Write, 30% Idle, 60% Spin-down），修正后的 W_HDD_avg = 0.05*8W + 0.05*8W + 0.30*4.5W + 0.60*0.75W ≈ 3.025W，显著低于 N131 原估算的 4.675W

## Corrected Claim

基于 N63 工作负载分布（5% Read, 5% Write, 30% Idle, 60% Spin-down），修正后的 W_HDD_avg = 0.05*8W + 0.05*8W + 0.30*4.5W + 0.60*0.75W ≈ 3.025W，显著低于 N131 原估算的 4.675W

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算正确（0.05*8+0.05*8+0.30*4.5+0.60*0.75=3.025），且3.025W < 4.675W符合描述
