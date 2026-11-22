# N84: AWQ 算法下 Qwen3-27B W4 量化后，WikiText-103 PPL 具体增量为 0.40±0.10，MMLU 准确率损失为 3.0%±1.0%，

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24

## Claim

AWQ 算法下 Qwen3-27B W4 量化后，WikiText-103 PPL 具体增量为 0.40±0.10，MMLU 准确率损失为 3.0%±1.0%，AWQ 通过激活感知量化在 W4 下保持相对 GPTQ 更低的 PPL 损失

## Corrected Claim

AWQ 算法下 Qwen3-27B W4 量化后，WikiText-103 PPL 和 MMLU 准确率会有所下降，AWQ 通过激活感知量化在 W4 下通常保持相对 GPTQ 更低的 PPL 损失。

## Evidence

[质询]具体数值（PPL增量0.40±0.10，MMLU损失3.0%±1.0%）属于特定实验条件下的经验数据，不同量化实现、校准数据集及评估协议可能导致结果显著差异，且缺乏来源支持无法确认该特定数值组合的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B AWQ W4 PPL MMLU accuracy loss
