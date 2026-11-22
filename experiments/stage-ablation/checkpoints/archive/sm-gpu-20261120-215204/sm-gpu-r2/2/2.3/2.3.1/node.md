# N73: GPTQ-Int8 量化下 Qwen3-27B 的 MMLU 基准测试分数相对于 BF16 基线（约 85-90 分）的绝对下降幅度，需检索 HuggingFa

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

GPTQ-Int8 量化下 Qwen3-27B 的 MMLU 基准测试分数相对于 BF16 基线（约 85-90 分）的绝对下降幅度，需检索 HuggingFace Qwen3 量化模型卡片或相关论文获取具体数值（预期 0.5-2 分）。

## Corrected Claim

GPTQ-Int8 量化下 Qwen3-27B 的 MMLU 基准测试分数相对于 BF16 基线的绝对下降幅度预期在 0.5-2 分之间，现有间接证据显示不同量化路径间差异约为 0.7 分，具体 GPTQ-Int8 数值需进一步检索确认。

## Evidence

[质询]来源[1]提及的是'Qwen3.8-27B'且未明确指定量化方法为GPTQ-Int8，也未明确基准测试为MMLU（仅提及550题基准），存在模型版本、量化算法及评测集口径混淆的风险，无法直接证实GPTQ-Int8在MMLU上的具体下降幅度。 | 来源[1]提供了同一模型不同量化路径下0.70分的差异数据，间接支持了量化损失较小的逻辑预期，但未直接覆盖GPTQ-Int8在MMLU上的具体数值，属于间接支持。

## Search Query

Qwen3-27B GPTQ Int8 MMLU benchmark score degradation

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2073832437491287186&rut=fbdbf615f6f6ac9c426c2482560430165e3b403def59815183b01cb465fb5b63', 'type': 'ddg', 'title': 'qwen3.8-27b量化模型实测对比情况 - 知乎'}
