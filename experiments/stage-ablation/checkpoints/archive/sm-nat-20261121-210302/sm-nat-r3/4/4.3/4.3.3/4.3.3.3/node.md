# N138: 最大访问频率 f_max 的估算公式：f_max = λ_total * P_{max}，其中 λ_total = 50,000,000 次/天，P_{max}

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

最大访问频率 f_max 的估算公式：f_max = λ_total * P_{max}，其中 λ_total = 50,000,000 次/天，P_{max} 为最热对象的请求概率（由 Pareto 归一化常数决定）

## Corrected Claim

最大访问频率 f_max 的估算公式：f_max = λ_total * P_{max}，其中 λ_total = 50,000,000 次/天，P_{max} 为最热对象的请求概率（由 Pareto 归一化常数决定）

## Evidence

先验知识/题面给定，逻辑校验通过：最大访问频率等于总请求率乘以最热对象的概率，量纲与逻辑自洽。
