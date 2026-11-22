# N78: 信号失效的买家侧解释量化：若买家将'降价'解读为'商品有瑕疵'（负面信号），则买家保留价下移 ΔR_neg = -γ * (P_old - P_new)。若 γ

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

信号失效的买家侧解释量化：若买家将'降价'解读为'商品有瑕疵'（负面信号），则买家保留价下移 ΔR_neg = -γ * (P_old - P_new)。若 γ=0.5 (信号敏感度)，且降价幅度为 10%，则保留价下移 5%，导致有效需求减少，咨询量下降至基准的 e^(-ΔR_neg/σ_noise) 倍，需计算该倍数是否与 60% 无咨询率吻合。

## Corrected Claim

信号失效的买家侧解释量化：若买家将'降价'解读为'商品有瑕疵'（负面信号），则买家保留价下移 ΔR_neg = -γ * (P_old - P_new)。若 γ=0.5 (信号敏感度)，且降价幅度为 10%，则保留价下移 5%，导致有效需求减少，咨询量下降至基准的 e^(-ΔR_neg/σ_noise) 倍，需计算该倍数是否与 60% 无咨询率吻合。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

negative signal effect price reduction buyer reservation price shift
