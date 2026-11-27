# N637: Qwen3-27B 在 INT4 (AWQ) 量化下的 HumanEval Pass@1 实测值 (HE_INT4_AWQ) 需检索具体模型卡或第三方评测；若缺

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N263

## Claim

Qwen3-27B 在 INT4 (AWQ) 量化下的 HumanEval Pass@1 实测值 (HE_INT4_AWQ) 需检索具体模型卡或第三方评测；若缺失，基于 AWQ 量化对代码生成任务的典型影响系数估算：HE_INT4 ≈ HE_BF16 * (1 - 0.08)，即假设 4-bit 量化导致 Pass@1 下降约 8% [待核验]。

## Corrected Claim

Qwen3-27B 在 INT4 (AWQ) 量化下的 HumanEval Pass@1 实测值需检索具体模型卡或第三方评测；若缺失，可参考 AWQ 量化对代码生成任务通常导致性能轻微下降的经验规律进行定性估算，但具体下降幅度（如8%）因模型和校准策略而异，不应视为固定常数。

## Evidence

[质询]该陈述包含一个具体的经验性量化系数（8%），声称这是AWQ量化对代码生成任务Pass@1的典型影响。然而，量化对模型性能的影响高度依赖于模型架构、训练数据分布、量化算法细节（如是否使用校准数据、校准集大小）以及具体任务难度。将复杂的量化误差简化为固定的线性衰减系数（1-0.08）缺乏普遍适用的理论依据，且不同模型（如Qwen3-27B）的具体表现可能显著偏离此平均值，存在以偏概全的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该系数为经验估算值，无法从第一性原理严格推导，符合degraded判定条件）

## Search Query

Qwen3-27B INT4 AWQ HumanEval Pass@1 score
