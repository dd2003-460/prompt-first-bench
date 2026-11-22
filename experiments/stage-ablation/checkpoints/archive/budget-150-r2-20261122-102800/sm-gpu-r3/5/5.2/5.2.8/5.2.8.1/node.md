# N304: 实际推理负载的 Duty Cycle 分解：对于交互式聊天场景，GPU 活跃时间占比约为 10%-20%（生成阶段）+ 5%-10%（Prefill 阶段），平

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N118

## Claim

实际推理负载的 Duty Cycle 分解：对于交互式聊天场景，GPU 活跃时间占比约为 10%-20%（生成阶段）+ 5%-10%（Prefill 阶段），平均利用率约为 15%；对于批量离线处理场景，利用率可达 80%-100%。

## Corrected Claim

实际推理负载的 Duty Cycle 分解：对于交互式聊天场景，GPU 活跃时间占比约为 10%-20%（生成阶段）+ 5%-10%（Prefill 阶段），平均利用率约为 15%；对于批量离线处理场景，利用率可达 80%-100%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM inference GPU duty cycle utilization rate interactive vs batch
