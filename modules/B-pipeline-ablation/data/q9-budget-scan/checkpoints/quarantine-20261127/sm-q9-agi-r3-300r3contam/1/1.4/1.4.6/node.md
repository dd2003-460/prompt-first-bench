# N43: 假设生成器Agent的触发条件量化定义：当上一轮Self-Critique拦截率IR(K) < 0.3且剩余预算B_remain > 50%时启动；输入Sche

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10, N11, N12

## Claim

假设生成器Agent的触发条件量化定义：当上一轮Self-Critique拦截率IR(K) < 0.3且剩余预算B_remain > 50%时启动；输入Schema为{context_vector, previous_hypotheses[], confidence_scores[]}，输出为Top-3候选假设列表，终止条件为生成假设通过置信度阈值τ_gen > 0.8。

## Corrected Claim

假设生成器Agent的触发条件量化定义：当上一轮Self-Critique拦截率IR(K) < 0.3且剩余预算B_remain > 50%时启动；输入Schema为{context_vector, previous_hypotheses[], confidence_scores[]}，输出为Top-3候选假设列表，终止条件为生成假设通过置信度阈值τ_gen > 0.8。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

multi-agent system hypothesis generator trigger condition schema
