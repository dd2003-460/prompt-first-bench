# N182: 在覆盖半径 R=50km 的基准工作点下，光纤单程传播延迟 L_prop = 50km / 200,000km/s = 0.25ms，往返基础延迟 RTT_ba

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

在覆盖半径 R=50km 的基准工作点下，光纤单程传播延迟 L_prop = 50km / 200,000km/s = 0.25ms，往返基础延迟 RTT_base = 2 * 0.25ms + 2.5ms (L_switching中值) = 3.0ms。

## Corrected Claim

在覆盖半径 R=50km 的基准工作点下，光纤单程传播延迟 L_prop = 50km / 200,000km/s = 0.25ms，往返基础延迟 RTT_base = 2 * 0.25ms + 2.5ms (L_switching中值) = 3.0ms。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一参数（覆盖半径 R）在不同取值下的状态枚举，存在结构性冗余；且父节点仅定义了基准计算逻辑，子节点却引入了父节点未提及的关键约束（如 10 POP 限制、抖动 L_jitter、重试成本等），导致分解超出父节点定义范围，不完备。）

## Search Query

fiber optic propagation delay calculation 200km/s
