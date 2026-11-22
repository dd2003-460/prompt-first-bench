# N168: Batch Size 对通信占比的影响：当 B=1 时，通信占比 ≈ 0.068% (基于 memory-bound 估算)；当 B=32 时，C_total 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

Batch Size 对通信占比的影响：当 B=1 时，通信占比 ≈ 0.068% (基于 memory-bound 估算)；当 B=32 时，C_total = 16 MB/step，T_comm = 16 MB / 28 GB/s ≈ 571 μs/step，T_comp_mem = 26.8 ms * 32 ≈ 857.6 ms/step (假设线性扩展)，通信占比 ≈ 0.067%，基本不变；但若计算成为瓶颈 (compute-bound)，T_comp 随 B 线性增加而 T_comm 也线性增加，占比保持不变，需区分 memory-bound 和 compute-bound 场景。

## Corrected Claim

Batch Size 对通信占比的影响：当 B=1 时，通信占比 ≈ 0.068% (基于 memory-bound 估算)；当 B=32 时，C_total = 16 MB/step，T_comm = 16 MB / 28 GB/s ≈ 571 μs/step，T_comp_mem = 26.8 ms * 32 ≈ 857.6 ms/step (假设线性扩展)，通信占比 ≈ 0.067%，基本不变；但若计算成为瓶颈 (compute-bound)，T_comp 随 B 线性增加而 T_comm 也线性增加，占比保持不变，需区分 memory-bound 和 compute-bound 场景。

## Evidence

先验知识/题面给定，逻辑校验通过：通信量与计算量随Batch Size线性扩展，在理想线性假设下占比保持不变，符合分布式训练通信开销的基本原理。
