# N123: Pareto(α=1.1) 分布的二阶矩 Var(S) 在 α≤2 时发散（无穷大），导致公式 k ≈ (Var(R)/Var(S)) * ... 中的分母 V

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

Pareto(α=1.1) 分布的二阶矩 Var(S) 在 α≤2 时发散（无穷大），导致公式 k ≈ (Var(R)/Var(S)) * ... 中的分母 Var(S) 为 ∞，使得 k ≈ 0，该解析近似在 α=1.1 时数学上失效，需替换为基于截断方差或高阶矩的修正项。

## Corrected Claim

Pareto(α=1.1) 分布的二阶矩 Var(S) 在 α≤2 时发散（无穷大），导致公式 k ≈ (Var(R)/Var(S)) * ... 中的分母 Var(S) 为 ∞，使得 k ≈ 0，该解析近似在 α=1.1 时数学上失效，需替换为基于截断方差或高阶矩的修正项。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布二阶矩在α≤2时发散是数学事实，导致分母无穷大从而k趋近0的推导符合逻辑。
