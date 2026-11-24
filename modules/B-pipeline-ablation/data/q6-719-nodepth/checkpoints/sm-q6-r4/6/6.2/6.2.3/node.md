# N164: D2 成本排序中的运维成本非线性项：C_ops 并非严格线性于 Q_total，自建策略中 C_ops 包含固定人力成本（不随 Q_total 变化）和可变监控

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

D2 成本排序中的运维成本非线性项：C_ops 并非严格线性于 Q_total，自建策略中 C_ops 包含固定人力成本（不随 Q_total 变化）和可变监控费用（随 Q_total 变化），公式为 C_ops_total = C_ops_fixed + Q_total * C_ops_variable_per_req，其中 C_ops_variable_per_req 约为 0.001-0.005 元/请求

## Corrected Claim

D2 成本排序中的运维成本非线性项：C_ops 并非严格线性于 Q_total，自建策略中 C_ops 包含固定人力成本（不随 Q_total 变化）和可变监控费用（随 Q_total 变化），公式为 C_ops_total = C_ops_fixed + Q_total * C_ops_variable_per_req，其中 C_ops_variable_per_req 约为 0.001-0.005 元/请求

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在两个不同参数组（人力数量、单位可变成本）下的具体数值实例，属于参数取值的冗余列举，而非概念上的正交分解。此外，父节点提到的'非线性'特性（固定+可变结构）在子节点中仅通过数值体现，未明确区分'固定部分'和'可变部分'对总成本曲线的独立贡献，导致结构解析不完整。）
