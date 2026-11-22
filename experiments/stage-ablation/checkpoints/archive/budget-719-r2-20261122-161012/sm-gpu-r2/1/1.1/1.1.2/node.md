# N36: Qwen3-27B 在 BF16 精度下，除权重外还需预留约 2-5% 的额外显存用于激活值 (Activations) 和 CUDA 上下文开销，计算公式为 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

Qwen3-27B 在 BF16 精度下，除权重外还需预留约 2-5% 的额外显存用于激活值 (Activations) 和 CUDA 上下文开销，计算公式为 Total_VRAM_Req = Weight_Size + KV_Cache_Max + Activation_Overhead，其中 Activation_Overhead 通常与 Batch Size 和 Seq Len 成正比。

## Corrected Claim

Qwen3-27B 在 BF16 精度下，除权重外还需预留约 2-5% 的额外显存用于激活值 (Activations) 和 CUDA 上下文开销，计算公式为 Total_VRAM_Req = Weight_Size + KV_Cache_Max + Activation_Overhead，其中 Activation_Overhead 通常与 Batch Size 和 Seq Len 成正比。

## Evidence

先验知识/题面给定，逻辑校验通过：大模型推理中激活值显存占用确实与Batch Size和Seq Len成正比，且通常占权重显存的较小比例（2-5%在常规推理配置下量级合理），公式结构符合显存构成常识。

## Search Query

LLM inference VRAM overhead activations CUDA context memory usage estimate
