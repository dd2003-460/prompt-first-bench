# N191: 对于北京-上海链路（有效距离~1400km），单向传输延迟 T_one_way = Distance / v_fiber ≈ 1400km / 200,000k

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

对于北京-上海链路（有效距离~1400km），单向传输延迟 T_one_way = Distance / v_fiber ≈ 1400km / 200,000km/s ≈ 7ms，因此理论最小RTT_to_origin ≈ 2 × 7ms = 14ms。

## Corrected Claim

对于北京-上海链路（有效距离~1400km），单向传输延迟 T_one_way = Distance / v_fiber ≈ 1400km / 200,000km/s ≈ 7ms，因此理论最小RTT_to_origin ≈ 2 × 7ms = 14ms。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别代表了理想物理极限、典型实际场景和最坏情况，三者基于不同的距离系数和光纤折射率假设，逻辑上互斥且共同构成了从下限到上限的完整覆盖范围，不存在重复或矛盾。）
