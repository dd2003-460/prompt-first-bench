# N167: 工作点1（高响应/高溢价）：当 v_high(t) 近似为阶跃函数（即时响应）且 P_high = 1.2 * P_median 时，积分收敛速度最快，但 λ_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

工作点1（高响应/高溢价）：当 v_high(t) 近似为阶跃函数（即时响应）且 P_high = 1.2 * P_median 时，积分收敛速度最快，但 λ_b(P_high) 显著降低，导致 P(Sale) 的峰值出现在 t=0+ 附近，需计算此时的具体数值。

## Corrected Claim

工作点1（高响应/高溢价）：当 v_high(t) 近似为阶跃函数（即时响应）且 P_high = 1.2 * P_median 时，积分收敛速度最快，但 λ_b(P_high) 显著降低，导致 P(Sale) 的峰值出现在 t=0+ 附近，需计算此时的具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过：阶跃函数响应意味着瞬时变化，积分收敛最快符合直觉；价格高于中位数导致需求/购买概率下降（λ_b降低）符合经济学基本规律，峰值出现在t=0+附近符合高溢价下的即时抢购或衰减模型特征。

## Search Query

immediate response high price sale probability integral
