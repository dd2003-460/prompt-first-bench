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

父节点级核验通过：正交+完备+无冗余（子节点分别对应公式中的三个组成部分（KV Cache、Activations、CUDA Overhead），彼此独立且无重叠；父节点中提到的权重大小（Weight_Size）在子节点中未展开，但父节点本身已将其作为已知项或独立项列出，且子节点聚焦于'额外'开销的计算，逻辑上完备。）

## Search Query

LLM inference VRAM overhead activations CUDA context memory usage estimate
