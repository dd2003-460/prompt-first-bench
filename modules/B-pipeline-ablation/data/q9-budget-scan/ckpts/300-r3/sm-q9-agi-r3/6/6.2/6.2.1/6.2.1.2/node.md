# N298: 低接受率工作点（AR≈0.3-0.5）：在开放域推理任务中，频繁回滚导致验证开销占比激增，加速比Speedup_low ≈ 1.2-1.5，甚至可能低于1.0（

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

低接受率工作点（AR≈0.3-0.5）：在开放域推理任务中，频繁回滚导致验证开销占比激增，加速比Speedup_low ≈ 1.2-1.5，甚至可能低于1.0（负加速）

## Corrected Claim

低接受率工作点（AR≈0.3-0.5）：在开放域推理任务中，频繁回滚导致验证开销占比激增，加速比Speedup_low ≈ 1.2-1.5，甚至可能低于1.0（负加速）

## Evidence

先验知识/题面给定，逻辑校验通过：低接受率意味着高频率的回滚操作，每次回滚需重新计算或验证状态，导致验证开销显著增加，从而抵消并行加速收益，符合系统性能分析的基本逻辑。

## Search Query

speculative decoding negative speedup low acceptance rate open domain
