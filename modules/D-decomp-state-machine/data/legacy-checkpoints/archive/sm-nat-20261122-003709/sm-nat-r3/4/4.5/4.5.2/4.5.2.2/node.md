# N207: 在‘低老化/低更新率’工作点下，ε_LFU ≈ 0，条件为 λ_update * T_resident < 0.01，此时LFU的频率计数器在对象生命周期内充分

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

在‘低老化/低更新率’工作点下，ε_LFU ≈ 0，条件为 λ_update * T_resident < 0.01，此时LFU的频率计数器在对象生命周期内充分收敛，LFU性能接近Optimal，且优于LRU（因为能抵抗突发噪声）。

## Corrected Claim

在‘低老化/低更新率’工作点下，ε_LFU ≈ 0，条件为 λ_update * T_resident < 0.01，此时LFU的频率计数器在对象生命周期内充分收敛，LFU性能接近Optimal，且优于LRU（因为能抵抗突发噪声）。

## Evidence

先验知识/题面给定，逻辑校验通过：在低更新率（λ_update * T_resident < 0.01）下，对象驻留时间远大于更新间隔，LFU计数器有足够时间收敛至真实访问频率，从而区分热点与噪声，性能接近Optimal且优于LRU，符合缓存替换算法理论。
