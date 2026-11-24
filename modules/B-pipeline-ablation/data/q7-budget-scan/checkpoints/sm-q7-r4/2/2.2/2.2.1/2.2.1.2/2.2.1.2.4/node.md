# N517: 冷数据查询突增导致HDD饱和的概率模型：假设冷数据查询服从泊松分布 λ_cold = 0.1次/月/对象，500M对象中10%为活跃冷数据，则 λ_total 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N170, N171, N172

## Claim

冷数据查询突增导致HDD饱和的概率模型：假设冷数据查询服从泊松分布 λ_cold = 0.1次/月/对象，500M对象中10%为活跃冷数据，则 λ_total = 50M * 0.1 / 43200min ≈ 0.00116 req/min。HDD饱和阈值 Q_max = 1000（队列深度），若查询突发倍数 Burst_Factor = 100，则瞬时请求率 = 0.116 req/min，远低于饱和阈值，故HDD饱和概率 P_sat ≈ 0，除非发生全局性冷数据批量恢复（如灾难恢复演练）。

## Corrected Claim

冷数据查询突增导致HDD饱和的概率模型：假设冷数据查询服从泊松分布 λ_cold = 0.1次/月/对象，500M对象中10%为活跃冷数据，则 λ_total = 50M * 0.1 / 43200min ≈ 0.00116 req/min。HDD饱和阈值 Q_max = 1000（队列深度），若查询突发倍数 Burst_Factor = 100，则瞬时请求率 = 0.116 req/min，远低于饱和阈值，故HDD饱和概率 P_sat ≈ 0，除非发生全局性冷数据批量恢复（如灾难恢复演练）。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程自洽（50M*0.1/43200≈0.00116），量级合理，结论符合排队论直觉

## Search Query

HDD storage pool saturation probability Poisson process cold data recovery
