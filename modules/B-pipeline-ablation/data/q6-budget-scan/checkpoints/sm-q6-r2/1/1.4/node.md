# N10: 时间峰值系数 $K_{peak}$ 定义为日峰值带宽与日均带宽之比，即 $K_{peak} = B_{peak} / B_{avg}$；对于 C 端媒体平台，典

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

时间峰值系数 $K_{peak}$ 定义为日峰值带宽与日均带宽之比，即 $K_{peak} = B_{peak} / B_{avg}$；对于 C 端媒体平台，典型 $K_{peak}$ 在 1.5 到 2.5 之间，需据此计算峰值带宽需求 $B_{peak} = (2 \text{ TB} / 86400 \text{ s}) \times K_{peak}$。

## Corrected Claim

时间峰值系数 $K_{peak}$ 定义为日峰值带宽与日均带宽之比，即 $K_{peak} = B_{peak} / B_{avg}$；对于 C 端媒体平台，典型 $K_{peak}$ 在 1.5 到 2.5 之间，需据此计算峰值带宽需求 $B_{peak} = (2 \text{ TB} / 86400 \text{ s}) \times K_{peak}$。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点在逻辑上相互独立且互补：节点1聚焦于K_peak的经验取值范围及持续时间（数据输入）；节点2聚焦于峰值带宽的计算公式及单位换算（核心计算）；节点3聚焦于计费模型对峰值利用率的影响（成本视角）；节点4聚焦于资源采购策略及安全余量（工程实施）。各节点分别覆盖了定义、计算、计费、采购四个不同维度，无内容重叠或矛盾，且共同构成了完整的带宽规划流程。）

## Search Query

web traffic peak to average ratio media streaming
