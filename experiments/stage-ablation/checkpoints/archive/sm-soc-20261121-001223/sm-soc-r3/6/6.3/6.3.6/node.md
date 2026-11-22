# N201: 透明度展示对 P_avg 估计精度的影响：引入透明度后，买家对 P_avg 的估计方差 Var(P_avg_est) 从 σ²_prior 降至 σ²_post

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72, N73, N74

## Claim

透明度展示对 P_avg 估计精度的影响：引入透明度后，买家对 P_avg 的估计方差 Var(P_avg_est) 从 σ²_prior 降至 σ²_posterior；若 Var 降低超过 50%，则 δ 的实际有效值会收窄（即买家更严格执行阈值），导致高挂价商品的咨询量下降幅度大于线性预测。

## Corrected Claim

透明度展示对 P_avg 估计精度的影响：引入透明度后，买家对 P_avg 的估计方差 Var(P_avg_est) 从 σ²_prior 降至 σ²_posterior；若 Var 降低超过 50%，则 δ 的实际有效值会收窄（即买家更严格执行阈值），导致高挂价商品的咨询量下降幅度大于线性预测。

## Evidence

先验知识/题面给定，逻辑校验通过：贝叶斯更新降低方差，信息优势增强导致策略执行更严格，非线性效应符合经济学直觉。
