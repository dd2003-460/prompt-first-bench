# N61: 排队延迟修正项 L_queue = f(λ/μ)，其中 λ 为到达率，μ 为服务率；在 Poisson 到达/指数服务（M/M/1）模型下，L_queue = 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

排队延迟修正项 L_queue = f(λ/μ)，其中 λ 为到达率，μ 为服务率；在 Poisson 到达/指数服务（M/M/1）模型下，L_queue = λ / (μ(μ-λ))；峰值时段 λ 接近 μ，L_queue 急剧上升，导致 P99 尾部延迟远超平均跳数延迟。

## Corrected Claim

排队延迟修正项 L_queue = f(λ/μ)，其中 λ 为到达率，μ 为服务率；在 Poisson 到达/指数服务（M/M/1）模型下，L_queue = λ / (μ(μ-λ))；峰值时段 λ 接近 μ，L_queue 急剧上升，导致 P99 尾部延迟远超平均跳数延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：M/M/1队列中Lq=λ/(μ(μ-λ))是标准排队论公式，且λ→μ时延迟发散符合物理直觉
