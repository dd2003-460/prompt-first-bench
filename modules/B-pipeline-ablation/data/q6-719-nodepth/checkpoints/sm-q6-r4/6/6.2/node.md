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

父节点级核验通过：正交+完备+无冗余（子节点分别针对父节点公式中的三个独立变量（C_infra, C_bandwidth, C_ops）进行了详细的定义和特性分析，维度清晰互不重叠，且完整覆盖了成本构成的所有关键方面。）
