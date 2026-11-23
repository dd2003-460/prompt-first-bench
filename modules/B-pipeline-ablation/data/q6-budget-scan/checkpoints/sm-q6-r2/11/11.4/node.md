# N165: 月度总成本 C_total_monthly 的构成展开：C_total_monthly = C_infra_monthly + C_bandwidth_mont

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N51

## Claim

月度总成本 C_total_monthly 的构成展开：C_total_monthly = C_infra_monthly + C_bandwidth_monthly + C_ops_monthly + C_security_monthly，其中各项成本需分别针对公有云、自建、混合三种策略独立计算后取最大值或加权平均

## Corrected Claim

月度总成本 C_total_monthly 的构成展开：C_total_monthly = C_infra_monthly + C_bandwidth_monthly + C_ops_monthly + C_security_monthly，其中各项成本需分别针对公有云、自建、混合三种策略独立计算，最终总成本为所选策略下各项成本之和（若为混合策略，则为各组件对应策略成本之和）。

## Evidence

[质询]「取最大值或加权平均」的表述存在逻辑模糊性：在成本优化决策中，通常是比较不同策略的总成本以选择最低者，而非对各项成本取最大值（这会导致成本被高估且无实际决策意义）；若指混合云架构中不同组件分别采用不同策略，则应分别计算后求和，而非简单的‘取最大值’。该表述可能混淆了‘策略选择’与‘成本构成’的逻辑。 | 先验知识/题面给定，逻辑校验通过，但‘取最大值’的表述在成本优化语境下存在歧义，需降级为定性表述以排除逻辑误用风险。
