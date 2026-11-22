# N15: 推理吞吐量 (Throughput) = Batch_Size × Tokens_per_Second_per_Request，受限于显存带宽（Memory B

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

推理吞吐量 (Throughput) = Batch_Size × Tokens_per_Second_per_Request，受限于显存带宽（Memory Bandwidth）和计算单元（Compute Units），在长上下文（32K）场景下通常处于 Memory-Bound 状态

## Corrected Claim

推理吞吐量 (Throughput) = Batch_Size × Tokens_per_Second_per_Request，受限于显存带宽（Memory Bandwidth）和计算单元（Compute Units），在长上下文（32K）场景下通常处于 Memory-Bound 状态

## Evidence

先验知识/题面给定，逻辑校验通过：推理阶段（Decode）主要受限于显存带宽，长上下文下KV Cache读取量大，符合Memory-Bound特征；吞吐量公式在理想并行假设下逻辑自洽。
