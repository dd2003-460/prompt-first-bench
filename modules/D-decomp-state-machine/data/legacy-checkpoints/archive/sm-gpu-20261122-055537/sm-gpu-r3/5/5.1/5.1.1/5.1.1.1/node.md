# N262: Q_score 计算的分母基准 (Score_BF16) 量化锚点：Qwen3-27B 在 BF16 精度下的 MMLU 准确率为 [待核验: 需查阅 Qwen

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N80

## Claim

Q_score 计算的分母基准 (Score_BF16) 量化锚点：Qwen3-27B 在 BF16 精度下的 MMLU 准确率为 [待核验: 需查阅 Qwen3 官方技术报告，预期 >90%]，HumanEval Pass@1 准确率为 [待核验: 预期 >80%]。若无法获取官方数据，需自建基线：在 RTX 4090 上使用 BF16 权重（需 CPU Offload 或 2x4090）实测这两个基准，作为 Q_score 的归一化分母。

## Corrected Claim

Q_score 计算的分母基准 (Score_BF16) 量化锚点：Qwen3-27B 在 BF16 精度下的 MMLU 准确率预期较高（通常 >90%），HumanEval Pass@1 准确率预期较高（通常 >80%）。具体数值需查阅 Qwen3 官方技术报告或自建基线实测确认，作为 Q_score 的归一化分母。

## Evidence

[质询]该陈述包含具体的经验事实（Qwen3-27B在MMLU和HumanEval上的具体准确率数值），且明确标记为[待核验]。根据经验事实排除条款，此类硬件/模型性能指标无法从第一性原理推导，必须依赖外部来源支持。当前无可用来源，且预期值（>90%, >80%）虽符合大模型趋势但未经证实，存在具体数值偏差的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值）

## Search Query

Qwen3-27B BF16 MMLU HumanEval benchmark accuracy official
