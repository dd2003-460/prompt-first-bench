# N168: 咨询到达率 λ_consult 与降价信号 S_signal 的耦合机制：λ_consult = λ_base * S_signal * (1 + α_disc

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

咨询到达率 λ_consult 与降价信号 S_signal 的耦合机制：λ_consult = λ_base * S_signal * (1 + α_discount * (1 - P_new/P_old))；需验证当 S_signal 从 1.0 降至 0.3 时，即使价格降低 5%，λ_consult 的净变化率 Δλ/λ 是否为正，以解释为何 60% 卖家在降价后 48h 无新咨询（即 λ_consult 未显著高于基线）。

## Corrected Claim

咨询到达率 λ_consult 与降价信号 S_signal 存在耦合机制，其具体形式可能为 λ_consult = λ_base * S_signal * (1 + α_discount * (1 - P_new/P_old))。当 S_signal 显著下降（如从 1.0 降至 0.3）时，即使价格小幅降低，λ_consult 的净变化率可能仍为正或接近零，这解释了部分卖家在降价后短期内咨询量未显著高于基线的现象。

## Evidence

[质询]该陈述包含具体的经验参数（如α_discount的隐含值、S_signal的具体变化幅度0.3、价格降幅5%）以及基于这些参数得出的具体结论（净变化率为正）。虽然公式结构在逻辑上可能自洽（取决于α的大小），但缺乏外部数据支持这些特定参数组合下的实际市场行为，且‘60%卖家无新咨询’这一经验现象无法仅从给定的代数公式中严格推导出来，属于经验事实。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

inquiry rate impact price discount signaling consumer response latency e-commerce
