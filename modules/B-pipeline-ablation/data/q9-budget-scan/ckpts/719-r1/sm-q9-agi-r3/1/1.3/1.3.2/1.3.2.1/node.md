# N135: TruthfulQA 基准上的幻觉率 Hallucination_Rate 定义为：(Untruthful Answers Count) / (Total Qu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

TruthfulQA 基准上的幻觉率 Hallucination_Rate 定义为：(Untruthful Answers Count) / (Total Questions)，其中 Untruthful 判定需同时满足：(1) 答案与 Ground Truth 事实冲突，(2) 非拒答（Refusal），需使用官方评测脚本自动比对

## Corrected Claim

TruthfulQA 基准上的幻觉率 Hallucination_Rate 定义为：(Untruthful Answers Count) / (Total Questions)，其中 Untruthful 判定需同时满足：(1) 答案与 Ground Truth 事实冲突，(2) 非拒答（Refusal），需使用官方评测脚本自动比对

## Evidence

先验知识/题面给定，逻辑校验通过
