# N321: 临界带宽单价阈值 $P_{bw}^{crit}$ 的数值估算：假设 $C_{fixed}^{self} = 500,000$ 元/月，$V_{monthly} 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N120

## Claim

临界带宽单价阈值 $P_{bw}^{crit}$ 的数值估算：假设 $C_{fixed}^{self} = 500,000$ 元/月，$V_{monthly} = 60,000$ GB，$V_{self} = 54,000$ GB，则 $P_{bw}^{crit} = 500,000 / 6,000 \approx 83.3$ 元/GB，远高于实际市场价格（约 0.2-0.5 元/GB），表明在当前规模下自建策略在带宽成本维度上不具优势。

## Corrected Claim

临界带宽单价阈值 $P_{bw}^{crit}$ 的数值估算：假设 $C_{fixed}^{self} = 500,000$ 元/月，$V_{monthly} = 60,000$ GB，$V_{self} = 54,000$ GB，则 $P_{bw}^{crit} = 500,000 / 6,000 \approx 83.3$ 元/GB，远高于实际市场价格（约 0.2-0.5 元/GB），表明在当前规模下自建策略在带宽成本维度上不具优势。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 500,000 / (60,000 - 54,000) = 83.33 正确，且 83.3 元/GB 远高于市场带宽价格（0.2-0.5 元/GB）符合经济直觉，结论自洽。
