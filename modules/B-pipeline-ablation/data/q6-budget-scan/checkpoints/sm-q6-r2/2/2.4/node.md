# N14: 运维成本C_ops的人效模型：C_ops = (N_ops × S_ops) / R_daily，其中N_ops为运维工程师数量，S_ops为年薪（¥/年），R

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N2

## Claim

运维成本C_ops的人效模型：C_ops = (N_ops × S_ops) / R_daily，其中N_ops为运维工程师数量，S_ops为年薪（¥/年），R_daily为日请求数；通常每10个POP点需1-2名专职运维 [待核验]

## Corrected Claim

运维成本C_ops的人效模型应修正为：C_ops = (N_ops × S_ops) / (R_daily × 365)，其中N_ops为运维工程师数量，S_ops为年薪（¥/年），R_daily为日请求数，365为年天数，从而得到单位请求的运维成本（¥/req）。关于人员配置，通常每10个POP点需1-2名专职运维仅为粗略经验估算，实际需根据业务SLA和自动化水平调整。

## Evidence

[质询]公式量纲存在严重错误：分子为年薪（¥/年），分母为日请求数（req/day），计算结果单位应为 ¥·day/(year·req)，而非标准的运维成本单位（¥/req 或 ¥/year）。此外，'每10个POP点需1-2名专职运维'属于特定行业经验值，缺乏通用性，且未考虑自动化程度、业务复杂度等关键变量。 | source=knowledge，但公式量纲不自洽（年薪/日请求数无法直接得出合理成本指标），且经验参数缺乏普适性支持，逻辑校验未通过。

## Search Query

CDN operations team size per POP point headcount ratio
