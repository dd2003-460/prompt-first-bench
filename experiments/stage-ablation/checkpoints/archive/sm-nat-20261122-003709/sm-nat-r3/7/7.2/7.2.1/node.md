# N229: 修正LFU收敛时间常数公式：公式 τ_convergence ≈ 3 / λ_update 错误地将对象更新率（1%/天）混淆为请求到达率。LFU计数器收敛取决

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N86

## Claim

修正LFU收敛时间常数公式：公式 τ_convergence ≈ 3 / λ_update 错误地将对象更新率（1%/天）混淆为请求到达率。LFU计数器收敛取决于请求频率，正确公式应为 τ_convergence ≈ 3 / λ_request，其中 λ_request = 50,000,000 / 100,000 = 500 requests/day/object（平均），故 τ ≈ 3/500 = 0.006 天 ≈ 8.6 分钟，而非 300 天。

## Corrected Claim

修正LFU收敛时间常数公式：公式 τ_convergence ≈ 3 / λ_update 错误地将对象更新率（1%/天）混淆为请求到达率。LFU计数器收敛取决于请求频率，正确公式应为 τ_convergence ≈ 3 / λ_request，其中 λ_request = 50,000,000 / 100,000 = 500 requests/day/object（平均），故 τ ≈ 3/500 = 0.006 天 ≈ 8.6 分钟，而非 300 天。

## Evidence

先验知识/题面给定，逻辑校验通过：LFU收敛时间确实取决于请求到达率而非对象更新率，数值推导（500 req/day/object -> 0.006天）符合逻辑且量级合理。
