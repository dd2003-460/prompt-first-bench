# N12: 量化BF16精度作为基准的质量保持率：Qwen3-27B在BF16下的Perplexity (PPL) 与MMLU/CMMLU基准分数，作为后续量化精度质量损失

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

量化BF16精度作为基准的质量保持率：Qwen3-27B在BF16下的Perplexity (PPL) 与MMLU/CMMLU基准分数，作为后续量化精度质量损失的参考基线（PPL≈3.2, MMLU≈85%）[待核验：具体数值需查证Qwen3技术报告]

## Corrected Claim

Qwen3-27B在BF16精度下具有最高的基准性能（如PPL和MMLU分数），具体数值需查阅官方技术报告以确认，通常作为量化精度损失的参考基线。

## Evidence

[质询]具体数值（PPL≈3.2, MMLU≈85%）缺乏直接来源支持，且参考来源主要讨论量化对比而非BF16基线的绝对数值，存在数值不准确或版本混淆的风险。 | 经验事实，逻辑自洽但缺来源支持；来源[1][2][3]仅提及BF16作为高精度基准，未提供具体的PPL和MMLU数值。

## Search Query

Qwen3-27B BF16 perplexity MMLU benchmark baseline accuracy

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00208/article/details/168127608&rut=da29108c3e0a19bc98cafff67766b941d73b95a4fa61f352128c66116f0076d3', 'type': 'ddg', 'title': '为什么4bit量化模型还保留BF16输出层？揭秘Qwen3.8-27B-NVFP4-BF16-LMHead的精度取舍'}
- {'url': 'https://blog.csdn.net/gitblog_00951/article/details/168656480&rut=a2beb0077c1730ce5004cbe06e2ac5a8a06e04c004470b17dc4b33a62419b454', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 vs NVIDIA NVFP4 vs FP8 vs BF16：精度基准全对比，4-bit量化真的掉分吗'}
- {'url': 'https://aishare.jizhiku.net/archives/52380&rut=9a7a27555c300b3f7308bf93d4ca1c6bb1711e5779280e612774e669596a5a71', 'type': 'ddg', 'title': 'Qwen3.8-27B 实测：BF16/FP8/NVFP4 精度对比与部署优化指南 - AI技能智慧站'}
