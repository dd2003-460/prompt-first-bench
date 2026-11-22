# N83: Qwen3-27B 在 FP8 精度下的 HumanEval 代码生成得分：约为 68-73%，相比 BF16 下降 2-4 个百分点（代码生成对精度敏感，FP

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

Qwen3-27B 在 FP8 精度下的 HumanEval 代码生成得分：约为 68-73%，相比 BF16 下降 2-4 个百分点（代码生成对精度敏感，FP8 可能引入更多逻辑错误）

## Corrected Claim

Qwen3-27B 在 FP8 精度下的 HumanEval 代码生成得分预计相比 BF16 会有所下降（约2-4个百分点），具体数值需查阅官方技术报告或基准测试数据。

## Evidence

[质询]参考来源[1]的模型名称为'Qwen3.8-27B'，与陈述中的'Qwen3-27B'存在版本/命名不一致，且摘要内容仅涉及MathVision评测提示词，未包含HumanEval代码生成得分的具体数值，无法直接支持该经验事实。 | 经验事实，逻辑自洽（FP8精度下降导致代码生成能力轻微受损符合直觉），但参考来源[1]主题不匹配且未提供HumanEval数据，缺乏直接来源支持。

## Search Query

Qwen3-27B FP8 HumanEval code generation score quantization

## Retrieval Sources

- {'url': 'https://huggingface.co/Qwen/Qwen3.8-27B-FP8&rut=14136281e1ef2fc006f2a2d3b080ee78368ef2e65dbc32e90d1e2479a0f7bd3d', 'type': 'ddg', 'title': 'Qwen/Qwen3.8-27B-FP8 · Hugging Face'}
