# N146: 对象 i 的访问间隔均值 E[T_i] (小时) 的具体计算公式为 E[T_i] = 24 / λ_i = 24 / (500 * r_i) = 0.048 /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

对象 i 的访问间隔均值 E[T_i] (小时) 的具体计算公式为 E[T_i] = 24 / λ_i = 24 / (500 * r_i) = 0.048 / r_i 小时，该值直接决定 LRU 队列中该位置的驱逐压力。

## Corrected Claim

对象 i 的访问间隔均值 E[T_i] (小时) 的具体计算公式为 E[T_i] = 24 / λ_i = 24 / (500 * r_i) = 0.048 / r_i 小时，该值直接决定 LRU 队列中该位置的驱逐压力。

## Evidence

先验知识/题面给定，逻辑校验通过：泊松过程或指数分布下，均值间隔 E[T] = 1/λ，若 λ 单位为次/天且总请求量为 500 次/天，则 λ_i = 500 * r_i，E[T_i] = 24 / (500 * r_i) = 0.048 / r_i 小时，推导自洽。
