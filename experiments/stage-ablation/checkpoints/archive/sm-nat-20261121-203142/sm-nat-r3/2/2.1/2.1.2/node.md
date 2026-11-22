# N37: 缓存驻留时间 T_residence 的估算公式：T_residence ≈ C / (λ * E[S])，其中 λ 为每秒请求率 (5000万/86400 ≈

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

缓存驻留时间 T_residence 的估算公式：T_residence ≈ C / (λ * E[S])，其中 λ 为每秒请求率 (5000万/86400 ≈ 578 req/s)，E[S] 为平均对象大小，该时间决定对象在缓存中的平均存活期

## Corrected Claim

缓存驻留时间 T_residence 的估算公式：T_residence ≈ C / (λ * E[S])，其中 λ 为每秒请求率 (5000万/86400 ≈ 578 req/s)，E[S] 为平均对象大小，该时间决定对象在缓存中的平均存活期

## Evidence

父节点级核验未通过：有冗余（子节点本质上是同一公式在两个不同参数（x_min）下的具体算例，而非正交的概念维度。虽然覆盖了‘基准’和‘高成本’两个典型场景，但结构上属于‘参数敏感性分析’或‘多场景估算’，而非独立的知识模块。）
