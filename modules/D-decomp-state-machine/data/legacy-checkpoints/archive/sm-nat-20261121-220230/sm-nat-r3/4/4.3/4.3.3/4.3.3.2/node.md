# N205: 在负相关 ρ=-0.3 下，LFU 增益的修正系数 k_corr 可通过 Copula 积分计算：k_corr = ∫∫_{s_i * λ_i > thresh

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

在负相关 ρ=-0.3 下，LFU 增益的修正系数 k_corr 可通过 Copula 积分计算：k_corr = ∫∫_{s_i * λ_i > threshold} f_{S,H}(s,h) ds dh / ∫∫_{s_i * λ_i > threshold} f_S(s) f_H(h) ds dh，该系数反映了负相关对 LFU 增益的抑制作用。

## Corrected Claim

在负相关 ρ=-0.3 下，LFU 增益的修正系数 k_corr 可通过 Copula 积分计算：k_corr = ∫∫_{s_i * λ_i > threshold} f_{S,H}(s,h) ds dh / ∫∫_{s_i * λ_i > threshold} f_S(s) f_H(h) ds dh，该系数反映了负相关对 LFU 增益的抑制作用。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式结构符合Copula理论中通过联合分布与独立分布之比来量化相关性对特定区域（此处为LFU命中/增益区域）概率影响的定义，负相关确实会改变联合分布形态从而修正增益系数，逻辑自洽。
