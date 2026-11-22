# N146: Qwen3-27B 在 MMLU 基准测试中，AWQ-INT4 量化后的准确率相比 BF16 基线下降幅度具体为 2.5%（基于 Llama-3-70B 类似规

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N54

## Claim

Qwen3-27B 在 MMLU 基准测试中，AWQ-INT4 量化后的准确率相比 BF16 基线下降幅度具体为 2.5%（基于 Llama-3-70B 类似规模模型的公开基准外推，需 Qwen3 官方报告核验）

## Corrected Claim

Qwen3-27B 在 MMLU 基准测试中，AWQ-INT4 量化后的准确率相比 BF16 基线存在一定程度的下降（具体幅度需参考官方报告或实测数据，当前基于类似规模模型外推约为 2.5%）。

## Evidence

[质询]该陈述明确标注为“基于 Llama-3-70B 类似规模模型的公开基准外推”，属于推测性数据而非实测事实，且参考来源仅涉及 MathVision 提示词格式，未提供 MMLU 基准测试的具体准确率数值，无法证实 2.5% 这一具体数值。 | 逻辑上 INT4 量化导致精度下降符合常识，但 2.5% 的具体数值缺乏直接来源支持（来源 [1] 仅提及 MathVision 评估方法，未涉及 MMLU 数据），且陈述本身承认是外推值，故降级为定性表述。

## Search Query

Qwen3-27B AWQ INT4 MMLU accuracy drop benchmark

## Retrieval Sources

- {'url': 'https://huggingface.co/cyankiwi/Qwen3.8-27B-AWQ-INT4&rut=0dad223a751e6ff7e2d4fd594f5f1931beee36efb701300aeede2c8bb62d4ddf', 'type': 'ddg', 'title': 'cyankiwi/Qwen3.8-27B-AWQ-INT4 · Hugging Face'}
