# N310: 95th Percentile计费月成本 C_95th = P_95th_unit * B_95th，其中 B_95th 为月内95分位带宽值，对于突发型负载 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N99

## Claim

95th Percentile计费月成本 C_95th = P_95th_unit * B_95th，其中 B_95th 为月内95分位带宽值，对于突发型负载 B_95th ≈ B_avg * 1.5-2.0，P_95th_unit 通常比固定带宽单价高 10-20% 但总成本更低

## Corrected Claim

95th Percentile计费月成本 C_95th = P_95th_unit * B_95th，其中 B_95th 为月内95分位带宽值，对于突发型负载 B_95th ≈ B_avg * 1.5-2.0，P_95th_unit 通常比固定带宽单价高 10-20% 但总成本更低

## Evidence

先验知识/题面给定，逻辑校验通过
