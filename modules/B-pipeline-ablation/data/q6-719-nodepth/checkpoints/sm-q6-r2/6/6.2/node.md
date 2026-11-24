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

父节点级核验通过：正交+完备+无冗余（子节点分别针对父节点公式中的三个核心组成部分（基础设施、带宽/请求、运维）进行独立展开，维度清晰，互不重叠。子节点1聚焦基础设施成本的定义与分类；子节点2聚焦带宽与请求计费的权衡及主导性判断；子节点3聚焦运维成本的线性与非线性结构。三者共同构成了对总成本公式的完整分解，无冗余重复。）
