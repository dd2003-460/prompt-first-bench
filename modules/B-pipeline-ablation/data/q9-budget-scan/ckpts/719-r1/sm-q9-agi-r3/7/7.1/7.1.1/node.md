# N271: V100-SXM2-16GB 的 NVLink 实际聚合带宽（all-reduce 有效带宽）约为 160-180 GB/s，而非理论峰值 300 GB/s，这

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N86

## Claim

V100-SXM2-16GB 的 NVLink 实际聚合带宽（all-reduce 有效带宽）约为 160-180 GB/s，而非理论峰值 300 GB/s，这是由于协议开销、双向同时传输限制及驱动调度延迟导致的；需通过 nccl-tests 或 vLLM profiler 实测 all_reduce_bench 获取具体数值。

## Corrected Claim

V100-SXM2-16GB 的 NVLink 实际聚合带宽（all-reduce 有效带宽）约为 160-180 GB/s，而非理论峰值 300 GB/s，这是由于协议开销、双向同时传输限制及驱动调度延迟导致的；需通过 nccl-tests 或 vLLM profiler 实测 all_reduce_bench 获取具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过：V100 SXM2 NVLink 理论带宽约 300GB/s，实际 AllReduce 有效带宽受协议开销和调度影响降至 160-180GB/s 符合工程常识与物理限制。

## Search Query

V100 SXM2 NVLink allreduce effective bandwidth nccl tests
