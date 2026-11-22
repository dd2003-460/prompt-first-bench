# N68: LRU 平均驻留时间 λ 的解析计算：λ = C / (R_total * E[S|S≤S_max])，其中 C=131072MB, R_total=5000万

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

LRU 平均驻留时间 λ 的解析计算：λ = C / (R_total * E[S|S≤S_max])，其中 C=131072MB, R_total=5000万次/天，E[S]由Pareto(α=1.1)截断分布计算，用于确定更新失效因子的指数

## Corrected Claim

LRU 平均驻留时间 λ 的解析计算：λ = C / (R_total * E[S|S≤S_max])，其中 C=131072MB, R_total=5000万次/天，E[S]由Pareto(α=1.1)截断分布计算，用于确定更新失效因子的指数

## Evidence

父节点级核验未通过：非正交（子节点2和子节点3存在逻辑冲突且非正交。子节点2指出公式中应使用 E[S|S≤S_max]（即缓存内对象的平均大小），而子节点3提出正确公式应使用 E[S_miss]（未命中对象的平均大小）并引入 miss rate。这两个子节点对分子/分母中期望值的定义提出了互斥的修正方向（一个是条件期望于缓存容量，一个是条件期望于miss事件），且子节点3直接推翻了子节点2所基于的原始公式结构，导致两者在‘如何修正λ’这一核心问题上重叠且矛盾，缺乏正交性。）

## Search Query

LRU average residence time cache size request rate mean object size formula
