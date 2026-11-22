# N359: λ_learning 的估算公式：基于卖家在干预实施后第 k 周规避行为（如隐藏真实价格或调整标签）的比例 P_evasion(k)，通过线性回归 ln(P_e

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N123

## Claim

λ_learning 的估算公式：基于卖家在干预实施后第 k 周规避行为（如隐藏真实价格或调整标签）的比例 P_evasion(k)，通过线性回归 ln(P_evasion) ~ -λ_learning * k 估算，需至少 4 周数据点以消除初始冲击噪声。

## Corrected Claim

λ_learning 的估算公式：基于卖家在干预实施后第 k 周规避行为（如隐藏真实价格或调整标签）的比例 P_evasion(k)，通过线性回归 ln(P_evasion) ~ -λ_learning * k 估算，需至少 4 周数据点以消除初始冲击噪声。

## Evidence

先验知识/题面给定，逻辑校验通过
