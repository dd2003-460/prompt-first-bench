# N216: 条件期望 E[S|Top10%] 的计算：由于热度 H 与大小 S 负相关 (ρ=-0.3)，Top10% 热门对象的大小分布向左偏移。假设联合分布为双变量对数

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N78

## Claim

条件期望 E[S|Top10%] 的计算：由于热度 H 与大小 S 负相关 (ρ=-0.3)，Top10% 热门对象的大小分布向左偏移。假设联合分布为双变量对数正态近似，E[log S | H > h_10%] < E[log S]。具体数值需通过积分 ∫_{h_10%}^∞ ∫ s * f_{S|H}(s|h) f_H(h) ds dh / P(H>h_10%) 计算。

## Corrected Claim

条件期望 E[S|Top10%] 的计算：由于热度 H 与大小 S 负相关 (ρ=-0.3)，Top10% 热门对象的大小分布向左偏移。假设联合分布为双变量对数正态近似，E[log S | H > h_10%] < E[log S]。具体数值需通过积分 ∫_{h_10%}^∞ ∫ s * f_{S|H}(s|h) f_H(h) ds dh / P(H>h_10%) 计算。

## Evidence

先验知识/题面给定，逻辑校验通过：负相关系数意味着高热度区间对应低大小分布，条件期望小于无条件期望符合统计学直觉，积分公式定义正确。

## Search Query

conditional expectation size given hotness negative correlation
