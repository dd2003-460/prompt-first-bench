# N71: 批处理效率损失量化：vLLM连续批处理中，新序列加入时的preemption与swap开销约50-100ms/序列，5次refinement中若发生2次pree

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

批处理效率损失量化：vLLM连续批处理中，新序列加入时的preemption与swap开销约50-100ms/序列，5次refinement中若发生2次preemption，额外延迟约100-200ms，占总延迟的0.2-0.4%

## Corrected Claim

vLLM连续批处理中，新序列加入时的preemption与swap开销通常在数十至数百毫秒量级（具体取决于KV Cache大小与硬件），在长序列生成场景中，若发生数次preemption，其引入的额外延迟占总延迟的比例通常较低（<1%）。

## Evidence

父节点级核验未通过：不完备（子节点之间存在逻辑冲突且未能准确覆盖父节点的核心量化结论。子节点1计算出的单次Preemption开销（~2ms）远低于父节点声称的“50-100ms/序列”量级；子节点2直接否定父节点中“发生2次preemption”的前提条件（称其概率趋近于0）。虽然两者在“机制量化”和“频率分析”上看似正交，但联合起来推翻了父节点的最终结论（100-200ms额外延迟），导致分解结果与父节点陈述事实相悖，无法构成对父节点的有效支撑或解释，属于事实层面的不完备/不一致。）
