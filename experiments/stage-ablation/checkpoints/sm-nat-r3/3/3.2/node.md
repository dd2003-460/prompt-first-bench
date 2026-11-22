# N16: LFU 相对 LRU 的提升幅度：ΔH = H_byte_LFU - H_byte_LRU，需计算两者在相同容量下的命中率差异，并分析负相关 (ρ≈-0.3) 

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LFU 相对 LRU 的提升幅度：ΔH = H_byte_LFU - H_byte_LRU，需计算两者在相同容量下的命中率差异，并分析负相关 (ρ≈-0.3) 对 ΔH 的影响机制。

## Corrected Claim

LFU 相对 LRU 的提升幅度：ΔH = H_byte_LFU - H_byte_LRU，需计算两者在相同容量下的命中率差异，并分析负相关 (ρ≈-0.3) 对 ΔH 的影响机制。

## Evidence

父节点级核验未通过：不完备（子节点1仅提供了ΔH的代数定义，未包含父节点要求的'在相同容量下'这一关键约束条件的数学表达或验证；子节点2提供了机制解释和辅助量化指标，但缺乏对'负相关如何具体导致命中率差异'的严格数学推导或公式化关联，导致父节点中'分析...影响机制'这一核心任务在量化层面覆盖不全。）
