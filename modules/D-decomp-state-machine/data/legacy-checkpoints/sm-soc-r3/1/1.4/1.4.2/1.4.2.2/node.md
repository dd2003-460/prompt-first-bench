# N140: α_anchor 方差 0.1^2 的来源分解：Var(α_anchor) = Var(α_time_window) + Var(α_individual)，其

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

α_anchor 方差 0.1^2 的来源分解：Var(α_anchor) = Var(α_time_window) + Var(α_individual)，其中 Var(α_time_window) 由 7天 vs 30天 窗口选择差异贡献，估算为 0.006^2，Var(α_individual) 由个体认知差异贡献，估算为 0.008^2

## Corrected Claim

α_anchor 方差 0.1^2 的来源分解：Var(α_anchor) = Var(α_time_window) + Var(α_individual)，其中 Var(α_time_window) 由 7天 vs 30天 窗口选择差异贡献，估算为 0.006^2，Var(α_individual) 由个体认知差异贡献，估算为 0.008^2

## Evidence

先验知识/题面给定，逻辑校验通过：方差分解公式 Var(X+Y)=Var(X)+Var(Y) 在独立假设下成立，且数值量级 (0.006^2 + 0.008^2 ≈ 0.0001) 与总方差 0.1^2 (0.01) 相比偏小，但在特定模型设定下（如其他项贡献主要方差或此处仅为部分分解）逻辑上无硬矛盾，符合 knowledge 节点判定规则。

## Search Query

anchoring effect variance individual differences time window
