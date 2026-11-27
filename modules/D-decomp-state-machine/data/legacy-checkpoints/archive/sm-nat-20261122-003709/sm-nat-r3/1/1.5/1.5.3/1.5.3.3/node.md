# N127: 确定R_byte计算的数值稳定性边界：当缓存容量C接近总数据量时，E[S|Miss]趋于无穷大或分布退化，R_byte公式失效，需改用积分形式H_byte = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N40

## Claim

确定R_byte计算的数值稳定性边界：当缓存容量C接近总数据量时，E[S|Miss]趋于无穷大或分布退化，R_byte公式失效，需改用积分形式H_byte = ∫ p(s) I(s in Cache) ds / ∫ p(s) ds 进行直接数值积分以避免除法奇点。

## Corrected Claim

确定R_byte计算的数值稳定性边界：当缓存容量C接近总数据量时，E[S|Miss]趋于无穷大或分布退化，R_byte公式失效，需改用积分形式H_byte = ∫ p(s) I(s in Cache) ds / ∫ p(s) ds 进行直接数值积分以避免除法奇点。

## Evidence

先验知识/题面给定，逻辑校验通过：当缓存容量C接近总数据量时，若采用基于条件期望或频率的离散/近似公式，确实可能因分母趋近于零或分布退化导致数值不稳定；改用积分形式直接计算期望值在数学上是处理此类边界情况的标准且稳健的方法，逻辑自洽。

## Search Query

numerical stability byte hit rate calculation near full cache capacity
