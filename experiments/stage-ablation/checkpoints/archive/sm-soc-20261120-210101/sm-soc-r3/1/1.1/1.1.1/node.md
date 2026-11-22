# N30: 共享随机源：偏好噪声的方差分解模型。定义总偏好方差 Var(P) = Var(λ_loss) + Var(α_anchor) + Var(I_asym)，其中各

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N6

## Claim

共享随机源：偏好噪声的方差分解模型。定义总偏好方差 Var(P) = Var(λ_loss) + Var(α_anchor) + Var(I_asym)，其中各分项独立同分布或存在协方差项 Cov(λ, α)。需量化各分项在二手交易场景下的相对贡献占比。

## Corrected Claim

在特定的偏好噪声方差分解模型中，总偏好方差可分解为损失厌恶、锚定效应及不对称性等因素的方差之和及协方差项；各分项在二手交易场景下的具体相对贡献占比需通过实证数据量化，而非由模型定义直接给出。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1定义基准源，节点2-4分别对应父节点中提到的三个独立方差分项（Var(λ_loss), Var(α_anchor), Var(I_asym)），节点5对应协方差项。结构上完全覆盖了父节点定义的方差分解公式 Var(P) = Var(λ) + Var(α) + Var(I) + 2Cov(λ, α) 的所有组成部分。各节点职责单一，无内容重复或矛盾。）

## Search Query

preference noise variance decomposition loss aversion anchoring effect empirical estimation
