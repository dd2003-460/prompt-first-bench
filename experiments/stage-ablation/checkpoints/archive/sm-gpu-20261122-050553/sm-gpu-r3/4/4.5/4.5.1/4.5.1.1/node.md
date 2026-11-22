# N278: TP=2 张量并行通信开销量化：每层 All-Reduce 通信数据量 ≈ 2 × Batch_Size × Hidden_Size × Bytes_per_e

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

TP=2 张量并行通信开销量化：每层 All-Reduce 通信数据量 ≈ 2 × Batch_Size × Hidden_Size × Bytes_per_elem；对于 Qwen3-27B (Hidden=4096, FP16)，Batch=1 时单层通信量 ≈ 16KB，PCIe 4.0 x16 (32GB/s) 传输延迟 ≈ 0.5μs/层，48 层总延迟 ≈ 24μs，远小于 N92 声称的 5-10ms，表明通信瓶颈主要存在于大 Batch Size 场景。

## Corrected Claim

TP=2 张量并行通信开销量化：每层 All-Reduce 通信数据量 ≈ 2 × Batch_Size × Hidden_Size × Bytes_per_elem；对于 Qwen3-27B (Hidden=4096, FP16)，Batch=1 时单层通信量 ≈ 16KB，PCIe 4.0 x16 (32GB/s) 传输延迟 ≈ 0.5μs/层，48 层总延迟 ≈ 24μs，远小于 N92 声称的 5-10ms，表明通信瓶颈主要存在于大 Batch Size 场景。

## Evidence

先验知识/题面给定，逻辑校验通过：计算量级正确（2*1*4096*2B=16KB），PCIe 4.0 带宽下延迟估算合理（16KB/32GB/s ≈ 0.5μs），总延迟远小于毫秒级，结论符合大模型推理通信瓶颈的一般规律。

## Search Query

tensor parallelism all-reduce latency pcie 4.0 bandwidth calculation
