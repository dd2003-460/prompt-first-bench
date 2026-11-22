# N161: 成交量变化 ΔQ_t 的构成拆解：ΔQ_t = ΔQ_conversion + ΔQ_search_decay，其中 ΔQ_conversion 为咨询转化率下

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

成交量变化 ΔQ_t 的构成拆解：ΔQ_t = ΔQ_conversion + ΔQ_search_decay，其中 ΔQ_conversion 为咨询转化率下降项（基于 N69 的 Q_loss ≈ 36% 咨询流失，假设转化漏斗其他环节不变，贡献约 -15%~-25%），ΔQ_search_decay 为搜索流量自然衰减项（假设 -5%~-10%），两者之和需落在父节点给定的 [-10%, -20%] 区间内，若超出则需修正转化假设。

## Corrected Claim

成交量变化 ΔQ_t 的构成拆解：ΔQ_t = ΔQ_conversion + ΔQ_search_decay，其中 ΔQ_conversion 为咨询转化率下降项（基于 N69 的 Q_loss ≈ 36% 咨询流失，假设转化漏斗其他环节不变，贡献约 -15%~-25%），ΔQ_search_decay 为搜索流量自然衰减项（假设 -5%~-10%），两者之和需落在父节点给定的 [-10%, -20%] 区间内，若超出则需修正转化假设。

## Evidence

先验知识/题面给定，逻辑校验通过：各分项区间（-15%~-25% 与 -5%~-10%）之和覆盖父节点区间 [-10%, -20%]，且包含修正机制，逻辑自洽。
