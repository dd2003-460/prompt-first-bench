# N37: 运维人力成本为 (运维人员数量 N_ops * 人均年薪 S_ops) / 365 天，N_ops 与POP数量 N_pop 和公有云CDN使用量 Q_clou

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

运维人力成本为 (运维人员数量 N_ops * 人均年薪 S_ops) / 365 天，N_ops 与POP数量 N_pop 和公有云CDN使用量 Q_cloud 相关，典型比例为 1人管理 2-5 个POP或 100TB 公有云流量。

## Corrected Claim

运维人力成本为 (运维人员数量 N_ops * 人均年薪 S_ops) / 365 天，N_ops 与POP数量 N_pop 和公有云CDN使用量 Q_cloud 相关，典型比例为 1人管理 2-5 个POP或 100TB 公有云流量。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：分别定义了自建和公有云场景下的人员数量（基于不同驱动因子）、统一的人均薪资参数，以及各自对应的成本计算结果。虽然最后两个节点是前三个节点的线性组合，但在成本分解树中，将‘资源量’、‘单价’和‘总成本’分层展示是标准做法，不属于冗余。父节点中提到的‘或’关系（POP数或流量）已被子节点正确拆解为两种独立场景的并行计算，覆盖了所有关键方面。）
