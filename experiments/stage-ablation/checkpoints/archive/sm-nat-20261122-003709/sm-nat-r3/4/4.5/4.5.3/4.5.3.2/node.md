# N209: 在λ=0.01/day且T_res≈10天的中等更新率工作点下，ε_LFU由频率计数器老化滞后主导，其值约为 λ*T_res * k_lfu（k_lfu≈0.5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N72

## Claim

在λ=0.01/day且T_res≈10天的中等更新率工作点下，ε_LFU由频率计数器老化滞后主导，其值约为 λ*T_res * k_lfu（k_lfu≈0.5），计算得ε_LFU≈0.05，此时ΔH_LFU = ε_LRU - ε_LFU = 0.03 - 0.05 = -0.02，表明LFU性能反而劣于LRU 2个百分点。

## Corrected Claim

在λ=0.01/day且T_res≈10天的中等更新率工作点下，ε_LFU由频率计数器老化滞后主导，其值约为 λ*T_res * k_lfu（k_lfu≈0.5），计算得ε_LFU≈0.05，此时ΔH_LFU = ε_LRU - ε_LFU = 0.03 - 0.05 = -0.02，表明LFU性能反而劣于LRU 2个百分点。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 0.01*10*0.5=0.05 及 0.03-0.05=-0.02 准确无误，符合 LFU 在中等更新率下因计数器老化滞后导致性能劣于 LRU 的理论预期。
