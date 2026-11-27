# N143: 量化 LFU 在 ρ=-0.3 下的劣势工作点 2（冷大对象污染）：若 LFU 未能有效老化低频大对象（假设冷对象访问频率极低但驻留时间长），其驱逐错误率 ε_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N46

## Claim

量化 LFU 在 ρ=-0.3 下的劣势工作点 2（冷大对象污染）：若 LFU 未能有效老化低频大对象（假设冷对象访问频率极低但驻留时间长），其驱逐错误率 ε_LFU 可能高于 LRU。在此工作点，ΔH_ρ 为负值。具体量化为：若 LFU 缓存中 5% 的空间被低频大对象占据，则 ΔH_ρ ≈ -0.05 * (S_cold_avg / S_hot_avg) * H_base，估算损失约为 0.2-0.8 个百分点。

## Corrected Claim

量化 LFU 在 ρ=-0.3 下的劣势工作点（冷大对象污染）：若 LFU 未能有效老化低频大对象，其驱逐错误率 ε_LFU 可能高于 LRU，导致 ΔH_ρ 为负值。具体损失幅度取决于冷/热对象的大小比及占比，需通过具体负载模拟确定。

## Evidence

[质询]该陈述包含具体的经验性量化估算（如'5%空间'对应'0.2-0.8个百分点'的损失），这属于特定缓存场景下的经验事实或模拟结果，无法从第一性原理严格推导得出，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

LFU pollution penalty large objects low frequency cache eviction error
