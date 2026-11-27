# N129: 修正N21的总显存公式：Total_Mem = W_precision + KV_Cache + Activation_Peak + Framework_Ove

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

修正N21的总显存公式：Total_Mem = W_precision + KV_Cache + Activation_Peak + Framework_Overhead。N21中BF16下65GB = 54GB (权重) + 5.2GB (KV) + 2.5GB (激活) + 3.3GB (其他/碎片/Overhead)。需明确Framework_Overhead的构成（CUDA Context, cuDNN buffers等）。

## Corrected Claim

修正N21的总显存公式：Total_Mem = W_precision + KV_Cache + Activation_Peak + Framework_Overhead。N21中BF16下65GB = 54GB (权重) + 5.2GB (KV) + 2.5GB (激活) + 3.3GB (其他/碎片/Overhead)。需明确Framework_Overhead的构成（CUDA Context, cuDNN buffers等）。

## Evidence

先验知识/题面给定，逻辑校验通过：总显存公式符合GPU推理显存占用的一般构成（权重+KV Cache+激活+框架开销），且数值加和（54+5.2+2.5+3.3=65）在算术上自洽，量级符合BF16大模型推理的典型分布。

## Search Query

GPU memory overhead CUDA context inference
