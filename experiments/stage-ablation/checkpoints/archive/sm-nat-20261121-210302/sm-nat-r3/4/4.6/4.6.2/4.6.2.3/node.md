# N172: Pareto(β=0.9) 热度分布的截断效应：当 i 接近 N=100,000 时，f_i 的值受有限 N 截断影响，尾部对象的频率 f_N = C * N^

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

Pareto(β=0.9) 热度分布的截断效应：当 i 接近 N=100,000 时，f_i 的值受有限 N 截断影响，尾部对象的频率 f_N = C * N^{-0.9} 需单独计算，以避免使用无限总体的解析式导致长尾频率高估。

## Corrected Claim

Pareto(β=0.9) 热度分布的截断效应：当 i 接近 N=100,000 时，f_i 的值受有限 N 截断影响，尾部对象的频率 f_N = C * N^{-0.9} 需单独计算，以避免使用无限总体的解析式导致长尾频率高估。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布定义明确，有限总体截断导致尾部频率需单独计算以避免高估，符合数学逻辑。
