# N211: Top 1% 热门对象（k=1..1000）的平均驻留时间 W_LRU_top1% = (1/1000) * Σ_{k=1}^{1000} (1/λ_k)，需根

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

Top 1% 热门对象（k=1..1000）的平均驻留时间 W_LRU_top1% = (1/1000) * Σ_{k=1}^{1000} (1/λ_k)，需根据 Pareto(β=0.9) 热度分布计算 λ_k 的具体数值。

## Corrected Claim

Top 1% 热门对象（k=1..1000）的平均驻留时间 W_LRU_top1% = (1/1000) * Σ_{k=1}^{1000} (1/λ_k)，需根据 Pareto(β=0.9) 热度分布计算 λ_k 的具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU驻留时间定义为访问间隔的倒数，平均驻留时间即各对象驻留时间的算术平均，公式推导符合定义。
