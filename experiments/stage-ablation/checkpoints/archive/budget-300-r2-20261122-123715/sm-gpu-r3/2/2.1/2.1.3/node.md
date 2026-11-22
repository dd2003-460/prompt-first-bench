# N55: Qwen3-27B 在 4-bit (W4A8/W4A16) 量化下，通用对话困惑度增加量 ΔPPL 预期在 0.5-1.5 之间，若 ΔPPL > 1.0 或

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

Qwen3-27B 在 4-bit (W4A8/W4A16) 量化下，通用对话困惑度增加量 ΔPPL 预期在 0.5-1.5 之间，若 ΔPPL > 1.0 或长尾任务（如复杂推理）准确率下降 > 10%，则 W4 精度不可接受，需回退至 INT8。

## Corrected Claim

Qwen3-27B 在 4-bit (W4A8/W4A16) 量化下，通用对话困惑度增加量 ΔPPL 通常较小，若 ΔPPL 显著增加（如 > 1.0）或长尾任务准确率大幅下降，则 W4 精度可能不可接受，需回退至 INT8。

## Evidence

[质询]该陈述包含具体的经验性阈值（ΔPPL 0.5-1.5, 准确率下降 >10%）和特定模型版本（Qwen3-27B），属于经验事实。参考来源仅证实了存在 Qwen3.8-27B 的 W4A16 量化版本，但未提供具体的困惑度增加量数据或准确率下降的具体数值，无法直接支持这些具体阈值的合理性或准确性。 | 来源 [1] 证实了 Qwen3.8-27B 存在 W4A16 量化版本，间接支持了量化场景的存在，但未提供具体的 ΔPPL 数值或准确率下降数据，属于间接支持且缺乏具体数值佐证。

## Search Query

Qwen3-27B 4-bit quantization perplexity degradation threshold

## Retrieval Sources

- {'url': 'https://huggingface.co/pearsonkyle/Qwen3.8-27B-GPTQ-W4A16&rut=4e11c424d0a8e15962d3b984a3a8f9fe4ee6d6a7f215acbbf072116bdee989df', 'type': 'ddg', 'title': 'pearsonkyle/Qwen3.8-27B-GPTQ-W4A16 · Hugging Face'}
