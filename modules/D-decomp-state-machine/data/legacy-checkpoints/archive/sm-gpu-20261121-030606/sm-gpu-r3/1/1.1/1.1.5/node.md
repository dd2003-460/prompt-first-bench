# N84: NVFP4/W4 精度下 Qwen3-27B 总显存下限 = 13.5GB (权重) + 4.7GB (KV) + 2.5GB (激活) = 20.7GB，24

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7, N8, N9

## Claim

NVFP4/W4 精度下 Qwen3-27B 总显存下限 = 13.5GB (权重) + 4.7GB (KV) + 2.5GB (激活) = 20.7GB，24GB 显存可行且留有 13.75% 余量，这是唯一能在 24GB 卡上运行 27B 模型的精度选项

## Corrected Claim

NVFP4/W4 精度下 Qwen3-27B 总显存下限 = 13.5GB (权重) + 4.7GB (KV) + 2.5GB (激活) = 20.7GB，24GB 显存可行且留有 13.75% 余量，这是唯一能在 24GB 卡上运行 27B 模型的精度选项

## Evidence

先验知识/题面给定，逻辑校验通过：NVFP4权重约13.5GB，KV Cache与激活值估算合理，总和20.7GB小于24GB，余量计算正确，且符合24GB显存运行27B模型需低精度量化的工程常识。

## Search Query

4-bit quantization LLM inference VRAM requirement
