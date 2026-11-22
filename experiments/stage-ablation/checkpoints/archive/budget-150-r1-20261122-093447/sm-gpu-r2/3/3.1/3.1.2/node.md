# N78: Qwen3-27B 在 INT8 (SmoothQuant) 精度下的 GSM8K 基准测试准确率及相对于 BF16 基线的绝对下降值（ΔGSM8K）

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

Qwen3-27B 在 INT8 (SmoothQuant) 精度下的 GSM8K 基准测试准确率及相对于 BF16 基线的绝对下降值（ΔGSM8K）

## Corrected Claim

Qwen3-27B 在 INT8 (SmoothQuant) 精度下的 GSM8K 基准测试准确率及相对于 BF16 基线的绝对下降值（ΔGSM8K）具体数值未在提供的参考来源中明确给出，仅知该量化版本具有较低的KL散度（mean full-vocab KLD vs BF16 = 0.0110）。

## Evidence

[质询]参考来源[1]仅提供了模型量化后的KL散度（KLD）指标，未包含GSM8K基准测试的具体准确率数值或相对于BF16基线的绝对下降值（ΔGSM8K），无法直接支持该事实节点中的具体数值结论。 | 来源[1]主题相关（Qwen3-27B INT8量化），但仅报告了KLD指标，未提供GSM8K准确率及ΔGSM8K数值，属于间接支持/证据缺失，且该事实为经验数据，无法从第一性原理推导。

## Search Query

Qwen3-27B INT8 GSM8K accuracy benchmark

## Retrieval Sources

- {'url': 'https://huggingface.co/Freaksterz/Qwen3.8-27B-SmoothQuant-W8A8-INT8/blob/main/README.md&rut=c0b0d6810e321a8b26ef1af1f3cf04f7ac74da735e86800d3c61b84b842a73d9', 'type': 'ddg', 'title': 'Qwen3.8-27B-SmoothQuant-W8A8-INT8 - Hugging Face'}
