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

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的 KV_Cache_Max、Activation_Overhead 和 CUDA 上下文开销三个独立组成部分，逻辑清晰且互不重叠；三者共同覆盖了除权重外的所有显存开销项，符合公式定义，无冗余或遗漏。）

## Search Query

LLM inference VRAM overhead activations CUDA context memory usage estimate
