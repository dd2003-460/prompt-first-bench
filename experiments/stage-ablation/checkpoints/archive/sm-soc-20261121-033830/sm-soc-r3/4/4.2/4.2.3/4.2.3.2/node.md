# N227: 候选B的库存天数 D_days 的动态权重：D_days 并非静态输入，而是随时间 t 衰减的变量，有效库存压力 D_eff(t) = D_days * exp

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

候选B的库存天数 D_days 的动态权重：D_days 并非静态输入，而是随时间 t 衰减的变量，有效库存压力 D_eff(t) = D_days * exp(-λ_t * t)，其中 λ_t 为买家需求到达率，高需求时期（λ_t 高）库存压力衰减快，算法应动态调整建议价以反映实时流动性。

## Corrected Claim

候选B的库存天数 D_days 的动态权重：D_days 并非静态输入，而是随时间 t 衰减的变量，有效库存压力 D_eff(t) = D_days * exp(-λ_t * t)，其中 λ_t 为买家需求到达率，高需求时期（λ_t 高）库存压力衰减快，算法应动态调整建议价以反映实时流动性。

## Evidence

先验知识/题面给定，逻辑校验通过
