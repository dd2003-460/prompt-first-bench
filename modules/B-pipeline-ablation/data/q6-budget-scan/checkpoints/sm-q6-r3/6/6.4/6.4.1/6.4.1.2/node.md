# N317: 全自建策略成本对带宽单价的偏导数 $\frac{\partial C_{self}}{\partial P_{bw}}$ 等于自建节点预留带宽量 $B_{res

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N119

## Claim

全自建策略成本对带宽单价的偏导数 $\frac{\partial C_{self}}{\partial P_{bw}}$ 等于自建节点预留带宽量 $B_{reserved} \times 30$（若按流量计费）或 0（若按固定专线包月计费），需根据自建带宽计费模式确定。

## Corrected Claim

全自建策略成本对带宽单价的偏导数 $\frac{\partial C_{self}}{\partial P_{bw}}$ 等于自建节点预留带宽量 $B_{reserved} \times 30$（若按流量计费）或 0（若按固定专线包月计费），需根据自建带宽计费模式确定。

## Evidence

先验知识/题面给定，逻辑校验通过：成本对单价的偏导数在数学上等于用量，若按流量计费则成本与带宽量成正比，偏导数为带宽量（乘以时间系数30天符合月度成本逻辑）；若按固定包月计费，成本与带宽单价无关，偏导数为0。逻辑自洽且符合经济学/数学基本原理。
