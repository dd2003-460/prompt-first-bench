# N11: 分析多卡互联拓扑对推理性能的影响：NVLink (900GB/s) vs PCIe 4.0 x16 (32GB/s) vs PCIe 5.0 x16 (64GB

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

分析多卡互联拓扑对推理性能的影响：NVLink (900GB/s) vs PCIe 4.0 x16 (32GB/s) vs PCIe 5.0 x16 (64GB/s) 在张量并行(Tensor Parallelism)中的带宽瓶颈，计算2×RTX 4090 (无NVLink) 在BF16推理时的通信开销占比（约15-25%时间损失）

## Corrected Claim

分析多卡互联拓扑对推理性能的影响：NVLink (900GB/s) vs PCIe 4.0 x16 (32GB/s) vs PCIe 5.0 x16 (64GB/s) 在张量并行(Tensor Parallelism)中的带宽瓶颈，计算2×RTX 4090 (无NVLink) 在BF16推理时的通信开销占比（约15-25%时间损失）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

multi-GPU tensor parallelism NVLink PCIe bandwidth LLM inference overhead RTX 4090
