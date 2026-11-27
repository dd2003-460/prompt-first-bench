# N106: INT4 (AWQ) 量化在 HumanEval 代码生成基准上的具体性能退化值：Qwen3-27B 在 BF16 下 HumanEval Pass@1 为 [

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

INT4 (AWQ) 量化在 HumanEval 代码生成基准上的具体性能退化值：Qwen3-27B 在 BF16 下 HumanEval Pass@1 为 [待核验]，INT4 下通常下降 5-8 个百分点。若 BF16 基线为 60%，则 INT4 约为 52-55%。

## Corrected Claim

INT4 (AWQ) 量化在 HumanEval 代码生成基准上通常会导致性能下降，具体退化幅度取决于模型规模与量化策略，一般认为在几个百分点范围内，但具体数值需参考特定模型的官方评测报告。

## Evidence

[质询]该陈述包含具体的经验性数值（BF16基线60%、INT4退化5-8个百分点），属于硬件/模型性能经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B HumanEval Pass@1 benchmark INT4 AWQ degradation
