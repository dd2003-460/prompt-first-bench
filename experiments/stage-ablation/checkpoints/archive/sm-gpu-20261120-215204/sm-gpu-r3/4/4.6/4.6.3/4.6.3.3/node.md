# N318: 工作点 C (混合负载)：在持续对话场景中，RTX 4090 的整体吞吐受 Prefill (计算密集) 和 Decode (内存密集) 交替影响，若 Pref

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N112

## Claim

工作点 C (混合负载)：在持续对话场景中，RTX 4090 的整体吞吐受 Prefill (计算密集) 和 Decode (内存密集) 交替影响，若 Prefill 占比 10%，Decode 占比 90%，则整体有效吞吐接近 Decode 速度，而非 Prefill 速度

## Corrected Claim

工作点 C (混合负载)：在持续对话场景中，RTX 4090 的整体吞吐受 Prefill (计算密集) 和 Decode (内存密集) 交替影响，若 Prefill 占比 10%，Decode 占比 90%，则整体有效吞吐接近 Decode 速度，而非 Prefill 速度

## Evidence

先验知识/题面给定，逻辑校验通过：在混合负载中，若某一阶段（Decode）占比极高（90%），根据加权平均原理，整体吞吐确实由该阶段主导，且Decode为内存密集瓶颈，符合LLM推理基本规律。
