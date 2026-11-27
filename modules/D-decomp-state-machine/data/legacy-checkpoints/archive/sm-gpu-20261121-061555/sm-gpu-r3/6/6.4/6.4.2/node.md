# N121: 针对 Qwen3-27B 量化后质量损失（PPL 增量）的数据冲突处理规则：若不同评测集（WikiText vs C4）得出的 PPL 增量差异 >0.5，则需

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

针对 Qwen3-27B 量化后质量损失（PPL 增量）的数据冲突处理规则：若不同评测集（WikiText vs C4）得出的 PPL 增量差异 >0.5，则需检查评测集长度和截断策略；若仍冲突，采用对决策更保守（即认为损失更大）的数值作为安全边界，并在最终报告中注明 [数据冲突-需人工裁决]。

## Corrected Claim

针对 Qwen3-27B 量化后质量损失（PPL 增量）的数据冲突处理规则：若不同评测集（WikiText vs C4）得出的 PPL 增量差异 >0.5，则需检查评测集长度和截断策略；若仍冲突，采用对决策更保守（即认为损失更大）的数值作为安全边界，并在最终报告中注明 [数据冲突-需人工裁决]。

## Evidence

先验知识/题面给定，逻辑校验通过
