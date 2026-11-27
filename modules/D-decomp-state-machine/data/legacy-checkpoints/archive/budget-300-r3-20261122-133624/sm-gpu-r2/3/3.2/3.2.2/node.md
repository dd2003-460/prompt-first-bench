# N82: GPTQ 算法下 Qwen3-27B INT8 量化后，WikiText-103 PPL 具体增量为 0.25±0.05，MMLU 准确率损失为 2.0%±0.

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N23

## Claim

GPTQ 算法下 Qwen3-27B INT8 量化后，WikiText-103 PPL 具体增量为 0.25±0.05，MMLU 准确率损失为 2.0%±0.5%，GPTQ 因离线量化特性在极端离群值处理上略逊于 SmoothQuant

## Corrected Claim

GPTQ 算法下 Qwen3-27B INT8 量化后，WikiText-103 PPL 和 MMLU 准确率会有轻微下降，GPTQ 因离线量化特性在极端离群值处理上略逊于 SmoothQuant

## Evidence

[质询]具体数值（PPL增量0.25±0.05，MMLU损失2.0%±0.5%）属于特定实验条件下的经验数据，不同量化配置（如group size、校准集大小）会导致结果显著波动，且缺乏来源支持该特定数值组合的普遍性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B GPTQ INT8 PPL MMLU accuracy loss
