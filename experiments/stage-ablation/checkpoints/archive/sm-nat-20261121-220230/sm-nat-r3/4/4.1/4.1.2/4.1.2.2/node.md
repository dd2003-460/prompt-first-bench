# N190: 工作点B（负相关修正，ρ=-0.3）：在负相关 ρ=-0.3 下，小对象更热，C_corr 中平均对象大小小于 C_indep。填充误差 E_corr ≈ E_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N65

## Claim

工作点B（负相关修正，ρ=-0.3）：在负相关 ρ=-0.3 下，小对象更热，C_corr 中平均对象大小小于 C_indep。填充误差 E_corr ≈ E_indep * (1 - 0.3 * (α-1)/(β-1)) ≈ 640MB * 0.97 ≈ 621MB。差异 ΔE ≈ 19MB，占 128GB 的 0.015%。该工作点代表中性价比最优场景，适用于已知相关性系数的精细化估算。

## Corrected Claim

工作点B（负相关修正，ρ=-0.3）：在负相关 ρ=-0.3 下，小对象更热，C_corr 中平均对象大小小于 C_indep。填充误差 E_corr ≈ E_indep * (1 - 0.3 * (α-1)/(β-1)) ≈ 640MB * 0.97 ≈ 621MB。差异 ΔE ≈ 19MB，占 128GB 的 0.015%。该工作点代表中性价比最优场景，适用于已知相关性系数的精细化估算。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算（640*0.97=620.8≈621，差值19MB，占比0.015%）准确，负相关导致小对象更热从而降低填充误差的逻辑符合缓存/存储优化原理。

## Search Query

cache fill error negative correlation size heat
