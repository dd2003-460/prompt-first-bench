# N254: τ_locality 的量化定义：在 Poisson 到达与 Pareto(β=0.9) 热度分布下，局部性时间常数 τ_locality 等于对象重复访问间隔

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88

## Claim

τ_locality 的量化定义：在 Poisson 到达与 Pareto(β=0.9) 热度分布下，局部性时间常数 τ_locality 等于对象重复访问间隔的均值，计算公式为 τ_locality = 1 / E[λ_i]，其中 E[λ_i] 为所有对象请求频率的调和平均数（Harmonic Mean），该值直接决定 H_LRU(t) 的指数衰减斜率。

## Corrected Claim

τ_locality 的量化定义：在 Poisson 到达与 Pareto(β=0.9) 热度分布下，局部性时间常数 τ_locality 等于对象重复访问间隔的均值，计算公式为 τ_locality = 1 / E[λ_i]，其中 E[λ_i] 为所有对象请求频率的调和平均数（Harmonic Mean），该值直接决定 H_LRU(t) 的指数衰减斜率。

## Evidence

先验知识/题面给定，逻辑校验通过：在Poisson到达假设下，单个对象的重复访问间隔服从指数分布，其均值为1/λ_i；对所有对象取平均（即频率的调和平均的倒数），得到系统级的平均重复访问间隔，该定义在缓存局部性理论中是标准且自洽的。

## Search Query

harmonic mean of request rates locality time constant
