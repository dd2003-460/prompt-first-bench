# N166: Qwen3-27B 使用 SmoothQuant 算法进行 INT8 量化后的 HumanEval (Pass@1) 分数需检索相关量化基准测试数据，特别关注 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N49

## Claim

Qwen3-27B 使用 SmoothQuant 算法进行 INT8 量化后的 HumanEval (Pass@1) 分数需检索相关量化基准测试数据，特别关注 SmoothQuant 对激活值分布平滑处理对代码生成任务的影响，以验证 Δ=-1.5% 的估计值，并对比 GPTQ 方案以确定哪种量化算法在代码任务上损失更小。

## Corrected Claim

Qwen3-27B 使用 SmoothQuant 算法进行 INT8 量化后的 HumanEval (Pass@1) 分数需检索相关量化基准测试数据，特别关注 SmoothQuant 对激活值分布平滑处理对代码生成任务的影响，以验证量化损失的具体数值，并对比 GPTQ 方案以确定哪种量化算法在代码任务上损失更小。

## Evidence

[质询]该陈述包含具体的经验数值（Δ=-1.5%）和特定模型（Qwen3-27B）的量化基准测试结果，属于经验事实，无法从第一性原理推导，且当前无可用来源支持该具体数值。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

Qwen3-27B SmoothQuant INT8 HumanEval Pass@1 score
