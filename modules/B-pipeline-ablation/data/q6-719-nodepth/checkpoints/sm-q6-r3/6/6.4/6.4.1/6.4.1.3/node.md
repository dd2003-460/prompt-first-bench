# N512: 修正后的公有云带宽成本计算：使用有效单价 ¥0.15/GB。当 s=1MB 时，C_bandwidth_public = 1 * 0.15 = ¥0.15/10

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N169

## Claim

修正后的公有云带宽成本计算：使用有效单价 ¥0.15/GB。当 s=1MB 时，C_bandwidth_public = 1 * 0.15 = ¥0.15/1000req；当 s=5MB 时，C_bandwidth_public = 5 * 0.15 = ¥0.75/1000req。原 claim 中的 ¥0.24 和 ¥1.22 是基于未打折单价 ¥0.25/GB 的计算，需修正为折扣后数值。

## Corrected Claim

修正后的公有云带宽成本计算：使用有效单价 ¥0.15/GB。当 s=1MB 时，C_bandwidth_public = 1 * 0.15 = ¥0.15/1000req；当 s=5MB 时，C_bandwidth_public = 5 * 0.15 = ¥0.75/1000req。原 claim 中的 ¥0.24 和 ¥1.22 是基于未打折单价 ¥0.25/GB 的计算，需修正为折扣后数值。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 1*0.15=0.15 和 5*0.15=0.75 数学正确，且符合带宽成本随数据量线性增长的物理/经济直觉。
