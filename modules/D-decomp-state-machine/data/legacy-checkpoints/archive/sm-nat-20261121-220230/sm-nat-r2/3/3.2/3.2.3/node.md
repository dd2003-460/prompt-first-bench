# N60: 对于中热度对象（50 < λ_i < 1000 req/day），T_resident ≈ 1.5 天。计算：该区间对象在 LRU 队列中处于中间位置，驻留时间

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

对于中热度对象（50 < λ_i < 1000 req/day），T_resident ≈ 1.5 天。计算：该区间对象在 LRU 队列中处于中间位置，驻留时间受相邻对象访问频率影响，近似为 T_resident ≈ 1 / (λ_i * P_collision)，其中 P_collision 为与其他对象竞争驱逐的概率，在 128GB 缓存和 10 万对象规模下，P_collision ≈ 0.2，故 T_resident ≈ 1.5 天，P_invalid ≈ 1.5%。

## Corrected Claim

对于中热度对象（50 < λ_i < 1000 req/day），T_resident ≈ 1.5 天（基于 P_collision ≈ 0.2 的估算），P_invalid 需根据具体失效模型计算，不能直接等同于 1.5%。

## Evidence

[质询]数值推导存在内部矛盾：若 T_resident ≈ 1.5 天，则 P_invalid ≈ 1.5% 缺乏明确的计算依据（通常失效概率与驻留时间成反比或取决于具体失效模型，此处直接等同数值缺乏逻辑支撑）；且 P_collision ≈ 0.2 为经验估算值，未提供推导过程，属于经验事实而非第一性原理可严格推出的结论。 | 经验事实，逻辑自洽但缺来源支持；P_invalid 与 T_resident 的数值对应关系缺乏明确逻辑推导，且 P_collision 为估算值，无法从第一性原理严格推出。

## Search Query

LRU resident time medium frequency objects collision probability cache
