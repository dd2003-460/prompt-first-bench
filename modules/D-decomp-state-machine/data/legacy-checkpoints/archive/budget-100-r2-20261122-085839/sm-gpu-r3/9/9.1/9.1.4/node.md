# N290: 量化方法对 MMLU 分数影响的敏感性参数：在相同位宽（如 W4）下，GPTQ 与 AWQ 两种主流量化算法导致的 MMLU 分数差异范围（例如 ±1-2 个百

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N107

## Claim

量化方法对 MMLU 分数影响的敏感性参数：在相同位宽（如 W4）下，GPTQ 与 AWQ 两种主流量化算法导致的 MMLU 分数差异范围（例如 ±1-2 个百分点），以确定'质量损失'的最小可接受量化方案。

## Corrected Claim

在相同位宽（如 W4）下，GPTQ 与 AWQ 两种主流量化算法导致的 MMLU 分数存在差异，具体幅度取决于模型与任务，通常较小但非固定值。

## Evidence

[质询]该陈述包含具体的经验数值范围（±1-2 个百分点），属于经验事实而非第一性原理可推导内容。不同模型架构、数据集子集及量化实现细节可能导致差异显著偏离此范围，且缺乏来源支持该特定数值区间。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

GPTQ vs AWQ quantization accuracy difference LLM MMLU
