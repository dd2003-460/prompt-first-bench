# N41: D2 成本排序判据为每千请求的总成本 C_total_per_1000req = (C_infra + C_bandwidth + C_ops) / Q_tot

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6

## Claim

D2 成本排序判据为每千请求的总成本 C_total_per_1000req = (C_infra + C_bandwidth + C_ops) / Q_total * 1000，其中 C_infra 为基础设施成本，C_bandwidth 为带宽成本，C_ops 为运维成本。

## Corrected Claim

D2 成本排序判据为每千请求的总成本 C_total_per_1000req = (C_infra + C_bandwidth + C_ops) / Q_total * 1000，其中 C_infra 为基础设施成本，C_bandwidth 为带宽成本，C_ops 为运维成本。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的三个加项（C_infra, C_bandwidth, C_ops），逻辑上正交且覆盖了所有成本组成部分。虽然子节点2涉及了请求计费，但主要侧重于带宽主导性的判断及与对象大小的关系，与子节点1中关于基础设施计费模式的区分（资源vs请求）虽有交叉但侧重点不同（一个是成本占比结构，一个是计费模式定义），未构成严重冗余。）
