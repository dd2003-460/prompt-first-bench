# N71: 批处理效率损失量化：vLLM连续批处理中，新序列加入时的preemption与swap开销约50-100ms/序列，5次refinement中若发生2次pree

- **status**: degraded
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

[质询]数值量级缺乏通用基准支持：50-100ms/序列的preemption开销在不同硬件（GPU型号）、内存带宽及vLLM版本间波动极大，且通常取决于KV Cache大小，将其作为固定经验值缺乏普适性；此外，0.2-0.4%的占比依赖于总延迟的具体假设（如总延迟需达到50s以上才符合此比例），未明确上下文导致比例计算可能失真。 | source=knowledge，逻辑自洽（100-200ms绝对值与0.2-0.4%相对值在长推理场景下数量级兼容），但具体毫秒数属于经验参数，无外部来源直接支持，依据经验事实排除条款降级。
