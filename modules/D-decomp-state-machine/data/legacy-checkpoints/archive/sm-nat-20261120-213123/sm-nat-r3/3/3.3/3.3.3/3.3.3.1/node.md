# N119: 工作点1（高性低成/小对象主导）：假设热门对象平均驻留时间 T_LRU ≈ 1天，更新率 u=0.01/天，则 u*T_LRU = 0.01 < 0.1，线性近

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

工作点1（高性低成/小对象主导）：假设热门对象平均驻留时间 T_LRU ≈ 1天，更新率 u=0.01/天，则 u*T_LRU = 0.01 < 0.1，线性近似有效；有效命中率折损 D_linear = 1 - 0.01 = 0.99，即损失1%。

## Corrected Claim

工作点1（高性低成/小对象主导）：假设热门对象平均驻留时间 T_LRU ≈ 1天，更新率 u=0.01/天，则 u*T_LRU = 0.01 < 0.1，线性近似有效；有效命中率折损 D_linear = 1 - 0.01 = 0.99，即损失1%。

## Evidence

先验知识/题面给定，逻辑校验通过：u*T_LRU = 0.01 < 0.1 满足线性近似条件，D_linear = 1 - 0.01 = 0.99 计算正确
