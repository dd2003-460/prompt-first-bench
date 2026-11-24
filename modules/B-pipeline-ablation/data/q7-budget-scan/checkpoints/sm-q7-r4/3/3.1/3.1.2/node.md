# N87: PUE (Power Usage Effectiveness) 取值影响最终电费，本地自建机房PUE通常为1.3-1.5，托管机房PUE可能为1.2-1.4，需

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

PUE (Power Usage Effectiveness) 取值影响最终电费，本地自建机房PUE通常为1.3-1.5，托管机房PUE可能为1.2-1.4，需根据实际机房类型选取参数。

## Corrected Claim

PUE (Power Usage Effectiveness) 取值影响最终电费，本地自建机房PUE通常为1.3-1.5，托管机房PUE可能为1.2-1.4，需根据实际机房类型选取参数。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别聚焦于‘本地自建’、‘托管机房’和‘电价敏感性/联合建模’三个维度，彼此独立且互不重叠（正交）。它们共同覆盖了父节点中关于不同机房类型的PUE取值范围及最终电费影响的描述（完备）。虽然都涉及计算公式，但针对的场景和变量侧重不同（一个是设备选型依据，一个是服务商对比，一个是成本敏感度分析），不属于简单的参数取值冗余，而是必要的逻辑分层。）

## Search Query

data center PUE average value local vs colocation
