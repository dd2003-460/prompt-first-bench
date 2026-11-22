# N308: 工作点 D（混合置信情景）：CapEx 数据为 [实时查询]（高波动），OpEx 数据为 [记忆-高置信]（低波动），此时 TCO 的方差主要由 CapEx 主

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N109

## Claim

工作点 D（混合置信情景）：CapEx 数据为 [实时查询]（高波动），OpEx 数据为 [记忆-高置信]（低波动），此时 TCO 的方差主要由 CapEx 主导，最终推荐应输出 'CapEx 区间 [Min, Max]' 对应的 TCO 区间，并指出在区间内哪些子区间推荐方案 X，哪些子区间推荐方案 Y。

## Corrected Claim

工作点 D（混合置信情景）：CapEx 数据为 [实时查询]（高波动），OpEx 数据为 [记忆-高置信]（低波动），此时 TCO 的方差主要由 CapEx 主导，最终推荐应输出 'CapEx 区间 [Min, Max]' 对应的 TCO 区间，并指出在区间内哪些子区间推荐方案 X，哪些子区间推荐方案 Y。

## Evidence

先验知识/题面给定，逻辑校验通过：在混合置信情景下，高波动项（CapEx）主导方差，输出区间并分段推荐符合决策逻辑。
