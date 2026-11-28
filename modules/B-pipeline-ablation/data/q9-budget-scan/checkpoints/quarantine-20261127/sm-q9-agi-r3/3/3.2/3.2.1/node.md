# N64: Self-Consistency (SC) 采样 n=5 次的 Token 消耗计算公式为 Total_Tokens = 5 * (Prompt_Tokens 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

Self-Consistency (SC) 采样 n=5 次的 Token 消耗计算公式为 Total_Tokens = 5 * (Prompt_Tokens + Avg_Response_Tokens_per_Sample)。对于 BBH 类任务，Prompt 约 500 tokens，Response 平均 200 tokens，则单次 SC 调用消耗 3500 tokens，相比单次 CoT (700 tokens) 增加 5 倍，而非 N18 声称的 3-5 倍（若含 Prompt 重复则更高）。

## Corrected Claim

Self-Consistency (SC) 采样 n=5 次的 Token 消耗计算公式为 Total_Tokens = 5 * (Prompt_Tokens + Avg_Response_Tokens_per_Sample)。对于 BBH 类任务，Prompt 约 500 tokens，Response 平均 200 tokens，则单次 SC 调用消耗 3500 tokens，相比单次 CoT (700 tokens) 增加 5 倍，而非 N18 声称的 3-5 倍（若含 Prompt 重复则更高）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 Total_Tokens = n * (P + R) 符合 LLM API 计费逻辑；数值计算 5*(500+200)=3500 正确；对比基准 700 (500+200) 正确；倍数 3500/700=5 正确。
