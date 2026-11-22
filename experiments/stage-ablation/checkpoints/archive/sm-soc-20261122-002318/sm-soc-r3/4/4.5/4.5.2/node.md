# N68: 信息价值 (VOI) 的具体计算式：VOI = E[Max Revenue | Info] - E[Max Revenue | No Info]。在二手市场展示

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

信息价值 (VOI) 的具体计算式：VOI = E[Max Revenue | Info] - E[Max Revenue | No Info]。在二手市场展示'90天中位成交价'后，买家保留价分布从宽分布 (σ_old) 收窄至窄分布 (σ_new)，VOI 量化为 ∫(F_old(R) - F_new(R)) * (R - P_market) dR 的积分值，需确定 σ_new/σ_old 的压缩比（通常假设透明度提升使方差减少 50-70%）。

## Corrected Claim

信息价值 (VOI) 的具体计算式：VOI = E[Max Revenue | Info] - E[Max Revenue | No Info]。在二手市场展示'90天中位成交价'后，买家保留价分布从宽分布 (σ_old) 收窄至窄分布 (σ_new)，VOI 量化为 ∫(F_old(R) - F_new(R)) * (R - P_market) dR 的积分值，需确定 σ_new/σ_old 的压缩比（通常假设透明度提升使方差减少 50-70%）。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一参数（方差压缩比 σ_new/σ_old）的两个极端取值，属于同一维度的不同状态而非正交维度；且父节点明确提到的“需确定压缩比”这一核心建模步骤在子节点中未被覆盖，子节点直接跳到了结果分析，导致完备性缺失。）

## Search Query

value of information price transparency variance reduction buyer surplus
