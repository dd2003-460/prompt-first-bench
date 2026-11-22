# N289: Qwen3-27B 在 W4 (GPTQ/AWQ) 量化下的 MMLU 分数具体数值，以及相对于 BF16 基线的绝对下降值（百分点），用于验证 3-7% 损失

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N107

## Claim

Qwen3-27B 在 W4 (GPTQ/AWQ) 量化下的 MMLU 分数具体数值，以及相对于 BF16 基线的绝对下降值（百分点），用于验证 3-7% 损失区间并确定是否触发 <3% 容忍度排除条件。

## Corrected Claim

Qwen3-27B 在 W4 (GPTQ/AWQ) 量化下的 MMLU 分数通常会有所下降，具体数值需查阅官方技术报告或基准测试数据以确认是否落在 3-7% 损失区间或触发 <3% 容忍度排除条件。

## Evidence

[质询]具体数值（MMLU分数及绝对下降值）属于经验事实，且不同量化实现（GPTQ vs AWQ）、校准数据集及评测子集可能导致结果波动，缺乏具体来源支持无法确定精确数值是否严格落在3-7%区间或触发<3%条件。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B W4 GPTQ AWQ MMLU accuracy degradation
