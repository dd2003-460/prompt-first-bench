# N217: 当引入瞬时突发负载（如 Poisson 到达率 λ(t) 随时间波动，CV=0.5）时，LRU 流体模型命中率公式的误差从稳态的 1.2% 上升至 7.5%，表

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N75, N76, N77

## Claim

当引入瞬时突发负载（如 Poisson 到达率 λ(t) 随时间波动，CV=0.5）时，LRU 流体模型命中率公式的误差从稳态的 1.2% 上升至 7.5%，表明该公式在突发场景下失效

## Corrected Claim

当引入瞬时突发负载（如 Poisson 到达率随时间波动）时，LRU 流体模型命中率公式的误差通常较稳态情况显著上升，表明该公式在突发场景下的适用性受限。

## Evidence

[质询]该陈述包含具体的经验数值（稳态误差1.2%、突发误差7.5%、CV=0.5），属于特定实验或模拟结果，无法从第一性原理直接推导，且缺乏来源支持其具体数值的准确性。 | 经验事实，逻辑自洽（突发负载通常导致缓存命中率下降及模型误差增大）但缺来源支持具体数值。

## Search Query

LRU cache hit rate bursty workload fluid model error
