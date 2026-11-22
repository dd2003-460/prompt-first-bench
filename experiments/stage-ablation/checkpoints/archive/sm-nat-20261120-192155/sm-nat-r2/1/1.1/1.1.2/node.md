# N22: 分母计算项：全量对象U的总字节流量 Σ_{i∈U} r_i * s_i = (5000万/天) * E[s_i]，其中E[s_i]需通过Pareto(α=1.1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

分母计算项：全量对象U的总字节流量 Σ_{i∈U} r_i * s_i = (5000万/天) * E[s_i]，其中E[s_i]需通过Pareto(α=1.1)分布的截断期望计算，即 E[s_i] = (∫_{s_min}^{s_max} s * f(s) ds) / (∫_{s_min}^{s_max} f(s) ds)

## Corrected Claim

分母计算项：全量对象U的总字节流量 Σ_{i∈U} r_i * s_i = (5000万/天) * E[s_i]，其中E[s_i]需通过Pareto(α=1.1)分布的截断期望计算，即 E[s_i] = (∫_{s_min}^{s_max} s * f(s) ds) / (∫_{s_min}^{s_max} f(s) ds)

## Evidence

先验知识/题面给定，逻辑校验通过：总流量等于对象数量乘以平均大小，且截断期望的积分定义在数学上正确。
