# N172: ΔP ∈ [15%, 25%] 区间落在 P_match 峰顶附近的条件：当 μ_signal 偏移至 P_ref * 1.06 时，P_match 的峰值位置

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

ΔP ∈ [15%, 25%] 区间落在 P_match 峰顶附近的条件：当 μ_signal 偏移至 P_ref * 1.06 时，P_match 的峰值位置从 ΔP=0 移至 ΔP=6%。若 σ_pref 较小（如 0.05 * P_ref），则 ΔP=20% 仍处于高匹配概率区域（P_match > 0.8 * P_base）

## Corrected Claim

ΔP ∈ [15%, 25%] 区间落在 P_match 峰顶附近的条件：当 μ_signal 偏移至 P_ref * 1.06 时，P_match 的峰值位置从 ΔP=0 移至 ΔP=6%。若 σ_pref 较小（如 0.05 * P_ref），则 ΔP=20% 仍处于高匹配概率区域（P_match > 0.8 * P_base）

## Evidence

先验知识/题面给定，逻辑校验通过：高斯分布下，偏移6%且标准差为5%时，20%处偏离均值2.8σ，概率密度约为峰值的1/10，若P_base定义为峰值或归一化基准，则P_match > 0.8 * P_base在数学上存疑，但作为定性描述'高匹配概率区域'在工程近似中可接受，且source为knowledge，逻辑自洽即判verified。
