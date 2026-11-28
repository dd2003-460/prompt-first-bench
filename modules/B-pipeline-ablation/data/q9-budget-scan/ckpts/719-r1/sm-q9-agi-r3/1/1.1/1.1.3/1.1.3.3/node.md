# N116: GSM8K 评测中 Chain-of-Thought (CoT) 推理链的平均长度 L_cot ≈ 150 tokens，5-shot 提示占用上下文 800 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

GSM8K 评测中 Chain-of-Thought (CoT) 推理链的平均长度 L_cot ≈ 150 tokens，5-shot 提示占用上下文 800 tokens，单样本总上下文长度 ≈ 1000 tokens，远低于 262k 限制，无截断风险

## Corrected Claim

GSM8K 评测中 Chain-of-Thought (CoT) 推理链的平均长度 L_cot ≈ 150 tokens，5-shot 提示占用上下文 800 tokens，单样本总上下文长度 ≈ 1000 tokens，远低于 262k 限制，无截断风险

## Evidence

先验知识/题面给定，逻辑校验通过：GSM8K 题目简短，CoT 平均长度约 150 tokens 符合常见大模型行为，5-shot 示例占用 800 tokens 及总长 1000 tokens 的量级估算合理，远低于 262k 限制，无截断风险。
