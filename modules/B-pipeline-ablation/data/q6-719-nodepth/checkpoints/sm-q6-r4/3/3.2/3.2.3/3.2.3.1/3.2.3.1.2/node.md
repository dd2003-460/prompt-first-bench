# N734: 低带宽配置下的突发溢出概率 P_overflow 计算：基于泊松分布或M/M/1排队模型，若平均到达率 λ 与峰值系数 1.5 对应，P_overflow = 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N252

## Claim

低带宽配置下的突发溢出概率 P_overflow 计算：基于泊松分布或M/M/1排队模型，若平均到达率 λ 与峰值系数 1.5 对应，P_overflow = P(Queue > 0) 在低负载下接近 0，但需验证是否满足 SLA 要求 < 0.1%

## Corrected Claim

低带宽配置下的突发溢出概率 P_overflow 计算：基于泊松分布或M/M/1排队模型，若平均到达率 λ 与峰值系数 1.5 对应，P_overflow = P(Queue > 0) 在低负载下接近 0，但需验证是否满足 SLA 要求 < 0.1%

## Evidence

先验知识/题面给定，逻辑校验通过：在M/M/1排队模型中，低负载（ρ<1）且峰值系数有限时，队列长度分布收敛快，溢出概率确实趋近于0，符合排队论基本性质。
