# N116: 全自建策略的月度出口带宽变动成本 $C_{bw}^{self}$ (¥/月)，基于峰值带宽需求 $B_{peak}$ 和单 Gbps 月租单价 $R_{bps}

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

全自建策略的月度出口带宽变动成本 $C_{bw}^{self}$ (¥/月)，基于峰值带宽需求 $B_{peak}$ 和单 Gbps 月租单价 $R_{bps}$ 计算：$C_{bw}^{self} = 10 \times B_{peak}^{pop} \times R_{bps}$，需根据日均 2TB 和峰值系数 $K_{peak}$ 推导单 POP 峰值带宽。

## Corrected Claim

全自建策略的月度出口带宽变动成本 $C_{bw}^{self}$ (¥/月)，基于峰值带宽需求 $B_{peak}$ 和单 Gbps 月租单价 $R_{bps}$ 计算：$C_{bw}^{self} = 10 \times B_{peak}^{pop} \times R_{bps}$，需根据日均 2TB 和峰值系数 $K_{peak}$ 推导单 POP 峰值带宽。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同带宽参数下的三个计算实例（冗余），且未覆盖父节点中‘基于日均2TB推导峰值’的关键逻辑步骤（不完备）。）

## Search Query

edge node egress bandwidth cost per Gbps China telecom
