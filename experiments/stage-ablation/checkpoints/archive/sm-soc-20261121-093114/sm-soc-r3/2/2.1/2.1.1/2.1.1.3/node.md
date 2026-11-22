# N137: S_signal < 0 时决策时间延长的机制：T_decision' = T_decision * (1 + η_neg * |S_signal|)，其中 η

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N44

## Claim

S_signal < 0 时决策时间延长的机制：T_decision' = T_decision * (1 + η_neg * |S_signal|)，其中 η_neg 为负面信号敏感度系数，通常 η_neg > η（负面信号影响更强），需通过不同信号强度下的决策时间变化曲线估计 η_neg 的值，验证 η_neg / η 的比值是否显著大于 1。

## Corrected Claim

S_signal < 0 时决策时间延长的机制：T_decision' = T_decision * (1 + η_neg * |S_signal|)，其中 η_neg 为负面信号敏感度系数，通常 η_neg > η（负面信号影响更强），需通过不同信号强度下的决策时间变化曲线估计 η_neg 的值，验证 η_neg / η 的比值是否显著大于 1。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

negative signal sensitivity coefficient decision time extension curve estimation
