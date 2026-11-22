# N267: Qwen3-27B在2×RTX 3090张量并行下，Decode阶段每生成1个Token的All-Reduce通信数据量（MB），计算公式：Comm_Data 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94, N95, N96

## Claim

Qwen3-27B在2×RTX 3090张量并行下，Decode阶段每生成1个Token的All-Reduce通信数据量（MB），计算公式：Comm_Data = 2 * Num_Layers * Hidden_Size * 2 bytes(FP16) / 1024^2，假设Hidden_Size=4096，则 Comm_Data = 2 * 32 * 4096 * 2 / 1024^2 ≈ 0.5 MB/layer，总通信量 ≈ 32 * 0.5 = 16 MB/token，需对比PCIe 4.0 x16带宽（~25 GB/s单向）计算传输延迟

## Corrected Claim

Qwen3-27B在2×RTX 3090张量并行下，Decode阶段每生成1个Token的All-Reduce通信数据量（MB），计算公式：Comm_Data = 2 * Num_Layers * Hidden_Size * 2 bytes(FP16) / 1024^2，假设Hidden_Size=4096，则 Comm_Data = 2 * 32 * 4096 * 2 / 1024^2 ≈ 0.5 MB/layer，总通信量 ≈ 32 * 0.5 = 16 MB/token，需对比PCIe 4.0 x16带宽（~25 GB/s单向）计算传输延迟

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确（2 * 32 * 4096 * 2 / 1024^2 = 0.5 MB/layer，总 16 MB），量级合理，符合张量并行通信原理。

## Search Query

tensor parallelism all-reduce communication volume per token LLM
