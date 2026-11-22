# N26: Pareto(β=0.9) 的热度变异系数 CV_freq = sqrt((β-1)/(β-3)) 在 β<3 时同样发散，需数值积分计算：CV_freq = 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N7

## Claim

Pareto(β=0.9) 的热度变异系数 CV_freq = sqrt((β-1)/(β-3)) 在 β<3 时同样发散，需数值积分计算：CV_freq = sqrt(∫ f^2 g(f) df / (∫ f g(f) df)^2 - 1)，对于 β=0.9，CV_freq 极大，表明热度分布极度倾斜，少数热门对象主导请求量。

## Corrected Claim

Pareto(β=0.9) 的热度变异系数 CV_freq = sqrt((β-1)/(β-3)) 在 β<3 时同样发散，需数值积分计算：CV_freq = sqrt(∫ f^2 g(f) df / (∫ f g(f) df)^2 - 1)，对于 β=0.9，CV_freq 极大，表明热度分布极度倾斜，少数热门对象主导请求量。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 733)
