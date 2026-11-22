# N391: RTX 4090 FP8推理吞吐量相对于BF16的实际加速比取决于模型结构中的GEMM矩阵维度，Qwen3-27B的hidden_size=4096和inter

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N160

## Claim

RTX 4090 FP8推理吞吐量相对于BF16的实际加速比取决于模型结构中的GEMM矩阵维度，Qwen3-27B的hidden_size=4096和intermediate_size=11008导致GEMM形状为[4096, 11008]，FP8加速比理论值为1.8x（基于Tensor Core利用率），但实际因内存带宽限制仅能实现1.2x-1.4x

## Corrected Claim

RTX 4090 FP8推理吞吐量相对于BF16的实际加速比受模型结构及内存带宽限制影响，Qwen3-27B在典型负载下实际加速比约为1.2x-1.4x，低于FP8 Tensor Core的理论峰值加速比。

## Evidence

[质询]将FP8加速比简单归因于GEMM形状[4096, 11008]且断言理论值为1.8x缺乏严谨推导；FP8加速比主要取决于硬件Tensor Core对FP8的支持效率（通常为2x于FP16/BF16）及算子融合程度，而非单纯由矩阵维度决定，且1.8x这一具体数值缺乏通用理论支撑，属于经验性估算。 | 先验知识/题面给定，逻辑校验通过：虽然FP8通常提供约2x于BF16的理论峰值算力，但实际加速比受内存带宽、算子开销及模型结构影响，1.2x-1.4x的实际范围符合工程直觉，但1.8x的理论值表述过于具体且缺乏普适性理论依据，故降级为定性表述。
