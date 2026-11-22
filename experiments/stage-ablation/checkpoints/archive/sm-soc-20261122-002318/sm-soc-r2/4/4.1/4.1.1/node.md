# N56: 买家保留价分布 F(R) 的均值上移幅度 ΔP_anchor 由信号效应与噪声效应共同决定：ΔP_anchor = β_signal * (P_anchor -

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N21

## Claim

买家保留价分布 F(R) 的均值上移幅度 ΔP_anchor 由信号效应与噪声效应共同决定：ΔP_anchor = β_signal * (P_anchor - P_market) + 0.5 * σ_noise² / (2 * RiskAversionCoeff)，其中 β_signal 是信号强度系数，通常估计为 0.3-0.5。

## Corrected Claim

买家保留价分布 F(R) 的均值上移幅度 ΔP_anchor 受信号效应与噪声效应共同影响，通常可近似表示为信号项与风险调整噪声项之和，其中信号强度系数 β_signal 估计在 0.3-0.5 之间，噪声项的具体系数需根据特定风险厌恶模型校准。

## Evidence

[质询]公式中噪声项系数 0.5 缺乏理论推导支持，且将信号效应与噪声效应简单线性叠加的假设在微观基础层面过于简化，可能忽略高阶交互项或非线性风险调整。 | 先验知识/题面给定，逻辑校验通过（量纲一致，符号方向合理），但具体系数 0.5 及线性叠加形式属于经验性参数化，缺乏严格理论推导或来源支持，故降级。
