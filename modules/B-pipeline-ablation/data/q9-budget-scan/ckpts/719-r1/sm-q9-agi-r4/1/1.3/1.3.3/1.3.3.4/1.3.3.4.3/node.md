# N420: 精度损失量化基准：对于 27B 级别模型，INT4 AWQ/GPTQ 在 WikiText2 上的 Perplexity (PPL) 增加通常为 0.1-0.5

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N141

## Claim

精度损失量化基准：对于 27B 级别模型，INT4 AWQ/GPTQ 在 WikiText2 上的 Perplexity (PPL) 增加通常为 0.1-0.5 相比 FP16。NVFP4 (若存在) 理论上精度更高，但需验证其在 V100 上的实际 PPL 增量。若 NVFP4 PPL 增量为 0.05，AWQ 为 0.3，则 NVFP4 精度略优，但需权衡速度。

## Corrected Claim

对于 27B 级别模型，INT4 AWQ/GPTQ 在 WikiText2 上的 Perplexity (PPL) 增加通常较小（具体数值需实测验证）。NVFP4 理论上精度更高，但需验证其在 V100 上的实际 PPL 增量及速度权衡。

## Evidence

[质询]该陈述包含具体的经验数值（INT4 AWQ/GPTQ 在 27B 模型上的 PPL 增量 0.1-0.5），属于经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

AWQ GPTQ perplexity degradation 27b model wiki text2 benchmark
