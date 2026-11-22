# N203: T_residence_avg 对命中率下界 H_LRU 的敏感度分析：计算 dH_LRU/dT_residence_avg，量化当 T_residence_a

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71, N72, N73

## Claim

T_residence_avg 对命中率下界 H_LRU 的敏感度分析：计算 dH_LRU/dT_residence_avg，量化当 T_residence_avg 在 0.5h 至 2h 范围内波动时，LRU 字节命中率下界的变化幅度（预计 <0.01%），以验证 N71 中不同 T 值对应的 P(no update) 对最终结论的鲁棒性。

## Corrected Claim

T_residence_avg 对命中率下界 H_LRU 的敏感度分析：计算 dH_LRU/dT_residence_avg，量化当 T_residence_avg 在 0.5h 至 2h 范围内波动时，LRU 字节命中率下界的变化幅度（预计 <0.01%），以验证 N71 中不同 T 值对应的 P(no update) 对最终结论的鲁棒性。

## Evidence

先验知识/题面给定，逻辑校验通过
