# N129: Qwen3-27B 在 NVFP4/W4 量化下于 GSM8K 数据集上的具体准确率数值 (Acc_W4_GSM8K)，用于量化 4-bit 量化在复杂推理任务

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

Qwen3-27B 在 NVFP4/W4 量化下于 GSM8K 数据集上的具体准确率数值 (Acc_W4_GSM8K)，用于量化 4-bit 量化在复杂推理任务上的退化。

## Corrected Claim

Qwen3.8-27B 在 NVFP4/W4 量化下于 GSM8K 数据集上的准确率为 97.27%。

## Evidence

[质询]来源[3]明确提及的模型名称为 'Qwen3.8-27B'，而事实节点声称的是 'Qwen3-27B'。虽然 'Qwen3.8' 可能是 'Qwen3' 系列的一个特定版本或笔误，但两者在命名上存在差异，且来源[1]和[2]也均使用 'Qwen3.8-27B'。若 'Qwen3-27B' 与 'Qwen3.8-27B' 并非同一模型或同一量化版本，则数值可能不适用。此外，GSM8K 97.27% 的准确率对于 4-bit 量化模型而言极高，通常接近全精度水平，需确认该数值是否确实对应 W4 量化后的结果，而非全精度基线或混合精度下的特定子集。 | 来源[3]直接提供了 'Qwen3.8-27B-NVFP4' 在 GSM8K 上的准确率为 97.27%，与事实节点中的数值一致，但模型名称存在 'Qwen3' 与 'Qwen3.8' 的细微差异，且来源均为博客文章，权威性略低于官方技术报告，故降级为 degraded。

## Search Query

Qwen3-27B NVFP4 W4 GSM8K accuracy

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_01106/article/details/168111467&rut=361021651fef8df07d9011fed9d909294d8bbe7a46c63eb79ef4e0ec7cc39cb8', 'type': 'ddg', 'title': 'Qwen3.8-27B-NVFP4完整指南：4位NVFP4量化如何玩转27B多模态大模型-CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00251/article/details/155252364&rut=9bbbcdd0f333ba596a05ec7574c1923e9f0911e63c9721d5071cfab3d5ce492c', 'type': 'ddg', 'title': '什么是Qwen3.8-27B-NVFP4？27B视觉语言模型与NVFP4量化的完整入门指南-CSDN博客'}
- {'url': 'https://blog.gitcode.com/1a111ab8e09a688e2827a5b1ce93ebf9.html&rut=f350f197a6dad2e443987549f557fd9f0b60674263afbc13263f23912f9ab6b8', 'type': 'ddg', 'title': 'Qwen3.8-27B-NVFP4基准测试全解析：量化后GSM8K 97.27%的准确率从何而来？'}
