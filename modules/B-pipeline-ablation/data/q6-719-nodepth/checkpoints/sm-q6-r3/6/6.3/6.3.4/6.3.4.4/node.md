# N509: 多线BGP接入对RTT_user_pop的降低效应量化：部署BGP后，跨网RTT惩罚 ΔT_cross (15-25ms, 见N186) 被消除，RTT_use

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N168

## Claim

多线BGP接入对RTT_user_pop的降低效应量化：部署BGP后，跨网RTT惩罚 ΔT_cross (15-25ms, 见N186) 被消除，RTT_user_pop 从平均 30ms 降至 10-15ms，使得 P99_self 可能降至 120-130ms，但仍高于公有云的 160ms 吗？否，此处需修正：若公有云因跨网调度也受影响，需对比 BGP 后自建 RTT (10-15ms) 与公有云最优路径 RTT。

## Corrected Claim

部署BGP后，跨网RTT惩罚被消除，RTT_user_pop从平均30ms降至10-15ms，使得P99_self可能降至120-130ms。若公有云P99为160ms，则自建方案在P99延迟上优于公有云；需进一步对比BGP后自建RTT与公有云最优路径RTT以确认整体优势。

## Evidence

[质询]陈述中关于公有云RTT的数值存在逻辑矛盾：前文称自建BGP后RTT降至10-15ms，P99降至120-130ms，随后问“但仍高于公有云的160ms吗？”，若公有云P99为160ms，则120-130ms显然低于160ms，而非“高于”；此外，将RTT_user_pop（10-15ms）与P99_self（120-130ms）直接关联缺乏明确的延迟构成模型支持，可能存在量纲或指标混淆。 | 先验知识/题面给定，逻辑校验发现内部数值比较矛盾（120-130ms < 160ms，非高于），且缺乏外部来源支持具体数值。
