# N37: 缓存驻留时间 T_residence 的估算公式：T_residence ≈ C / (λ * E[S])，其中 λ 为每秒请求率 (5000万/86400 ≈

- **status**: verified
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

先验知识/题面给定，逻辑校验通过：公式 T_residence ≈ C / (λ * E[S]) 符合 Little's Law 在缓存容量约束下的推导（平均驻留时间 = 缓存容量 / 平均每秒写入字节数），数值量级合理（5000万/86400 ≈ 578 req/s 计算正确）。
