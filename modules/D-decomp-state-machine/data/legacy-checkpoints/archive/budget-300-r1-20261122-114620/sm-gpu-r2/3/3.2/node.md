# N19: FP8 精度质量损失：FP8 (E4M3/E5M2) 在 7B-70B 模型上 perplexity 增加 0.5-1.5%，在复杂推理任务（如 MMLU）上准

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

FP8 精度质量损失：FP8 (E4M3/E5M2) 在 7B-70B 模型上 perplexity 增加 0.5-1.5%，在复杂推理任务（如 MMLU）上准确率下降 1-2%，通常可接受

## Corrected Claim

FP8 (E4M3/E5M2) 在 7B-70B 模型上通常会导致轻微的 perplexity 增加和复杂推理任务准确率下降，具体数值因模型和任务而异，通常被认为在可接受范围内。

## Evidence

[质询]参考来源仅介绍了FP8的格式定义（E4M3/E5M2），未提供关于7B-70B模型上perplexity增加0.5-1.5%或MMLU准确率下降1-2%的具体实验数据，属于经验事实缺乏直接来源支持。 | 来源[1]确认了FP8格式定义，但未覆盖具体的精度损失数值；该陈述为经验事实，逻辑自洽但缺来源直接支持。

## Search Query

FP8 quantization LLM perplexity accuracy drop MMLU

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/574825662&rut=f191144fc4891f6c1f3bf6838e26898380539972ecea368c6b245ffd9df8d2f6', 'type': 'ddg', 'title': 'Fp8 量化-原理、实现与误差分析 - 知乎'}
