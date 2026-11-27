# N80: Qwen3-27B INT8 量化困惑度 (Perplexity) 实测数据：在 WikiText-2 数据集上，BF16 PPL ≈ 5.2 [待核验]，IN

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

Qwen3-27B INT8 量化困惑度 (Perplexity) 实测数据：在 WikiText-2 数据集上，BF16 PPL ≈ 5.2 [待核验]，INT8 PPL ≈ 5.5-5.8 (增加 5-10%)。MMLU 分数：BF16 ≈ 75% [待核验]，INT8 ≈ 73-74% (下降 1-2%)。质量损失在可接受范围内，但需针对特定任务 (如代码生成) 进行额外验证。

## Corrected Claim

Qwen3-27B（若存在该特定版本）INT8量化通常会导致困惑度轻微上升（约5-10%）和MMLU分数轻微下降（约1-2%），具体数值需以官方或权威第三方评测为准，当前参考来源未提供具体实测数据。

## Evidence

[质询]参考来源[1]标题及内容提及的是'Qwen3.8-27B'（疑似笔误或虚构版本，通常Qwen3系列为235B/32B/14B/8B/4B/1.5B/0.6B，且无27B标准发布，即便存在，来源也未提供INT8量化后的具体PPL和MMLU数值），无法直接支持具体的量化损失数据（PPL 5.2->5.5-5.8, MMLU 75%->73-74%）。此外，'Qwen3-27B'这一型号本身在主流公开资料中并不常见（Qwen2.5有32B，Qwen3有32B/14B等，27B可能是特定裁剪版或笔误），导致事实基础存疑。 | 来源[1]主题相关但仅提及模型名称，未提供量化困惑度或MMLU的具体实测数据，属于间接/无关支持；该事实为经验性硬件/模型性能数据，逻辑上INT8量化导致轻微性能下降符合直觉，但缺乏直接来源支持具体数值，故降级。

## Search Query

Qwen3-27B INT8 perplexity MMLU benchmark

## Retrieval Sources

- {'url': 'https://www.sohu.com/a/1069709228_122066679&rut=9ad67d086bcf92a5e7ea6db5b06e882ce477a10d51c7ed4d0b2d60c0bac35872', 'type': 'ddg', 'title': '本地AI革命来了!Perplexity发布Qwen3.8-27B智能体，隐私+性能双爆表'}
