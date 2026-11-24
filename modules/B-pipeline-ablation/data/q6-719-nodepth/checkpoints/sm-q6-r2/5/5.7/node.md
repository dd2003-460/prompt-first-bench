# N39: 自建POP的固定成本摊销随 POP 数量 N_pop 增加而摊薄，单位请求固定成本 C_fixed_per_req = C_fixed_total / Q_to

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

自建POP的固定成本摊销随 POP 数量 N_pop 增加而摊薄，单位请求固定成本 C_fixed_per_req = C_fixed_total / Q_total，其中 C_fixed_total 为所有POP的硬件摊销+运维人力成本。

## Corrected Claim

自建POP的固定成本摊销随 POP 数量 N_pop 增加而摊薄，单位请求固定成本 C_fixed_per_req = C_fixed_total / Q_total，其中 C_fixed_total 为所有POP的硬件摊销+运维人力成本。

## Evidence

父节点级核验未通过：不完备（子节点在成本构成上正交（硬件、机房电力、人力），无重复。但存在两个主要问题：1. 完备性不足：父节点明确提到 C_fixed_total 包含'硬件摊销'，但子节点仅提供了'硬件总成本'（资本支出），未提供摊销系数（如折旧年限或月摊销率），导致无法直接计算父节点定义的 C_fixed_total；2. 概念混淆：子节点2标题为'月度'成本，而子节点1和3为'年度/总量'成本，时间维度不统一，且子节点2未明确是月度还是年度，与父节点的'固定成本摊销'（通常基于年度或项目周期）在量纲上未对齐。）
