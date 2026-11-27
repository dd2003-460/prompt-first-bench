# N65: 对象i的访问到达率 λ_i 的具体数值：λ_i = F_i / 86400（次/秒），其中 F_i 是对象i的日均请求次数，由 Pareto(β=0.9) 分布

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

对象i的访问到达率 λ_i 的具体数值：λ_i = F_i / 86400（次/秒），其中 F_i 是对象i的日均请求次数，由 Pareto(β=0.9) 分布确定，头部对象 F_i 可达百万级，尾部对象 F_i < 1次/天。

## Corrected Claim

对象i的访问到达率 λ_i 的具体数值：λ_i = F_i / 86400（次/秒），其中 F_i 是对象i的日均请求次数，由 Pareto(β=0.9) 分布确定，头部对象 F_i 可达百万级，尾部对象 F_i < 1次/天。

## Evidence

先验知识/题面给定，逻辑校验通过：λ=F/86400 量纲正确（次/天 ÷ 秒/天 = 次/秒）；Pareto(β=0.9) 分布具有重尾特性，头部高频、尾部低频符合该分布数学性质，数值量级合理。
