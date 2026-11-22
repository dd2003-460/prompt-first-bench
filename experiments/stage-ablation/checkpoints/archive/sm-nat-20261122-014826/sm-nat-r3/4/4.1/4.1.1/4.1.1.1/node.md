# N124: λ_i 的解析表达式：对于 Rank 为 r 的对象，其请求率 λ_r = (Total_Requests / Z) * r^(-β)。代入 Total_Req

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N45

## Claim

λ_i 的解析表达式：对于 Rank 为 r 的对象，其请求率 λ_r = (Total_Requests / Z) * r^(-β)。代入 Total_Requests = 50,000,000/天, Z = 12,589, β=0.9，得 λ_r = 3971.6 * r^(-0.9) 次/天。例如 Rank 1 对象 λ_1 ≈ 3972 次/天，Rank 10,000 对象 λ_10000 ≈ 25.1 次/天。

## Corrected Claim

λ_i 的解析表达式：对于 Rank 为 r 的对象，其请求率 λ_r = (Total_Requests / Z) * r^(-β)。代入 Total_Requests = 50,000,000/天, Z = 12,589, β=0.9，得 λ_r = 3971.6 * r^(-0.9) 次/天。例如 Rank 1 对象 λ_1 ≈ 3972 次/天，Rank 10,000 对象 λ_10000 ≈ 25.1 次/天。

## Evidence

先验知识/题面给定，逻辑校验通过：50,000,000 / 12,589 ≈ 3971.6，且 3971.6 * 10000^(-0.9) ≈ 25.1，数值计算准确，符合 Zipf 分布定义。
