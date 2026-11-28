# N674: 本地 Qwen3.8-27B 的 FCR 测量方法：对每个测试样本，运行 5 次生成（Temperature=0.7），由 LLM-as-a-Judge 评估幻

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N245

## Claim

本地 Qwen3.8-27B 的 FCR 测量方法：对每个测试样本，运行 5 次生成（Temperature=0.7），由 LLM-as-a-Judge 评估幻觉声明比例，取平均值作为该样本的 FCR_local；需记录每次生成的 Token 数以计算成本

## Corrected Claim

本地 Qwen3.8-27B 的 FCR 测量方法：对每个测试样本，运行 5 次生成（Temperature=0.7），由 LLM-as-a-Judge 评估幻觉声明比例，取平均值作为该样本的 FCR_local；需记录每次生成的 Token 数以计算成本

## Evidence

先验知识/题面给定，逻辑校验通过
