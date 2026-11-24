# N223: 核心区域工作点（70%用户）：距离 d<100km，根据 RTT=0.05*d+5，RTT<10ms；考虑跨网惩罚 ΔT_cross≈15ms，P99_RTT_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

核心区域工作点（70%用户）：距离 d<100km，根据 RTT=0.05*d+5，RTT<10ms；考虑跨网惩罚 ΔT_cross≈15ms，P99_RTT_core ≈ 25ms

## Corrected Claim

核心区域工作点（70%用户）：距离 d<100km，根据 RTT=0.05*d+5，RTT<10ms；考虑跨网惩罚 ΔT_cross≈15ms，P99_RTT_core ≈ 25ms

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别针对距离分布、跨网惩罚构成、修正公式三个不同维度进行分解，逻辑清晰且互不重叠；覆盖了父节点中所有关键参数（距离、跨网惩罚、抖动）及最终结果的修正，完备性良好；各子节点描述的是独立的物理量或计算步骤，不存在冗余。）
