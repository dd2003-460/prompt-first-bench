# N13: INT8/W8A8精度下的质量损失评估：基于MMLU/GPQA基准测试，INT8量化相比BF16的准确率下降通常在1.0-2.5%范围内 [待核验: 需查找Qw

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N2

## Claim

INT8/W8A8精度下的质量损失评估：基于MMLU/GPQA基准测试，INT8量化相比BF16的准确率下降通常在1.0-2.5%范围内 [待核验: 需查找Qwen3-27B在INT8下的具体基准测试数据]

## Corrected Claim

INT8/W8A8精度下的质量损失评估：基于MMLU/GPQA基准测试，INT8量化相比BF16的准确率损失取决于量化策略，通常在较小范围内（如<2.5%），部分场景下可几乎无损失。

## Evidence

[质询]陈述声称INT8量化相比BF16准确率下降通常在1.0-2.5%范围内，但参考来源[1]明确指出'W8A8量化不必然掉精度'，且来源[2]显示在特定任务中可实现'几乎零掉点'（99.93%恢复率），这与'通常下降1.0-2.5%'的定量断言存在潜在矛盾或至少表明该范围并非普遍适用的'通常'情况，且缺乏针对Qwen3-27B在MMLU/GPQA上具体下降幅度的直接数据支持。 | 来源[1]和[2]表明W8A8量化精度损失取决于策略且可能极小（接近零），未直接支持'通常下降1.0-2.5%'这一具体数值范围，属于经验事实且缺乏直接来源支持，故降级。

## Search Query

Qwen3-27B INT8 W8A8 quantization MMLU GPQA benchmark accuracy drop

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00523/article/details/167275752&rut=faf4e5087a4cdf10f5bea22d391bac7b959c0d21d74af81cd72fa7aacae20444', 'type': 'ddg', 'title': '量化会掉精度吗？Qwen3.8-27B-w8a8的GPQA精度评估实战指南'}
- {'url': 'https://blog.csdn.net/gitblog_01133/article/details/163955374&rut=3415c6df8101fa83e12a72499c191c63e363e8448ea6ea2e907009896ec7ceb1', 'type': 'ddg', 'title': '7大视觉任务几乎零掉点：Qwen2.5-VL-7B-Instruct-quantized.w8a8精度评估全解析（MMM'}
- {'url': 'https://developers.redhat.com/articles/2026/09/07/understanding-w8a8-int8-llm-quantization&rut=75894f422816c5bbbeb1d4cb61de7d20b7587ad5ce4c76d9aedaade18240b1f7', 'type': 'ddg', 'title': 'Understanding W8A8 INT8 LLM quantization: Half the size, better ...'}
