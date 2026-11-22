# N172: 信号强度阈值 s_signal > 0.7 对应的具体业务指标：当 s_signal > 0.7 时，意味着 (P_high / P_low) > 1.2 且 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N54, N55, N56

## Claim

信号强度阈值 s_signal > 0.7 对应的具体业务指标：当 s_signal > 0.7 时，意味着 (P_high / P_low) > 1.2 且 R_good > 0.95 且 N_reviews > 20（基于典型权重 α=0.4, β=0.3, γ=0.3 的逆推），该阈值下核验成本 C_verify 降低幅度 > 50% 的统计显著性需通过 A/B 测试中 p < 0.05 验证。

## Corrected Claim

在特定业务模型中，信号强度阈值 s_signal > 0.7 通常被设定为对应 (P_high / P_low) > 1.2 且 R_good > 0.95 且 N_reviews > 20 的条件（基于典型权重 α=0.4, β=0.3, γ=0.3 的逆推），该阈值下核验成本 C_verify 降低幅度 > 50% 的统计显著性需通过 A/B 测试中 p < 0.05 验证。

## Evidence

[质询]该陈述包含具体的经验性数值阈值（如 s_signal > 0.7 对应 P_high/P_low > 1.2 等）及统计显著性要求，属于特定业务场景下的经验事实或模型参数，无法从第一性原理或数学公理严格推导得出，且缺乏外部来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

signal strength threshold 0.7 cost reduction 50% A/B test second hand platform
