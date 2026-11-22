# N45: 量化质量评估基准：Qwen3-27B 在 INT4/AWQ 量化下的 MMLU 准确率下降通常 < 1-2% (相对于 BF16)，Perplexity (困惑

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

量化质量评估基准：Qwen3-27B 在 INT4/AWQ 量化下的 MMLU 准确率下降通常 < 1-2% (相对于 BF16)，Perplexity (困惑度) 增加 < 0.1-0.3；若任务对长文本逻辑推理敏感，INT4 可能导致 CoT (Chain-of-Thought) 推理链断裂率上升约 5-10% [待核验: 需具体基准测试数据]。

## Corrected Claim

Qwen3-27B 在 INT4/AWQ 量化下，MMLU 准确率通常会有轻微下降，Perplexity 略有增加；若任务对长文本逻辑推理敏感，INT4 可能导致 CoT 推理链断裂率上升。具体数值需参考特定基准测试报告。

## Evidence

[质询]该陈述包含具体的经验性数值指标（MMLU下降<1-2%、Perplexity增加<0.1-0.3、CoT断裂率上升5-10%），这些属于硬件/模型量化后的具体性能表现，无法从第一性原理推导，且参考来源[1]仅涉及MathVision的提示词格式，未提供MMLU、Perplexity或CoT断裂率的具体量化对比数据，缺乏直接证据支持。 | 逻辑上量化导致精度轻微下降符合直觉，但具体数值（如<1-2%）属于经验事实，参考来源[1]与MMLU/Perplexity/CoT断裂率主题无关，无法提供直接支持，故降级。

## Retrieval Sources

- {'url': 'https://huggingface.co/cyankiwi/Qwen3.8-27B-AWQ-INT4&rut=0dad223a751e6ff7e2d4fd594f5f1931beee36efb701300aeede2c8bb62d4ddf', 'type': 'ddg', 'title': 'cyankiwi/Qwen3.8-27B-AWQ-INT4 · Hugging Face'}
