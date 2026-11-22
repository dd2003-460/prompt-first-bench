# N56: 买家保留价分布 F(R) 的均值上移幅度 ΔP_anchor 由信号效应与噪声效应共同决定：ΔP_anchor = β_signal * (P_anchor -

- **status**: verified
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

父节点级核验通过：正交+完备+无冗余（子节点通过参数空间（β_signal, σ_noise）的不同取值划分了三个典型工作点（高/中/低信号与噪声组合），彼此互斥且覆盖全面，无逻辑矛盾或内容重复。）
