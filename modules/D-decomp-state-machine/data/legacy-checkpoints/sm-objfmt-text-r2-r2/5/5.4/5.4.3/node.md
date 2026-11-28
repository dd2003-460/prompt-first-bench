# N97: 吞吐量 (Throughput) 在性价比公式中应区分为“单用户解码速度 (Decode Speed, tokens/s/user)”和“系统聚合吞吐 (Agg

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N30

## Claim

吞吐量 (Throughput) 在性价比公式中应区分为“单用户解码速度 (Decode Speed, tokens/s/user)”和“系统聚合吞吐 (Aggregate Throughput, tokens/s/system)”，对于本地交互式工作站，决策变量应为 Decode Speed；若涉及批量离线推理，则为 Aggregate Throughput = Decode Speed × Concurrency (Batch Size)。

## Corrected Claim

吞吐量 (Throughput) 在性价比公式中应区分为“单用户解码速度 (Decode Speed, tokens/s/user)”和“系统聚合吞吐 (Aggregate Throughput, tokens/s/system)”，对于本地交互式工作站，决策变量应为 Decode Speed；若涉及批量离线推理，则为 Aggregate Throughput = Decode Speed × Concurrency (Batch Size)。

## Evidence

先验知识/题面给定，逻辑校验通过：吞吐量定义及并发关系符合系统性能基本逻辑
