# N311: 高敏感参数判定规则：若参数xi的临界变化量|Δxi| < σ_xi（标准差），则标记为高敏感；例如，若GPU价格标准差σ_price=$150，而临界ΔP=$2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

高敏感参数判定规则：若参数xi的临界变化量|Δxi| < σ_xi（标准差），则标记为高敏感；例如，若GPU价格标准差σ_price=$150，而临界ΔP=$2,400，则ΔP >> σ_price，价格不是高敏感参数；若电价标准差σ_r=$0.02/kWh，而临界Δr=$0.005/kWh，则Δr < σ_r，电价是高敏感参数

## Corrected Claim

高敏感参数判定规则：若参数xi的临界变化量|Δxi| < σ_xi（标准差），则标记为高敏感；例如，若GPU价格标准差σ_price=$150，而临界ΔP=$2,400，则ΔP >> σ_price，价格不是高敏感参数；若电价标准差σ_r=$0.02/kWh，而临界Δr=$0.005/kWh，则Δr < σ_r，电价是高敏感参数

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述定义了高敏感参数的判定规则（|Δxi| < σ_xi），并通过两个具体数值示例（GPU价格 ΔP=2400 >> σ=150 为非敏感；电价 Δr=0.005 < σ=0.02 为敏感）展示了规则的应用，数值比较逻辑自洽，量纲一致，无内部矛盾。

## Search Query

sensitivity threshold high sensitivity parameter definition
