# N266: 数据中心级 GPU 的故障分布不服从简单的指数分布 (恒定故障率)，而是包含早期失效 (Infant Mortality) 期 (前 6 个月故障率较高，约为稳

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77

## Claim

数据中心级 GPU 的故障分布不服从简单的指数分布 (恒定故障率)，而是包含早期失效 (Infant Mortality) 期 (前 6 个月故障率较高，约为稳态期的 2-3 倍) 和耗损失效期 (5 年后故障率上升)；在 3 年 TCO 计算中，若忽略早期失效，P_fail 会被低估约 1-2 个百分点，需使用威布尔分布 (Weibull Distribution) 参数 (η, β) 进行更精确的概率积分。

## Corrected Claim

数据中心级 GPU 的故障分布不服从简单的指数分布 (恒定故障率)，而是包含早期失效 (Infant Mortality) 期 (前 6 个月故障率较高，约为稳态期的 2-3 倍) 和耗损失效期 (5 年后故障率上升)；在 3 年 TCO 计算中，若忽略早期失效，P_fail 会被低估约 1-2 个百分点，需使用威布尔分布 (Weibull Distribution) 参数 (η, β) 进行更精确的概率积分。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GPU failure rate Weibull distribution infant mortality data center hardware reliability
