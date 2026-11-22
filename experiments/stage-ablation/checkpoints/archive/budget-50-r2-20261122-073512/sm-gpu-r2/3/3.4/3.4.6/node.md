# N131: Qwen3-27B 在 NVFP4/W4 量化下于 HumanEval 数据集上的具体 Pass@1 准确率 (Acc_W4_HumanEval)，用于量化 4

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

Qwen3-27B 在 NVFP4/W4 量化下于 HumanEval 数据集上的具体 Pass@1 准确率 (Acc_W4_HumanEval)，用于量化 4-bit 量化对代码生成能力的退化。

## Corrected Claim

Qwen3.6-27B 在 NVFP4 量化下精度保持良好（MMLU Pro 86.3 vs FP8 86.1），但缺乏 HumanEval 数据集上的具体 Pass@1 准确率数据。

## Evidence

[质询]参考来源中提到的模型版本为 Qwen3.6-27B 或 Qwen3.8-27B，而非 Qwen3-27B；且来源仅提供了 MMLU Pro 等通用基准的精度对比，未提供 HumanEval 数据集上的具体 Pass@1 数值，存在版本混淆及数据缺失风险。 | 来源 [2] 和 [3] 证实了 NVFP4 量化在 27B 模型上精度损失极小（MMLU Pro 差距 <0.5），逻辑上支持量化后性能保持，但缺乏 HumanEval 具体数值的直接证据，且模型版本号不完全匹配。

## Search Query

Qwen3-27B NVFP4 W4 HumanEval pass@1

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_01106/article/details/168111467&rut=361021651fef8df07d9011fed9d909294d8bbe7a46c63eb79ef4e0ec7cc39cb8', 'type': 'ddg', 'title': 'Qwen3.8-27B-NVFP4完整指南：4位NVFP4量化如何玩转27B多模态大模型-CSDN博客'}
- {'url': 'https://blog.csdn.net/chen695969/article/details/162604876&rut=83b2f645f8d3eb7bca0588168465104066fc61b7e0fdcd8c134eb2e096deb4e6', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 深度评测：英伟达官方量化，27B 长上下文本地部署新选择-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/162604876&rut=0da2072520e604542f799f79226bcef08e35f0d0efec6891856316c5de4d26f3', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 深度评测：英伟达官方量化，27B 长上下文本地部署新选择'}
