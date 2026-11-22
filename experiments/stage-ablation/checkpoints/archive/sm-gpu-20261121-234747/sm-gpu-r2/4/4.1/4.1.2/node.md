# N102: B类半静态事实（时效1-3年）的具体清单：包括模型参数量（如Qwen3-27B的27B参数）、精度支持矩阵（如H100支持FP8，RTX 4090不支持原生FP

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

B类半静态事实（时效1-3年）的具体清单：包括模型参数量（如Qwen3-27B的27B参数）、精度支持矩阵（如H100支持FP8，RTX 4090不支持原生FP8）、量化方法的质量损失数据（如FP8 Perplexity增加<1%）；这些参数随模型更新或驱动更新而变化，来源为HuggingFace模型卡片、NVIDIA驱动发布说明、量化库（GPTQ/AWQ）的GitHub commit，需标注具体版本号（如vLLM 0.5.1, AWQ 0.2.3）

## Corrected Claim

B类半静态事实（时效1-3年）的具体清单：包括模型参数量（如Qwen3-27B的27B参数）、精度支持矩阵（如H100支持FP8，RTX 4090不支持原生FP8）、量化方法的质量损失数据（如FP8 Perplexity增加<1%）；这些参数随模型更新或驱动更新而变化，来源为HuggingFace模型卡片、NVIDIA驱动发布说明、量化库（GPTQ/AWQ）的GitHub commit，需标注具体版本号（如vLLM 0.5.1, AWQ 0.2.3）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM model card version control precision support matrix update frequency
