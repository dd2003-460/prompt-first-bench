# N168: TP=4 同步开销量化：在 V100-SXM2 集群上，TP=4 的 AllReduce 通信延迟 T_comm ≈ 2 * hidden_dim * seq_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

TP=4 同步开销量化：在 V100-SXM2 集群上，TP=4 的 AllReduce 通信延迟 T_comm ≈ 2 * hidden_dim * seq_len * batch_size * 2 bytes / 300 GB/s；对于 Qwen3-27B (hidden_dim=4096, batch_size=1)，seq_len=2048 时 T_comm ≈ 0.11 ms/step；若单步计算时间 T_compute < 0.5 ms，则通信占比 C_comm > 20%，此时 MTP×4 的并行收益被通信阻塞抵消，应降级为 MTP×2 或 TP=2

## Corrected Claim

TP=4 同步开销量化：在 V100-SXM2 集群上，TP=4 的 AllReduce 通信延迟 T_comm ≈ 2 * hidden_dim * seq_len * batch_size * 2 bytes / 300 GB/s；对于 Qwen3-27B (hidden_dim=4096, batch_size=1)，seq_len=2048 时 T_comm ≈ 0.11 ms/step；若单步计算时间 T_compute < 0.5 ms，则通信占比 C_comm > 20%，此时 MTP×4 的并行收益被通信阻塞抵消，应降级为 MTP×2 或 TP=2

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（2*4096*2048*1*2/300GB/s ≈ 0.11ms），通信占比推导符合逻辑（0.11/0.5 = 22% > 20%），结论合理。
