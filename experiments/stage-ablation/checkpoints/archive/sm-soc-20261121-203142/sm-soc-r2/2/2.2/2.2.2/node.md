# N45: 投影1（算法识别层）：平台算法对信号 S_sig 的响应函数 R_algo(S_sig) = 1 - exp(-k * S_sig / T_noise)，其中 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N11, N12, N13

## Claim

投影1（算法识别层）：平台算法对信号 S_sig 的响应函数 R_algo(S_sig) = 1 - exp(-k * S_sig / T_noise)，其中 k 为算法敏感度系数，T_noise 为噪声阈值；当 S_sig < T_noise 时，R_algo ≈ 0，导致曝光量 ΔExposure ≈ 0。

## Corrected Claim

投影1（算法识别层）：平台算法对信号 S_sig 的响应函数 R_algo(S_sig) = 1 - exp(-k * S_sig / T_noise)，其中 k 为算法敏感度系数，T_noise 为噪声阈值；当 S_sig < T_noise 时，R_algo ≈ 0，导致曝光量 ΔExposure ≈ 0。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

algorithm sensitivity threshold product listing update exposure boost
