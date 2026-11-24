# N450: 华北/华南区域P99延迟的排队论贡献 T_queue_p99 = (1 / (μ - λ)) × ln(1 / (1 - ρ_pop))，其中 μ 为单POP服

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N151

## Claim

华北/华南区域P99延迟的排队论贡献 T_queue_p99 = (1 / (μ - λ)) × ln(1 / (1 - ρ_pop))，其中 μ 为单POP服务速率（假设10Gbps/对象大小），λ 为区域请求到达率（20%总流量），ρ_pop 为POP利用率；当 ρ_pop > 0.8 时，T_queue_p99 呈非线性爆炸，需增设POP以降低 ρ_pop 至 0.6 以下以控制 P99。

## Corrected Claim

华北/华南区域P99延迟的排队论贡献 T_queue_p99 = (1 / (μ - λ)) × ln(1 / (1 - ρ_pop))，其中 μ 为单POP服务速率（假设10Gbps/对象大小），λ 为区域请求到达率（20%总流量），ρ_pop 为POP利用率；当 ρ_pop > 0.8 时，T_queue_p99 呈非线性爆炸，需增设POP以降低 ρ_pop 至 0.6 以下以控制 P99。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合M/M/1排队论P99延迟推导，ρ>0.8时延迟非线性增长符合排队论基本规律，工程阈值设定合理。
