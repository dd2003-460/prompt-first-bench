# N186: Qwen3-27B 在 INT8 量化下，HumanEval Pass@1 的下降幅度具体数值需检索代码生成专项评测数据，预期区间为 1.5%-3.0%，需对比

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N60

## Claim

Qwen3-27B 在 INT8 量化下，HumanEval Pass@1 的下降幅度具体数值需检索代码生成专项评测数据，预期区间为 1.5%-3.0%，需对比 BF16 基线（通常 ~60-70%）以计算绝对下降值，验证 N60 中 2.0%-4.0% 的估计是否包含长尾错误案例。

## Corrected Claim

Qwen3-27B 在 INT8 量化下，HumanEval Pass@1 的下降幅度需检索代码生成专项评测数据以获取具体数值，通常量化会导致一定程度的性能下降，需对比 BF16 基线以计算绝对下降值，并验证 N60 中 2.0%-4.0% 的估计是否包含长尾错误案例。

## Evidence

[质询]该陈述包含具体的经验性数值区间（1.5%-3.0%）和基线范围（60-70%），属于硬件/模型性能经验事实，无法从第一性原理推导，且检索无可用来源支持，存在数值不准确的风险。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据）

## Search Query

Qwen3-27B INT8 HumanEval Pass@1 performance degradation
