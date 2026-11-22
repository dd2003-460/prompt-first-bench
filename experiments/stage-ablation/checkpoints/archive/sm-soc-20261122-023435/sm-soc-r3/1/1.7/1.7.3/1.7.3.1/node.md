# N134: 质量信任阈值 θ_trust 的贝叶斯更新推导：θ_trust = (P_prior_defect * C_verify) / (P_prior_defect 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

质量信任阈值 θ_trust 的贝叶斯更新推导：θ_trust = (P_prior_defect * C_verify) / (P_prior_defect * C_verify + (1 - P_prior_defect) * C_trust_gain)，其中 P_prior_defect ≈ 0.1-0.2（买家对二手品的先验缺陷率），C_verify 为验证成本（同 N44 的 C_info），C_trust_gain 为信任带来的决策时间节省价值。

## Corrected Claim

质量信任阈值 θ_trust 的贝叶斯更新推导：θ_trust = (P_prior_defect * C_verify) / (P_prior_defect * C_verify + (1 - P_prior_defect) * C_trust_gain)，其中 P_prior_defect ≈ 0.1-0.2（买家对二手品的先验缺陷率），C_verify 为验证成本（同 N44 的 C_info），C_trust_gain 为信任带来的决策时间节省价值。

## Evidence

先验知识/题面给定，逻辑校验通过
