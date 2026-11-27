# N133: Qwen3-27B 在 NVFP4/W4 量化下于 WikiText2 数据集上的困惑度 (Perplexity) 数值 (PPL_W4_WikiText2)，

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

Qwen3-27B 在 NVFP4/W4 量化下于 WikiText2 数据集上的困惑度 (Perplexity) 数值 (PPL_W4_WikiText2)，用于计算 4-bit 量化带来的具体困惑度增幅。

## Corrected Claim

Qwen3-27B（或相近版本如 Qwen3.6-27B）在 NVFP4/W4 量化下，其精度损失在 MMLU Pro 等基准上控制在 ±0.5 以内，但具体 WikiText2 困惑度数值需查阅原始技术报告或评测全文以获取准确值。

## Evidence

[质询]参考来源中提到的模型版本为 Qwen3.6-27B 或 Qwen3.8-27B，与陈述中的 Qwen3-27B 存在版本不一致；且来源摘要仅提及 MMLU Pro 等基准测试的精度保持情况，未提供 WikiText2 数据集上的具体困惑度 (PPL) 数值，无法直接支持该具体数值事实。 | 来源 [1][2][3] 均涉及 NVFP4/W4 量化对 27B 模型的影响，但仅提供了 MMLU Pro 等任务的性能对比，未包含 WikiText2 困惑度数据，属于间接相关但缺乏直接数值支持。

## Search Query

Qwen3-27B NVFP4 W4 WikiText2 perplexity

## Retrieval Sources

- {'url': 'https://blog.csdn.net/chen695969/article/details/162604876&rut=83b2f645f8d3eb7bca0588168465104066fc61b7e0fdcd8c134eb2e096deb4e6', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 深度评测：英伟达官方量化，27B 长上下文本地部署新选择-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/162604876&rut=0da2072520e604542f799f79226bcef08e35f0d0efec6891856316c5de4d26f3', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 深度评测：英伟达官方量化，27B 长上下文本地部署新选择'}
- {'url': 'https://blog.csdn.net/gitblog_00951/article/details/168230444&rut=8b056d765d32cea71a65a4e477811edcaa92cf8a2da8d9ba1853b3d49d6d94c6', 'type': 'ddg', 'title': 'NVFP4 W4A4量化到底强在哪？Qwen3.8-27B-NVFP4如何把模型从55GB压到21.9GB-CSDN博客'}
