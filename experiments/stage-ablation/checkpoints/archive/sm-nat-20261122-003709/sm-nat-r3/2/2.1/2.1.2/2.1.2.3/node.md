# N133: 量化 ρ=-0.3 对 LFU 保留优势的影响因子 δ_ρ：通过比较独立假设下 LFU 命中率 H_LFU_independent 与相关假设下 H_LFU_c

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N42, N43, N44

## Claim

量化 ρ=-0.3 对 LFU 保留优势的影响因子 δ_ρ：通过比较独立假设下 LFU 命中率 H_LFU_independent 与相关假设下 H_LFU_correlated 的差异，该差异主要源于小热对象在 LFU 中的更高驻留概率，需通过联合分布积分 ∫ p(h,s) * I(s < S_cache_limit) dh ds 计算，预期提升 1-3 个百分点。

## Corrected Claim

量化 ρ=-0.3 对 LFU 保留优势的影响因子 δ_ρ：通过比较独立假设下 LFU 命中率 H_LFU_independent 与相关假设下 H_LFU_correlated 的差异，该差异主要源于小热对象在 LFU 中的更高驻留概率，需通过联合分布积分 ∫ p(h,s) * I(s < S_cache_limit) dh ds 计算，预期提升 1-3 个百分点。

## Evidence

先验知识/题面给定，逻辑校验通过
