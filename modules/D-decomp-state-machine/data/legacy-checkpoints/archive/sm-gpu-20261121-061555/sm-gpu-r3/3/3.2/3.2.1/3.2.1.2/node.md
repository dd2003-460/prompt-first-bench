# N234: GPTQ 校准数据集大小对 PPL 稳定性的影响阈值：当 N_samples < 128 时，Qwen3-27B 的 WikiText-2 PPL 方差 (St

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N79

## Claim

GPTQ 校准数据集大小对 PPL 稳定性的影响阈值：当 N_samples < 128 时，Qwen3-27B 的 WikiText-2 PPL 方差 (Std Dev) 通常 > 0.15，导致量化质量不可复现；当 N_samples >= 256 时，PPL 方差降至 < 0.05，达到工程可用精度。

## Corrected Claim

GPTQ 校准数据集大小显著影响 PPL 稳定性：当校准样本数过少（如低于 128）时，量化后的 PPL 方差较大，导致结果不可复现；当样本数足够大（如 256 及以上）时，PPL 方差显著降低，达到工程可用的稳定精度。

## Evidence

[质询]该陈述包含具体的经验性数值阈值（N_samples < 128 时 Std Dev > 0.15，N_samples >= 256 时 Std Dev < 0.05）及特定模型（Qwen3-27B）的量化行为，属于无法从第一性原理推导的经验事实。虽然 GPTQ 校准数据量对稳定性有影响是已知结论，但具体的方差阈值和样本数界限缺乏通用理论支持，且不同模型/数据集下数值可能显著不同，存在过度具体化导致失真的风险。 | source=knowledge，逻辑上校准数据量增加通常降低方差符合统计直觉，但具体数值阈值（0.15/0.05）和样本界限（128/256）属于特定实验经验数据，非普适物理/数学定律，且无外部来源验证具体数值，故降级为定性表述。
