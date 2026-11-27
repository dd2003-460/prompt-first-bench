# N246: Qwen3-27B 在 W4A16 GPTQ 量化下，MMLU 基准测试的准确率损失具体数值为 2.0% - 3.5% (绝对值)，通常高于 AWQ 方案 0.

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N85

## Claim

Qwen3-27B 在 W4A16 GPTQ 量化下，MMLU 基准测试的准确率损失具体数值为 2.0% - 3.5% (绝对值)，通常高于 AWQ 方案 0.5%-1.0%；若 GPTQ 损失显著高于 AWQ (差值 > 1.5%)，则优先推荐 AWQ 方案。

## Corrected Claim

Qwen3-27B 在 W4A16 量化下，GPTQ 的 MMLU 准确率损失通常略高于 AWQ 方案；若实测中 GPTQ 损失显著高于 AWQ，则优先推荐 AWQ 方案。

## Evidence

[质询]具体数值区间（2.0%-3.5% vs 0.5%-1.0%）及差值阈值（>1.5%）属于特定实验条件下的经验数据，不同数据集、量化实现版本及评测协议下波动较大，缺乏通用性，且当前无来源支持该精确数值。 | 经验事实，逻辑自洽（GPTQ通常精度损失略高于AWQ符合业界共识）但缺来源支持，且具体数值无法从第一性原理推出。

## Search Query

Qwen3-27B GPTQ W4A16 MMLU accuracy loss comparison AWQ
