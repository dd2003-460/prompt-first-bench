# N226: GPTQ 相比 AWQ 在数学推理任务上的额外劣势量化：GPTQ 基于二阶信息优化，但在数学推理中数值精度敏感层 (如 Linear 投影层) 的量化误差比 A

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N72

## Claim

GPTQ 相比 AWQ 在数学推理任务上的额外劣势量化：GPTQ 基于二阶信息优化，但在数学推理中数值精度敏感层 (如 Linear 投影层) 的量化误差比 AWQ 高约 15-20% [待核验]，导致 MATH 基准上 GPTQ 比 AWQ 多损失 1-2 个百分点准确率，需通过对比两者在 MATH 子集 (如代数学、几何学) 上的分项错误率验证。

## Corrected Claim

GPTQ 基于二阶信息优化，但在数学推理中数值精度敏感层的量化误差可能高于 AWQ，导致 MATH 基准上 GPTQ 比 AWQ 多损失一定准确率，需通过对比两者在 MATH 子集上的分项错误率验证。

## Evidence

[质询]该陈述包含具体的经验性数值（量化误差高15-20%、准确率损失1-2个百分点），这些数值并非第一性原理可推导，且缺乏来源支持，属于未经证实的具体量化断言。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

GPTQ vs AWQ quantization error mathematical reasoning benchmark
