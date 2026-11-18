# N199: 2x RTX 4090 方案中，NVLink 互联带宽为 900 GB/s (双向)，在 Tensor Parallelism 模式下，All-Reduce 通

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

2x RTX 4090 方案中，NVLink 互联带宽为 900 GB/s (双向)，在 Tensor Parallelism 模式下，All-Reduce 通信开销占推理时间的比例取决于模型层数与通信频率，通常占 5-10%，需从理论吞吐量中扣除该部分以得到有效吞吐量。

## Corrected Claim

2x RTX 4090 方案中，NVLink 互联带宽为 900 GB/s (双向)，在 Tensor Parallelism 模式下，All-Reduce 通信开销占推理时间的比例取决于模型层数与通信频率，通常占 5-10%，需从理论吞吐量中扣除该部分以得到有效吞吐量。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 NVLink 带宽 900GB/s 符合硬件规格，TP 模式下 All-Reduce 开销 5-10% 符合大模型推理通信占比的工程经验量级。
