# N136: Qwen3-27B NVFP4 在 TruthfulQA 上的幻觉率 HR_NVFP4，需在 817 个标准问题子集上实测，特别关注 'Trick Questi

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N38

## Claim

Qwen3-27B NVFP4 在 TruthfulQA 上的幻觉率 HR_NVFP4，需在 817 个标准问题子集上实测，特别关注 'Trick Questions' 子类，因为量化噪声可能在边缘案例中放大事实性偏差

## Corrected Claim

Qwen3-27B NVFP4 在 TruthfulQA 上的幻觉率需通过实测确定，建议关注量化噪声对边缘案例（如 Trick Questions）的影响，但具体数值及子集规模需查阅相关基准测试报告。

## Evidence

[质询]该陈述包含具体的实验设计细节（817个子集、特定子类关注点）及假设性结论（量化噪声放大偏差），属于经验性研究计划或特定论文结论，无法从第一性原理推导，且参考来源未提供相关数据支持。 | 参考来源[1]仅介绍Qwen3.8模型发布，与Qwen3-27B NVFP4在TruthfulQA上的具体幻觉率实测数据及实验设计无关，属经验事实且缺来源支持。

## Search Query

Qwen3-27B NVFP4 TruthfulQA hallucination rate

## Retrieval Sources

- {'url': 'https://huggingface.co/unsloth/Qwen3.8-27B-NVFP4&rut=649298585494e0353e44766042aaac140a369b8993256f48be998a7101210bc6', 'type': 'ddg', 'title': 'unsloth/Qwen3.8-27B-NVFP4 · Hugging Face'}
