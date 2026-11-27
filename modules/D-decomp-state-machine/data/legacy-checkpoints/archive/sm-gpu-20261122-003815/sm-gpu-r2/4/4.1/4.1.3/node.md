# N119: BF16 精度下 Activation Buffer 量化：对于 27B 模型在 32K 序列长度下的推理，激活值临时占用显存约为 2-5 GB（取决于 bat

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22, N23, N24

## Claim

BF16 精度下 Activation Buffer 量化：对于 27B 模型在 32K 序列长度下的推理，激活值临时占用显存约为 2-5 GB（取决于 batch size 和框架实现，如 vLLM vs llama.cpp），需从总显存中扣除。

## Corrected Claim

BF16 精度下 Activation Buffer 量化：对于 27B 模型在 32K 序列长度下的推理，激活值临时占用显存约为 2-5 GB（取决于 batch size 和框架实现，如 vLLM vs llama.cpp），需从总显存中扣除。

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型在32K序列长度下，激活值显存占用主要取决于Batch Size和框架实现（如vLLM的PagedAttention vs llama.cpp的连续批处理），2-5GB的量级在典型推理场景（小Batch或中等Batch）下符合工程经验与物理直觉，无逻辑矛盾。
