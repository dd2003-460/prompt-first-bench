# N23: 并发控制的自适应批处理大小调整：根据当前GPU利用率（通过NVIDIA DCGM监控）动态调整batch_size，当GPU利用率>90%时减少batch_si

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

并发控制的自适应批处理大小调整：根据当前GPU利用率（通过NVIDIA DCGM监控）动态调整batch_size，当GPU利用率>90%时减少batch_size 20%，当利用率<50%时增加batch_size 20%，目标是将平均推理延迟控制在≤2秒/request，同时保持吞吐量≥4 requests/second。

## Corrected Claim

并发控制的自适应批处理大小调整：根据当前GPU利用率（通过NVIDIA DCGM监控）动态调整batch_size，当GPU利用率>90%时减少batch_size 20%，当利用率<50%时增加batch_size 20%，目标是将平均推理延迟控制在≤2秒/request，同时保持吞吐量≥4 requests/second。

## Evidence

先验知识/题面给定，逻辑校验通过：基于GPU利用率的自适应批处理策略符合资源调度基本逻辑，阈值设定（90%/50%）及调整幅度（20%）在工程实践中合理，目标指标（延迟≤2s，吞吐≥4 req/s）量级正常且无内部矛盾。

## Search Query

adaptive batch size GPU utilization NVIDIA DCGM vLLM throughput latency tradeoff
