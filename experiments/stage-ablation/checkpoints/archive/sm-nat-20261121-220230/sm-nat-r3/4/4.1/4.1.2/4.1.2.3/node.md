# N191: 工作点C（强负相关，ρ=-0.6）：在强负相关 ρ=-0.6 下，小对象显著更热，C_corr 中平均对象大小大幅小于 C_indep。填充误差 E_corr 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N65

## Claim

工作点C（强负相关，ρ=-0.6）：在强负相关 ρ=-0.6 下，小对象显著更热，C_corr 中平均对象大小大幅小于 C_indep。填充误差 E_corr ≈ E_indep * (1 - 0.6 * (α-1)/(β-1)) ≈ 640MB * 0.94 ≈ 602MB。差异 ΔE ≈ 38MB，占 128GB 的 0.03%。该工作点代表高成本低性场景，适用于极端相关性假设下的敏感性分析。

## Corrected Claim

工作点C（强负相关，ρ=-0.6）：在强负相关 ρ=-0.6 下，小对象显著更热，C_corr 中平均对象大小大幅小于 C_indep。填充误差 E_corr ≈ E_indep * (1 - 0.6 * (α-1)/(β-1)) ≈ 640MB * 0.94 ≈ 602MB。差异 ΔE ≈ 38MB，占 128GB 的 0.03%。该工作点代表高成本低性场景，适用于极端相关性假设下的敏感性分析。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算自洽（640*0.94=601.6≈602，差值38MB，占比0.03%），符合强负相关下小对象占比增加导致填充误差降低的物理直觉。

## Search Query

cache fill error strong negative correlation sensitivity
