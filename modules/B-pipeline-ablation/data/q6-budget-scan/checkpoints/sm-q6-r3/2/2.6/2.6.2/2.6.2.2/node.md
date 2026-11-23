# N283: 带宽包最优组合优化问题：Min C_bandwidth_package s.t. Sum(N_i * B_i) >= P95_Bandwidth_Mbps，其中

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N93

## Claim

带宽包最优组合优化问题：Min C_bandwidth_package s.t. Sum(N_i * B_i) >= P95_Bandwidth_Mbps，其中 B_i 为第i种带宽包规格（如100Mbps/500Mbps/1Gbps），N_i 为购买数量，p_i 为对应单价；由于阶梯定价通常存在规模效应，需枚举不同组合计算总成本，通常接近满载的大包比多个小包更划算

## Corrected Claim

带宽包最优组合优化问题：Min C_bandwidth_package s.t. Sum(N_i * B_i) >= P95_Bandwidth_Mbps，其中 B_i 为第i种带宽包规格（如100Mbps/500Mbps/1Gbps），N_i 为购买数量，p_i 为对应单价；由于阶梯定价通常存在规模效应，需枚举不同组合计算总成本，通常接近满载的大包比多个小包更划算

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN bandwidth package tiered pricing optimization
