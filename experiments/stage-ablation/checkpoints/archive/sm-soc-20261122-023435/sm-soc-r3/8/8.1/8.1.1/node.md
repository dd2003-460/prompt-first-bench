# N229: 权重衰减时间常数 T_decay 的机制解释：T_decay ≈ 24h 反映了平台算法对‘新鲜度’的偏好。在 t=T_decay 时，exp(-t/T_dec

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N74

## Claim

权重衰减时间常数 T_decay 的机制解释：T_decay ≈ 24h 反映了平台算法对‘新鲜度’的偏好。在 t=T_decay 时，exp(-t/T_decay) ≈ 0.37，意味着高溢价带来的流量加权衰减至初始值的 37%，剩余部分依赖商品本身的质量信号。

## Corrected Claim

权重衰减时间常数 T_decay 的机制解释：T_decay ≈ 24h 反映了平台算法对‘新鲜度’的偏好。在 t=T_decay 时，exp(-t/T_decay) ≈ 0.37，意味着高溢价带来的流量加权衰减至初始值的 37%，剩余部分依赖商品本身的质量信号。

## Evidence

先验知识/题面给定，逻辑校验通过：指数衰减函数 exp(-1) 的数学性质确为约 0.3679，与陈述中 0.37 一致；机制解释符合常见的推荐系统时间衰减模型逻辑。

## Search Query

platform recommendation algorithm freshness decay time constant
