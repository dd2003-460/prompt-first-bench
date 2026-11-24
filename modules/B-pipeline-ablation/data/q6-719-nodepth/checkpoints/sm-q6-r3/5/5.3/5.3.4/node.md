# N98: 全自建策略月度总成本 C_total_self = C_infra_self_total + C_bw_self_total + C_ops_self_tota

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

全自建策略月度总成本 C_total_self = C_infra_self_total + C_bw_self_total + C_ops_self_total = 200,000 + 150,000 + 210,000 = ¥560,000/月，与N24中假设的¥500,000/月存在差异，需以分项计算为准。

## Corrected Claim

全自建策略月度总成本 C_total_self = C_infra_self_total + C_bw_self_total + C_ops_self_total = 200,000 + 150,000 + 210,000 = ¥560,000/月，与N24中假设的¥500,000/月存在差异，需以分项计算为准。

## Evidence

父节点级核验未通过：不完备（子节点1（修正总成本）和子节点2（单位成本）存在逻辑依赖但不完全正交，因为子节点2直接依赖子节点1的结果；更严重的是，父节点核心是“月度总成本修正”，但子节点2和3分别引入了“单位经济模型”和“延迟合规惩罚”，这超出了父节点“月度总成本”的定义范围，导致完备性不足（未覆盖父节点中提到的具体分项差异分析，如为何从560k变为300k的具体分项拆解）且边界模糊。）
