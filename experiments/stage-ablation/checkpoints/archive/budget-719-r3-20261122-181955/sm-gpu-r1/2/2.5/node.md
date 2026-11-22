# N18: 精度对模型质量损失的影响：引用Qwen3官方技术报告或第三方评测，量化BF16 vs FP8 vs INT4在MMLU/HumanEval等基准上的准确率下降百

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

精度对模型质量损失的影响：引用Qwen3官方技术报告或第三方评测，量化BF16 vs FP8 vs INT4在MMLU/HumanEval等基准上的准确率下降百分比（%），确定可接受阈值（如<2%）。

## Corrected Claim

根据第三方评测（如CSDN博客），Qwen3系列模型在FP8量化下相比BF16约有2-3%的精度损失，但缺乏INT4量化及特定基准（MMLU/HumanEval）的官方量化数据，无法确定统一的<2%可接受阈值。

## Evidence

[质询]来源[1]仅提供了FP8相对于BF16的2-3%精度损失，未提供INT4的具体数据；且该数据来自CSDN博客而非Qwen3官方技术报告，缺乏对MMLU/HumanEval等特定基准的明确量化，无法直接支撑‘<2%’这一具体阈值的普适性结论。 | 来源[1]间接支持FP8精度损失在2-3%范围，但未覆盖INT4及特定基准测试，且非官方来源，故降级为定性表述。

## Search Query

Qwen3-27B quantization quality loss BF16 FP8 INT4 benchmark MMLU accuracy drop

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00279/article/details/151738226&rut=ecbe72f7e398d75c496c7bb4e4d133970162e734fca4c1b071ad025baefcd87f', 'type': 'ddg', 'title': 'Qwen3-30B-A3B量化精度对比：FP16/BF16/FP8推理性能损耗分析-CSDN博客'}
- {'url': 'https://terrencemiao.github.io/blog/2026/04/26/Qwen-3-6-27B%EF%BC%8C%E5%A4%9A%E7%A7%8D%E4%BC%98%E5%8C%96%E6%96%B9%E5%BC%8F%EF%BC%8C%E4%BB%8E-20t-s-%E9%A3%99%E5%88%B0-184t-s/&rut=f8ebaea406070c5caf247c7d86ed1a1b2306f936250cd587e0a14eb538ee0d6a', 'type': 'ddg', 'title': 'Qwen 3.6 27B，多种优化方式，从 20 t/s 飙到 184 t/s'}
- {'url': 'https://blog.csdn.net/weixin_42511373/article/details/156501511&rut=91333773b836e24d0b3425d9d5b7746eeab97e3c2fe9139ea2a369ccd499d259', 'type': 'ddg', 'title': 'Qwen3-4B模型精度损失？fp16与量化版性能对比评测-CSDN博客'}
