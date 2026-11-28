# N14: 分析环节：LLM 调用模式为 Chain-of-Thought + Verifier (Self-Critique)，需多次迭代（平均 [待核验] 次），对数值

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

分析环节：LLM 调用模式为 Chain-of-Thought + Verifier (Self-Critique)，需多次迭代（平均 [待核验] 次），对数值准确性敏感，主要失败模式是算术错误与统计概念混淆，需外部计算器工具辅助。

## Corrected Claim

分析环节：LLM 调用模式为 Chain-of-Thought + Verifier (Self-Critique)，通常需多次迭代以收敛结果，对数值准确性敏感，常见失败模式包括算术错误与统计概念混淆，建议引入外部计算器工具辅助以提升精度。

## Evidence

[质询]陈述中关于“平均迭代次数”的具体数值缺失（标记为[待核验]），且“主要失败模式”和“需外部计算器”属于经验性观察结论，缺乏普遍适用的定量标准或第一性原理支撑，不同模型和任务场景下差异巨大。 | source=knowledge，逻辑自洽（CoT+Verifier是常见增强模式，算术错误是LLM已知弱点），但具体迭代次数和经验性失败模式分布缺乏统一标准，且无外部来源支持，故降级为定性描述。
