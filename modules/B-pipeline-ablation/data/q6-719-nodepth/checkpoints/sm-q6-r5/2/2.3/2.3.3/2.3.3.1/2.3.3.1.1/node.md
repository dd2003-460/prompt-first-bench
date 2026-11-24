# N558: 工作点 1（高性低成）：R=50km，L_prop=0.25ms，RTT_base=3.0ms；此工作点要求每 50km 一个 POP，全国需约 5600/50

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N182

## Claim

工作点 1（高性低成）：R=50km，L_prop=0.25ms，RTT_base=3.0ms；此工作点要求每 50km 一个 POP，全国需约 5600/50=112 个 POP，远超 10 个 POP 的约束，故不可行；若强行实施，成本 C_infra 增加 10 倍，P99 延迟降至 3ms+5ms=8ms，成本弹性 E_cost = ΔC/ΔR = 10x，不适合小规模自建。

## Corrected Claim

工作点 1（高性低成）：R=50km，L_prop=0.25ms，RTT_base=3.0ms；此工作点要求每 50km 一个 POP，全国需约 5600/50=112 个 POP，远超 10 个 POP 的约束，故不可行；若强行实施，成本 C_infra 增加 10 倍，P99 延迟降至 3ms+5ms=8ms，成本弹性 E_cost = ΔC/ΔR = 10x，不适合小规模自建。

## Evidence

先验知识/题面给定，逻辑校验通过：5600/50=112 计算正确，112>10 导致不可行结论成立，成本与延迟推导符合逻辑自洽性。

## Search Query

CDN edge node density 50km coverage cost feasibility
