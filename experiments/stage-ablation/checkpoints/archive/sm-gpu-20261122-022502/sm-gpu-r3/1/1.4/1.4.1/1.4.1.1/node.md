# N130: Intel Xeon (8通道 DDR5-4800) 在持续推理负载下的实际内存带宽利用率仅为理论峰值 (307 GB/s) 的 60-70%（即 184-21

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41

## Claim

Intel Xeon (8通道 DDR5-4800) 在持续推理负载下的实际内存带宽利用率仅为理论峰值 (307 GB/s) 的 60-70%（即 184-215 GB/s），因内存控制器排队延迟和 ECC 开销导致，需使用 STREAM benchmark 实测修正。

## Corrected Claim

Intel Xeon (8通道 DDR5-4800) 在持续推理负载下的实际内存带宽利用率仅为理论峰值 (307 GB/s) 的 60-70%（即 184-215 GB/s），因内存控制器排队延迟和 ECC 开销导致，需使用 STREAM benchmark 实测修正。

## Evidence

先验知识/题面给定，逻辑校验通过：8通道DDR5-4800理论带宽307GB/s计算正确（8*4800*8/8=307.2），60-70%利用率符合服务器CPU在持续推理负载下的典型工程经验，STREAM benchmark修正建议合理

## Search Query

Intel Xeon 8 channel DDR5-4800 actual memory bandwidth utilization STREAM benchmark
