# N107: τ_signal 的具体数值需通过'买家点击率拐点'反推：在 D ∈ [-10%, 30%] 区间内，以 1% 为步长扫描 D，找到 CTR(D) 曲线斜率由负

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27, N28, N29

## Claim

τ_signal 的具体数值需通过'买家点击率拐点'反推：在 D ∈ [-10%, 30%] 区间内，以 1% 为步长扫描 D，找到 CTR(D) 曲线斜率由负转正的临界点 D*，该点即为 τ_signal 的经验估计值。若 CTR 在 D=15% 处出现局部峰值，则 τ_signal ≈ 15%。

## Corrected Claim

τ_signal 的具体数值需通过'买家点击率拐点'反推：在 D ∈ [-10%, 30%] 区间内，以 1% 为步长扫描 D，找到 CTR(D) 曲线斜率由负转正的临界点 D*，该点即为 τ_signal 的经验估计值。若 CTR 在 D=15% 处出现局部峰值，则 τ_signal ≈ 15%。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述定义了一种基于CTR曲线斜率变化（拐点/峰值）来反推信号阈值τ_signal的经验方法，逻辑自洽且符合数据驱动建模的常规思路，无内部矛盾。

## Search Query

click through rate inflection point price deviation threshold
