# N21: 外部事实核查 Hook 的触发策略应基于置信度阈值：当模型自评估置信度 < τ 时调用检索工具，τ 的优化值需平衡‘误报率’（False Positive, F

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

外部事实核查 Hook 的触发策略应基于置信度阈值：当模型自评估置信度 < τ 时调用检索工具，τ 的优化值需平衡‘误报率’（False Positive, FP）与‘漏报率’（False Negative, FN），最小化总成本函数 C_total = C_API * FP_rate * Q_total + C_Human_Review * FN_rate * Q_total，其中 C_API 为单次检索调用成本（~$0.01-0.05），C_Human_Review 为单位人工复核时间成本（~$50/hr / 2min/task ≈ $1.67）。

## Corrected Claim

外部事实核查 Hook 的触发策略应基于置信度阈值：当模型自评估置信度 < τ 时调用检索工具，τ 的优化值需平衡‘误报率’（False Positive, FP）与‘漏报率’（False Negative, FN），最小化总成本函数 C_total = C_API * FP_rate * Q_total + C_Human_Review * FN_rate * Q_total，其中 C_API 为单次检索调用成本（~$0.01-0.05），C_Human_Review 为单位人工复核时间成本（~$50/hr / 2min/task ≈ $1.67）。

## Evidence

先验知识/题面给定，逻辑校验通过：成本函数构建符合经济学直觉，数值量级（API成本 vs 人工成本）合理，且作为knowledge节点无需外部来源支持。

## Search Query

confidence threshold retrieval augmented generation cost optimization
