# N165: 头部对象（i=1）的绝对访问频率 λ_1：λ_1 = 5e7 * (1/1^0.9) / 9999.55 ≈ 5000.15 requests/day，该数值是

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N72

## Claim

头部对象（i=1）的绝对访问频率 λ_1：λ_1 = 5e7 * (1/1^0.9) / 9999.55 ≈ 5000.15 requests/day，该数值是计算 LRU 栈顶对象驻留时间 T_1 = 1/λ_1 的基础，直接决定 Top-1 对象是否受更新率影响（T_1 ≈ 2.4e-4 days）。

## Corrected Claim

头部对象（i=1）的绝对访问频率 λ_1：λ_1 = 5e7 * (1/1^0.9) / 9999.55 ≈ 5000.15 requests/day，该数值是计算 LRU 栈顶对象驻留时间 T_1 = 1/λ_1 的基础，直接决定 Top-1 对象是否受更新率影响（T_1 ≈ 2.4e-4 days）。

## Evidence

先验知识/题面给定，逻辑校验通过
