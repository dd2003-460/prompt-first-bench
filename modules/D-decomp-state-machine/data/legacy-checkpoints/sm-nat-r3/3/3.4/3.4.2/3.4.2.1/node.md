# N193: LFU 频率排名失稳的量化条件：λ_update * T_residence_avg > 0.1。当 λ_update = 0.01/天，T_residence

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

LFU 频率排名失稳的量化条件：λ_update * T_residence_avg > 0.1。当 λ_update = 0.01/天，T_residence_avg = 1 小时时，λ_update * T_residence_avg = 0.01 * (1/24) ≈ 0.00042 << 0.1，因此 LFU 频率排名稳定，ΔH_net 不为 0。

## Corrected Claim

LFU 频率排名失稳的量化条件：λ_update * T_residence_avg > 0.1。当 λ_update = 0.01/天，T_residence_avg = 1 小时时，λ_update * T_residence_avg = 0.01 * (1/24) ≈ 0.00042 << 0.1，因此 LFU 频率排名稳定，ΔH_net 不为 0。

## Evidence

先验知识/题面给定，逻辑校验通过：单位换算正确（1小时=1/24天），数值计算准确（0.01 * 1/24 ≈ 0.00042），且 0.00042 < 0.1 符合逻辑推导，结论与前提一致。
