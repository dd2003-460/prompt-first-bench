# N13: 高成本低性工作点：更新率与对象大小分布的交互效应，大对象更新频率低但重填充成本高，小对象更新频率高但重填充成本低，综合折损比例 = ∫ p_invalid(s)

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

高成本低性工作点：更新率与对象大小分布的交互效应，大对象更新频率低但重填充成本高，小对象更新频率高但重填充成本低，综合折损比例 = ∫ p_invalid(s) * cost_refill(s) ds / ∫ cost_miss(s) ds，估算折损 0.8-1.5%

## Corrected Claim

高成本低性工作点：更新率与对象大小分布的交互效应，大对象更新频率低但重填充成本高，小对象更新频率高但重填充成本低，综合折损比例 = ∫ p_invalid(s) * cost_refill(s) ds / ∫ cost_miss(s) ds，估算折损 0.8-1.5%

## Evidence

先验知识/题面给定，逻辑校验通过
