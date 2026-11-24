# N529: 在 P_core < P_core_critical 且 P99_mix > T 的双重约束下，最优策略从混合转为全公有云CDN的决策阈值：当 P_core <

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N174

## Claim

在 P_core < P_core_critical 且 P99_mix > T 的双重约束下，最优策略从混合转为全公有云CDN的决策阈值：当 P_core < 40% 时，全公有云CDN的总成本 C_total_public 低于混合策略 C_total_mix，且 P99_public 更容易通过增加节点密度满足 T<=150ms 约束。

## Corrected Claim

在 P_core < P_core_critical 且 P99_mix > T 的双重约束下，存在一个决策阈值 P_threshold（具体数值取决于成本结构与延迟敏感度），当 P_core < P_threshold 时，全公有云CDN的总成本 C_total_public 低于混合策略 C_total_mix，且 P99_public 更容易通过增加节点密度满足 T<=150ms 约束。

## Evidence

[质询]40% 这一具体数值阈值缺乏通用理论支持，属于特定场景下的经验参数，不同业务负载、带宽单价及 CDN 定价模型下该阈值会显著波动，直接断言为通用决策阈值存在以偏概全的风险。 | source=knowledge，逻辑自洽（成本与延迟权衡符合基本经济直觉），但 40% 为经验事实，无来源直接支持该具体数值，依据经验事实排除条款降级。
