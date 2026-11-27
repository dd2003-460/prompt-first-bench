# N412: 有效价格 P_eff 的相对优势阈值需满足 P_eff_high > P_eff_low，其中 P_eff_high = P_list_high - λ_tru

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N132

## Claim

有效价格 P_eff 的相对优势阈值需满足 P_eff_high > P_eff_low，其中 P_eff_high = P_list_high - λ_trust * S_sig_high，P_eff_low = P_list_low - λ_trust * S_sig_low，需解出满足该不等式的 λ_trust 最小值。

## Corrected Claim

有效价格 P_eff 的相对优势阈值需满足 P_eff_high > P_eff_low，其中 P_eff_high = P_list_high - λ_trust * S_sig_high，P_eff_low = P_list_low - λ_trust * S_sig_low，需解出满足该不等式的 λ_trust 最小值。

## Evidence

先验知识/题面给定，逻辑校验通过
