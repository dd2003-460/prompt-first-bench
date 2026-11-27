# N80: LFU 相比 LRU 的提升幅度 ΔH 的精确数值推导：在 LRU 命中率接近 100% 的情况下，LFU 的理论上限 H_byte_LFU_max 也接近 1

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26

## Claim

LFU 相比 LRU 的提升幅度 ΔH 的精确数值推导：在 LRU 命中率接近 100% 的情况下，LFU 的理论上限 H_byte_LFU_max 也接近 100%，因此 ΔH = H_byte_LFU - H_byte_LRU ≈ 0；但考虑到 LFU 在长尾负载下的频率统计滞后，实际提升幅度可能为负（即 LFU 略低于 LRU），量化为 ΔH ≈ -0.1% 至 -0.5%，具体取决于更新率和热度分布的动态变化。

## Corrected Claim

在LRU命中率接近100%的特定稳定负载下，LFU相比LRU的提升幅度ΔH通常接近0，可能因频率统计滞后出现微小负值，但具体数值高度依赖负载动态特性，无统一固定区间。

## Evidence

[质询]该陈述将‘LRU命中率接近100%’这一极端理想化场景作为推导前提，并据此得出LFU提升幅度为负（-0.1%至-0.5%）的精确量化结论。然而，在LRU命中率接近100%的稳态下，工作集通常非常稳定，LFU的频率统计滞后效应极小，甚至可能因LFU更好地识别热点而持平或略优，断言其必然为负且给出具体负值区间缺乏普适性理论支持，属于过度具体的经验性断言。 | 经验事实，逻辑自洽但缺来源支持；检索无可用来源，且该具体数值区间（-0.1%至-0.5%）无法从第一性原理严格推出，属于特定负载下的经验观察，故降级。

## Search Query

LFU vs LRU cache hit rate difference Pareto beta 0.9 negative correlation size heat 1% update rate
