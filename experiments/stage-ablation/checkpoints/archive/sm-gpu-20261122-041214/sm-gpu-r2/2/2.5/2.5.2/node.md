# N92: NVIDIA Hopper (H100) 架构原生支持 FP8 和 NVFP4，其 Tensor Core 在 FP8 下的理论峰值算力 (TFLOPS) 约为

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24

## Claim

NVIDIA Hopper (H100) 架构原生支持 FP8 和 NVFP4，其 Tensor Core 在 FP8 下的理论峰值算力 (TFLOPS) 约为 Ampere (A100) INT8 峰值算力的 2 倍，但在 LLM 解码阶段通常受显存带宽限制而非算力限制。

## Corrected Claim

NVIDIA Hopper (H100) 架构原生支持 FP8（但不支持 NVFP4，NVFP4 为 Blackwell 特性），其 Tensor Core 在 FP8 下的理论峰值算力 (TFLOPS) 约为 Ampere (A100) INT8 峰值算力的 4 倍（稠密），但在 LLM 解码阶段通常受显存带宽限制而非算力限制。

## Evidence

[质询]H100 架构原生支持 FP8，但 NVFP4 是 Blackwell (B100/B200) 架构引入的特性，Hopper 并不原生支持 NVFP4；此外，H100 FP8 峰值算力约为 A100 INT8 的 4 倍（而非 2 倍），具体取决于是否启用稀疏性，但通常引用稠密算力时倍数更高。 | 先验知识/题面给定，逻辑校验发现架构特性归属错误（NVFP4 属于 Blackwell）及算力倍数描述不准确，故降级。

## Search Query

H100 Hopper FP8 NVFP4 Tensor Core peak TFLOPS vs A100 INT8
