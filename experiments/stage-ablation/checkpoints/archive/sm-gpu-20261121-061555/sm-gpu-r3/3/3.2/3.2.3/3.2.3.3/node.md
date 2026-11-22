# N241: SmoothQuant 对 Qwen3-27B 质量的影响量化：在 α=0.5 下，WikiText-2 PPL 增量通常为 0.05-0.15，MMLU 准确

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N81

## Claim

SmoothQuant 对 Qwen3-27B 质量的影响量化：在 α=0.5 下，WikiText-2 PPL 增量通常为 0.05-0.15，MMLU 准确率下降 < 0.5%；若 α 偏离 0.5 过多（如 α=0.8 偏向权重），激活值量化误差激增，PPL 增量可能超过 0.5，导致不可接受的质量损失。

## Corrected Claim

SmoothQuant 对 Qwen3-27B 质量的影响：在 α=0.5 下，量化误差通常较小，PPL 增量和 MMLU 准确率下降在可接受范围内；若 α 偏离 0.5 过多（如 α=0.8），激活值量化误差可能显著增加，导致 PPL 增量过大，造成不可接受的质量损失。

## Evidence

[质询]具体数值（PPL增量0.05-0.15、MMLU下降<0.5%、α=0.8时PPL>0.5）属于特定模型（Qwen3-27B）在特定量化配置下的经验测量结果，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持
