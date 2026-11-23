# N319: 临界带宽单价阈值 $P_{bw}^{crit}$ 的计算公式为 $P_{bw}^{crit} = (C_{fixed}^{self} - C_{fixed}^{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N120

## Claim

临界带宽单价阈值 $P_{bw}^{crit}$ 的计算公式为 $P_{bw}^{crit} = (C_{fixed}^{self} - C_{fixed}^{cloud}) / (V_{monthly} - V_{self})$，其中 $C_{fixed}^{self}$ 为自建固定成本，$C_{fixed}^{cloud}$ 为公有云固定成本（通常为 0），$V_{self}$ 为自建节点承载流量。

## Corrected Claim

临界带宽单价阈值 $P_{bw}^{crit}$ 的计算公式为 $P_{bw}^{crit} = (C_{fixed}^{self} - C_{fixed}^{cloud}) / (V_{monthly} - V_{self})$，其中 $C_{fixed}^{self}$ 为自建固定成本，$C_{fixed}^{cloud}$ 为公有云固定成本（通常为 0），$V_{self}$ 为自建节点承载流量。

## Evidence

先验知识/题面给定，逻辑校验通过
