# N157: 信任积累速率 λ 的计算公式：λ 并非常数，而是与买家在该品类下的历史交易频次 F_history 呈对数关系，λ = λ_base * log(1 + F_h

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

信任积累速率 λ 的计算公式：λ 并非常数，而是与买家在该品类下的历史交易频次 F_history 呈对数关系，λ = λ_base * log(1 + F_history)，其中 λ_base 需通过时间序列数据拟合确定。

## Corrected Claim

信任积累速率 λ 的计算公式：λ 并非常数，而是与买家在该品类下的历史交易频次 F_history 呈对数关系，λ = λ_base * log(1 + F_history)，其中 λ_base 需通过时间序列数据拟合确定。

## Evidence

先验知识/题面给定，逻辑校验通过
