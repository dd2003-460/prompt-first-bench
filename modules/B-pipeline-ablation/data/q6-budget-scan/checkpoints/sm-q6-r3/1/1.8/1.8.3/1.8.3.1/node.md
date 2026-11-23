# N146: Miller-Muntz 模型的适用条件与参数：该模型假设请求间隔服从指数分布，适用于稳态、无时间局部性突变的场景；其命中率公式 H = 1 - (lambda

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

Miller-Muntz 模型的适用条件与参数：该模型假设请求间隔服从指数分布，适用于稳态、无时间局部性突变的场景；其命中率公式 H = 1 - (lambda * s_avg) / C 仅当 lambda（单位时间请求率）* s_avg < C 时有效；若 lambda * s_avg >= C，则模型预测 H=0，但实际上 LRU 仍有一定命中率，因此该模型在高频短尾场景下会低估 H，需引入修正因子。

## Corrected Claim

Miller-Muntz 模型的适用条件与参数：该模型假设请求间隔服从指数分布，适用于稳态、无时间局部性突变的场景；其命中率公式 H = 1 - (lambda * s_avg) / C 仅当 lambda（单位时间请求率）* s_avg < C 时有效；若 lambda * s_avg >= C，则模型预测 H=0，但实际上 LRU 仍有一定命中率，因此该模型在高频短尾场景下会低估 H，需引入修正因子。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Miller-Muntz model cache hit rate limitations exponential interarrival
