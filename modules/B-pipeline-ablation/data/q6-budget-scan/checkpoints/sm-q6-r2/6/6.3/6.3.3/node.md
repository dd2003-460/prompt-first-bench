# N116: 全自建策略的月度出口带宽变动成本 $C_{bw}^{self}$ (¥/月)，基于峰值带宽需求 $B_{peak}$ 和单 Gbps 月租单价 $R_{bps}

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N28

## Claim

全自建策略的月度出口带宽变动成本 $C_{bw}^{self}$ (¥/月)，基于峰值带宽需求 $B_{peak}$ 和单 Gbps 月租单价 $R_{bps}$ 计算：$C_{bw}^{self} = 10 \times B_{peak}^{pop} \times R_{bps}$，需根据日均 2TB 和峰值系数 $K_{peak}$ 推导单 POP 峰值带宽。

## Corrected Claim

全自建策略的月度出口带宽变动成本 $C_{bw}^{self}$ (¥/月)，基于峰值带宽需求 $B_{peak}$ 和单 Gbps 月租单价 $R_{bps}$ 计算：$C_{bw}^{self} = 10 \times B_{peak}^{pop} \times R_{bps}$，需根据日均 2TB 和峰值系数 $K_{peak}$ 推导单 POP 峰值带宽。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

edge node egress bandwidth cost per Gbps China telecom
