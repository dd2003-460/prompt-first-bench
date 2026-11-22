# N123: 64K 上下文下的总显存需求下限公式：Total_VRAM_64K = Weight_Size(精度) + KV_64K + Activation_Buffer

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

64K 上下文下的总显存需求下限公式：Total_VRAM_64K = Weight_Size(精度) + KV_64K + Activation_Buffer(~2GB)，若 Total_VRAM_64K > 24GB，则 RTX 4090 (24GB) 被排除出候选集；若 > 32GB，则 RTX 5090 (32GB) 在 BF16 下被排除，需转向 FP8 量化或更大显存卡。

## Corrected Claim

64K 上下文下的总显存需求下限公式：Total_VRAM_64K = Weight_Size(精度) + KV_64K + Activation_Buffer(~2GB)，若 Total_VRAM_64K > 24GB，则 RTX 4090 (24GB) 被排除出候选集；若 > 32GB，则 RTX 5090 (32GB) 在 BF16 下被排除，需转向 FP8 量化或更大显存卡。

## Evidence

先验知识/题面给定，逻辑校验通过：显存需求公式符合大模型推理显存构成原理（权重+KV Cache+激活值），RTX 4090/5090 显存规格及排除逻辑符合硬件事实与工程直觉。
