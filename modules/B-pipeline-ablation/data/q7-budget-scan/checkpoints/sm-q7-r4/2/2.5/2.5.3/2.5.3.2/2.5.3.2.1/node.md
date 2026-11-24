# N645: 在冷数据访问率极高（100%）的工作点下，Q_retrieval = 400TB，对应取回数据量 409,600 GB，此为上界约束，代表最坏情况下的流量压力。

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N234

## Claim

在冷数据访问率极高（100%）的工作点下，Q_retrieval = 400TB，对应取回数据量 409,600 GB，此为上界约束，代表最坏情况下的流量压力。

## Corrected Claim

在冷数据访问率极高（100%）的工作点下，Q_retrieval = 400TB，对应取回数据量 409,600 GB，此为上界约束，代表最坏情况下的流量压力。

## Evidence

先验知识/题面给定，逻辑校验通过：400TB * 1024 GB/TB = 409,600 GB，数值换算准确，且符合冷数据全量取回的最坏情况定义。
