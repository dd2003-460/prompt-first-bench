# N633: Qwen3-27B 在 BF16 精度下的 MMLU 总得分基线值 (MMLU_BF16) 需从 Qwen3 官方发布数据获取，参考 27B 参数量级模型在 M

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N262

## Claim

Qwen3-27B 在 BF16 精度下的 MMLU 总得分基线值 (MMLU_BF16) 需从 Qwen3 官方发布数据获取，参考 27B 参数量级模型在 MMLU 上的典型得分区间 (80-85%)，具体数值需精确到小数点后一位以支持 <2% 的阈值判断。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的 MMLU 总得分基线值需从 Qwen3 官方发布数据获取，具体数值需精确到小数点后一位以支持 <2% 的阈值判断。

## Evidence

[质询]该陈述包含具体的经验性数值区间（80-85%）和特定模型（Qwen3-27B）的性能指标，属于经验事实，无法从第一性原理推导，且缺乏来源支持以确认该区间是否准确覆盖Qwen3-27B的实际表现。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B MMLU score BF16 official benchmark
