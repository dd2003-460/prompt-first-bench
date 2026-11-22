# N45: Qwen3-27B在FP8精度下的质量损失量化指标：在MMLU、GSM8K、HumanEval等基准测试中，FP8相比BF16的准确率下降百分比（通常<0.5%

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

Qwen3-27B在FP8精度下的质量损失量化指标：在MMLU、GSM8K、HumanEval等基准测试中，FP8相比BF16的准确率下降百分比（通常<0.5%，但需具体数值）。

## Corrected Claim

Qwen3-27B在FP8精度下的质量损失通常较小，具体在MMLU、GSM8K、HumanEval等基准测试中相比BF16的准确率下降百分比需参考具体实测数据（来源[1]提供了测试方法但未给出具体数值）。

## Evidence

[质询]参考来源[1]仅提供了测试方法论（判分方式、调用参数），并未包含具体的准确率下降数值或百分比，无法直接支持'通常<0.5%'这一具体量化结论。 | 来源[1]与主题相关（Qwen3-27B量化实测），但仅描述测试方法，未提供具体数值支持；FP8量化损失通常较小符合技术直觉，但具体数值缺乏直接证据。

## Search Query

Qwen3-27B FP8 vs BF16 accuracy benchmark MMLU GSM8K

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2073832437491287186&rut=fbdbf615f6f6ac9c426c2482560430165e3b403def59815183b01cb465fb5b63', 'type': 'ddg', 'title': 'qwen3.8-27b量化模型实测对比情况 - 知乎'}
