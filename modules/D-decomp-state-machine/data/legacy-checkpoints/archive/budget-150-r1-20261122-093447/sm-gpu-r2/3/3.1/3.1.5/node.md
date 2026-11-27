# N81: Qwen3-27B 在 BF16 精度下的各基准测试（MMLU, GSM8K, HumanEval, MATH）基线准确率数值，作为量化损失计算的参照点

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

Qwen3-27B 在 BF16 精度下的各基准测试（MMLU, GSM8K, HumanEval, MATH）基线准确率数值，作为量化损失计算的参照点

## Corrected Claim

Qwen3-27B 在 BF16 精度下的各基准测试基线准确率数值未在当前参考来源中明确列出，仅知量化后与另一路径平均分差为0.70个百分点。

## Evidence

[质询]参考来源仅提供了量化后的平均分差（0.70个百分点），并未提供BF16精度下的具体基线准确率数值（如MMLU、GSM8K等单项分数），无法直接支持该事实节点中关于具体基线数值的陈述。 | 来源[1]提及了Qwen3.8-27B的量化对比，但仅给出平均分差，未提供BF16基线具体数值，属于间接相关但缺乏直接数据支持。

## Search Query

Qwen3-27B BF16 baseline MMLU GSM8K HumanEval MATH scores

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2073832437491287186&rut=b4516df8992fdf7a3c7e8f94308cbb87f96dc4ab542bf2ddc1a5f6aa5bec2829', 'type': 'ddg', 'title': 'qwen3.8-27b量化模型实测对比情况 - 知乎'}
