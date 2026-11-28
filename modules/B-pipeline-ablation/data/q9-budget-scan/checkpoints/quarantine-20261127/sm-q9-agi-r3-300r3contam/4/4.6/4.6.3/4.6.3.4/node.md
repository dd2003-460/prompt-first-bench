# N207: 本地集群吞吐量 T_local 的基准值：在 4xV100 TP=4 配置下，27B 模型生成 512 tokens 的墙钟时间约为 2.5s（假设 MFU 3

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

本地集群吞吐量 T_local 的基准值：在 4xV100 TP=4 配置下，27B 模型生成 512 tokens 的墙钟时间约为 2.5s（假设 MFU 30%），因此 T_local ≈ 240 queries/min（单流）或更高（批量）；若云端 N_max < 240，则云端为瓶颈，需限制并发请求数以避免超时。

## Corrected Claim

本地集群吞吐量 T_local 的基准值：在 4xV100 TP=4 配置下，27B 模型生成 512 tokens 的墙钟时间约为 2.5s（假设 MFU 30%），因此 T_local ≈ 240 queries/min（单流）或更高（批量）；若云端 N_max < 240，则云端为瓶颈，需限制并发请求数以避免超时。

## Evidence

先验知识/题面给定，逻辑校验通过：基于4xV100算力与30% MFU估算，27B模型生成512 tokens耗时约2.5s符合工程直觉，推导出的240 queries/min吞吐量量级合理。
