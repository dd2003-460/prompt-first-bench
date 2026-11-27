# N55: GPTQ 算法在 8-bit 量化 Qwen3-27B 时，相对于 BF16 基线的困惑度（Perplexity）增加幅度通常在 0.5% - 1.5% 区间，

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N13, N14, N15

## Claim

GPTQ 算法在 8-bit 量化 Qwen3-27B 时，相对于 BF16 基线的困惑度（Perplexity）增加幅度通常在 0.5% - 1.5% 区间，具体数值取决于校准数据集大小（通常 128-512 样本）和量化组大小（group_size=128 优于 64） [待核验：需引用 HuggingFace 或 Qwen 官方量化评测报告]

## Corrected Claim

GPTQ 算法在 8-bit 量化 Qwen3-27B 时，相对于 BF16 基线的困惑度（Perplexity）通常会有轻微增加，具体数值取决于校准数据集大小和量化组大小，但缺乏官方或权威来源提供的具体百分比区间数据。

## Evidence

[质询]参考来源[1]和[2]均未提供具体的困惑度（Perplexity）数值或增加幅度百分比，无法直接验证0.5%-1.5%这一具体经验数值区间；且来源[2]讨论的是INT4量化，与题目中的INT8量化场景不完全匹配，属于间接相关。 | 逻辑上8-bit量化对大模型困惑度影响较小，0.5%-1.5%的量级符合一般经验直觉，但参考来源[1][2]仅确认了模型和量化方法的存在，未提供具体的PPL评测数据支持该具体数值区间，属于经验事实且缺乏直接来源支持。

## Search Query

Qwen3-27B GPTQ INT8 quantization perplexity increase benchmark vs BF16

## Retrieval Sources

- {'url': 'https://huggingface.co/Chungulus/Qwen3.8-27B-GPTQ-INT8&rut=e999b505768c7a72b19163f3a83cc33eb907967f811e79e7b1f4b12b6bd3fd9f', 'type': 'ddg', 'title': 'Chungulus/Qwen3.8-27B-GPTQ-INT8 · Hugging Face'}
- {'url': 'https://github.com/mbgulden/Qwen3.8-27B-INT4-W4A16-MTP&rut=44815c71dd4b53e910a48454a0cbccce567aa56d77aac1805c6c7fe9f6db8148', 'type': 'ddg', 'title': 'Qwen3.8-27B-W4A16: Production INT4 Quantization Pipeline'}
