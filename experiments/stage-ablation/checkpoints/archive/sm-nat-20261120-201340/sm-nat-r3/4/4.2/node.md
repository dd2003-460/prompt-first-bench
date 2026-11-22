# N19: LRU 缓存中对象的平均驻留时间 T_resident 近似为缓存容量 C 除以请求率 R 与对象平均大小 S_avg 的乘积（T_resident ≈ C /

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

LRU 缓存中对象的平均驻留时间 T_resident 近似为缓存容量 C 除以请求率 R 与对象平均大小 S_avg 的乘积（T_resident ≈ C / (R * S_avg)），在 Pareto(α=1.1) 大小分布下 S_avg 需通过截断期望计算，该值决定更新损耗的时间窗口。

## Corrected Claim

LRU 缓存中对象的平均驻留时间 T_resident 近似为缓存容量 C 除以请求率 R 与对象平均大小 S_avg 的乘积（T_resident ≈ C / (R * S_avg)），在 Pareto(α=1.1) 大小分布下 S_avg 需通过截断期望计算，该值决定更新损耗的时间窗口。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU缓存驻留时间量级估算符合基本排队论直觉，Pareto分布截断期望计算逻辑自洽
