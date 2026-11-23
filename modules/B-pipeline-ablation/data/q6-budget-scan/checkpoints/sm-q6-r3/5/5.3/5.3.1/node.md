# N78: 预热对象选择策略：基于历史热度排名，选取 Top-K 热点对象进行预热，K 由预热预算 B_warm 决定：K = B_warm / (s_avg * c_ba

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

预热对象选择策略：基于历史热度排名，选取 Top-K 热点对象进行预热，K 由预热预算 B_warm 决定：K = B_warm / (s_avg * c_bandwidth)

## Corrected Claim

预热对象选择策略：基于历史热度排名，选取 Top-K 热点对象进行预热，K 由预热预算 B_warm 决定：K = B_warm / (s_avg * c_bandwidth)

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别聚焦于热度分布特性（Zipf指数α）、资源竞争约束（带宽预算B_warm与回源带宽的关系）、以及时间稳定性窗口（T_stability与半衰期t_half），彼此正交且无重复。它们共同覆盖了父节点中K值确定所需的关键因素：流量集中度、资源限制和时效性，因此具备完备性。未发现冗余，因为每个子节点引入了独立的变量或约束条件。）
