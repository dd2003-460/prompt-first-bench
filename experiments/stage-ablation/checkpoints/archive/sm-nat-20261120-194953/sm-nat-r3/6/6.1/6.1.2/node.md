# N148: 瞬时命中率损失 $\Delta H_{burst}$ 的解析表达式为 $\Delta H_{burst} = \frac{\sum_{j \in Evicted

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N69

## Claim

瞬时命中率损失 $\Delta H_{burst}$ 的解析表达式为 $\Delta H_{burst} = \frac{\sum_{j \in Evicted} R_j S_j}{\sum_{i=1}^{N} R_i S_i}$。在全量驻留且突发请求完全替换热点的情况下，若驱逐的前 $K_{evict}$ 个对象贡献了 $P_{head}$ 的总请求字节量，则 $\Delta H_{burst} \approx P_{head} \times (1 - H_{cold})$，其中 $H_{cold}$ 为冷对象命中率。由于冷对象热度极低，$H_{cold} \approx 0$，故 $\Delta H_{burst} \approx P_{head}$。对于 Pareto(0.9)，前 10% 对象贡献 68.1% 请求，若 $K_{evict}$ 覆盖前 10%，损失高达 68.1%。

## Corrected Claim

瞬时命中率损失 $\Delta H_{burst}$ 的解析表达式为 $\Delta H_{burst} = \frac{\sum_{j \in Evicted} R_j S_j}{\sum_{i=1}^{N} R_i S_i}$。在全量驻留且突发请求完全替换热点的情况下，若驱逐的前 $K_{evict}$ 个对象贡献了 $P_{head}$ 的总请求字节量，则 $\Delta H_{burst} \approx P_{head} \times (1 - H_{cold})$，其中 $H_{cold}$ 为冷对象命中率。由于冷对象热度极低，$H_{cold} \approx 0$，故 $\Delta H_{burst} \approx P_{head}$。对于 Pareto(0.9)，前 10% 对象贡献 68.1% 请求，若 $K_{evict}$ 覆盖前 10%，损失高达 68.1%。

## Evidence

先验知识/题面给定，逻辑校验通过
