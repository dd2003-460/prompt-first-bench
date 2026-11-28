# N41: NVFP4 量化后，Qwen3.8-27B 的权重体积从 FP16 的 54GB 压缩至约 13.5GB (27GB/2)，但在 V100 (CC 7.0) 上

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

NVFP4 量化后，Qwen3.8-27B 的权重体积从 FP16 的 54GB 压缩至约 13.5GB (27GB/2)，但在 V100 (CC 7.0) 上缺乏原生 FP4 Tensor Core，需通过软件模拟或反量化回 FP16/INT8 进行计算；若反量化回 FP16 计算，显存带宽需求恢复至 54GB/token，Decode 速度上限回落至 (3600GB/s)/54GB ≈ 66 tokens/s；若保持 FP4 存储但仅读取 FP4 数据（假设 vLLM 优化了 kernel），理论带宽需求降至 13.5GB，上限升至 266 tokens/s，但受限于 V100 的 INT8/FP16 计算单元吞吐，实际加速比受 ALU 指令集限制，预计仅提升 1.2-1.5x。

## Corrected Claim

NVFP4 量化后，Qwen3.8-27B 的权重体积从 FP16 的 54GB 压缩至约 13.5GB，但在 V100 (CC 7.0) 上不支持 FP4 数据类型，所有计算需反量化回 FP16/INT8，显存带宽需求恢复至 54GB/token，Decode 速度上限回落至约 66 tokens/s；由于反量化开销和 V100 的 ALU 限制，实际加速比远低于理论值，预计仅提升 1.2-1.5x。

## Evidence

[质询]V100 (CC 7.0) 不支持 FP4 格式，且其 Tensor Core 主要优化 FP16/BF16/INT8，不存在‘FP4 Tensor Core’这一硬件单元，因此‘缺乏原生 FP4 Tensor Core’的表述虽事实正确但略显冗余，更核心的问题是 V100 根本不支持 FP4 数据类型，任何 FP4 操作都必须反量化到 FP16/INT8 才能执行，不存在‘保持 FP4 存储但仅读取 FP4 数据’的高效计算路径，因为 V100 的 ALU 和 Tensor Core 无法直接处理 FP4 数据，必须经过反量化步骤，这会引入额外的计算开销和内存访问延迟，导致实际性能远低于理论带宽上限。 | 先验知识/题面给定，逻辑校验通过：V100 不支持 FP4，所有 FP4 操作需反量化，理论带宽计算基于理想化假设，实际性能受反量化开销和 ALU 限制影响，故降级为定性表述。
