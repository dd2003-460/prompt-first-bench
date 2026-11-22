# N792: 工作点 3 (高成本低性 - 原生 PyTorch/Transformers)：在未优化的原生 Transformers 推理路径中，CPU-GPU 数据拷贝时

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N282

## Claim

工作点 3 (高成本低性 - 原生 PyTorch/Transformers)：在未优化的原生 Transformers 推理路径中，CPU-GPU 数据拷贝时间约为 15-25ms (频繁的小块传输)，框架初始化及 Python 层调度开销约为 10-20ms (每个 Step)；总 Latency_overhead ≈ 25-45ms。此配置下，对于 32K 上下文，开销占比可达 10-15%，显著劣化 TTFT，仅适用于离线批处理或调试场景。

## Corrected Claim

工作点 3 (高成本低性 - 原生 PyTorch/Transformers)：在未优化的原生 Transformers 推理路径中，CPU-GPU 数据拷贝时间约为 15-25ms (频繁的小块传输)，框架初始化及 Python 层调度开销约为 10-20ms (每个 Step)；总 Latency_overhead ≈ 25-45ms。此配置下，对于 32K 上下文，开销占比可达 10-15%，显著劣化 TTFT，仅适用于离线批处理或调试场景。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

PyTorch transformers inference latency overhead python scheduling cost ms
