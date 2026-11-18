# N180: LRU 命中率波动幅度的一阶近似：ΔH_LRU ≈ -B * (1 - H_steady) * (T_burst / T_res_avg)，其中 T_res_a

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

LRU 命中率波动幅度的一阶近似：ΔH_LRU ≈ -B * (1 - H_steady) * (T_burst / T_res_avg)，其中 T_res_avg 为平均驻留时间，负号表示命中率下降，该公式假设突发期间缓存被新对象冲刷。

## Corrected Claim

LRU 命中率波动幅度的一阶近似：ΔH_LRU ≈ -B * (1 - H_steady) * (T_burst / T_res_avg)，其中 T_res_avg 为平均驻留时间，负号表示命中率下降，该公式假设突发期间缓存被新对象冲刷。

## Evidence

先验知识/题面给定，逻辑校验通过
