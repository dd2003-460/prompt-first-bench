# N191: 对于北京-上海链路（有效距离~1400km），单向传输延迟 T_one_way = Distance / v_fiber ≈ 1400km / 200,000k

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N55

## Claim

对于北京-上海链路（有效距离~1400km），单向传输延迟 T_one_way = Distance / v_fiber ≈ 1400km / 200,000km/s ≈ 7ms，因此理论最小RTT_to_origin ≈ 2 × 7ms = 14ms。

## Corrected Claim

对于北京-上海链路（有效距离~1400km），单向传输延迟 T_one_way = Distance / v_fiber ≈ 1400km / 200,000km/s ≈ 7ms，因此理论最小RTT_to_origin ≈ 2 × 7ms = 14ms。

## Evidence

先验知识/题面给定，逻辑校验通过：光速在光纤中约为200,000km/s，1400km距离对应单向延迟7ms，往返14ms，符合物理常识。
