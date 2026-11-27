# N310: 扰动幅度的量化定义：外部扰动 ΔP_disturb = 0.1 * P_market（即 10% 市场均价波动），需计算系统恢复至原均衡点 P* 的时间 T_r

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99

## Claim

扰动幅度的量化定义：外部扰动 ΔP_disturb = 0.1 * P_market（即 10% 市场均价波动），需计算系统恢复至原均衡点 P* 的时间 T_recover = -τ * ln(0.1) ≈ 2.3 * τ。

## Corrected Claim

扰动幅度的量化定义：外部扰动 ΔP_disturb = 0.1 * P_market（即 10% 市场均价波动），需计算系统恢复至原均衡点 P* 的时间 T_recover = -τ * ln(0.1) ≈ 2.3 * τ。

## Evidence

先验知识/题面给定，逻辑校验通过：一阶线性系统恢复至90%平衡点的时间常数计算符合物理直觉（T = -τ ln(0.1) ≈ 2.3τ）
