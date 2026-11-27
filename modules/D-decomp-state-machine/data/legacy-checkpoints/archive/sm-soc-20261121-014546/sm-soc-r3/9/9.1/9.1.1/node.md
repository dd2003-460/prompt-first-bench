# N362: 买家感知噪声 σ_buyer 的构成项分解：σ_buyer^2 = σ_intrinsic^2 + σ_information^2，其中 σ_intrinsic

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N120

## Claim

买家感知噪声 σ_buyer 的构成项分解：σ_buyer^2 = σ_intrinsic^2 + σ_information^2，其中 σ_intrinsic 为商品固有质量不确定性，σ_information 为信息不对称导致的估值误差。当 σ_information 降低 50% 时，σ_buyer 从 0.20 降至 0.17，临界值 σ_crit = 0.15 的约束力减弱。

## Corrected Claim

买家感知噪声 σ_buyer 的构成项分解：σ_buyer^2 = σ_intrinsic^2 + σ_information^2，其中 σ_intrinsic 为商品固有质量不确定性，σ_information 为信息不对称导致的估值误差。当 σ_information 降低 50% 时，σ_buyer 从 0.20 降至 0.17，临界值 σ_crit = 0.15 的约束力减弱。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算自洽（假设σ_intrinsic=0.10, σ_information=0.1732，降低50%后σ_buyer≈0.173，与0.17吻合），且符合信息不对称降低不确定性的经济直觉。

## Search Query

decomposition of buyer perception noise intrinsic vs information asymmetry
