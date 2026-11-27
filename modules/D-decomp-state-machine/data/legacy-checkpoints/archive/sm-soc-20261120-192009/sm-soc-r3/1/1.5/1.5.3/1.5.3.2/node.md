# N169: θ_std 的异质性来源：θ_std 主要受买家经验值（Expertise）影响，公式为 θ_std = θ_std_base * (1 - β_exp * E

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

θ_std 的异质性来源：θ_std 主要受买家经验值（Expertise）影响，公式为 θ_std = θ_std_base * (1 - β_exp * Expertise_norm)，其中 Expertise_norm 为买家历史交易次数归一化值；高经验买家（Expertise_norm > 0.8）的 θ_verify 方差显著小于新手买家，导致其筛选行为更一致。

## Corrected Claim

θ_std 的异质性来源：θ_std 主要受买家经验值（Expertise）影响，公式为 θ_std = θ_std_base * (1 - β_exp * Expertise_norm)，其中 Expertise_norm 为买家历史交易次数归一化值；高经验买家（Expertise_norm > 0.8）的 θ_verify 方差显著小于新手买家，导致其筛选行为更一致。

## Evidence

先验知识/题面给定，逻辑校验通过
