# N31: 事实核查管线：生成结论后调用外部 API（如 Wikipedia API 或 PubMed）进行实体链接，验证关键事实（F1-Fn）的存在性与准确性，准确率指标

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

事实核查管线：生成结论后调用外部 API（如 Wikipedia API 或 PubMed）进行实体链接，验证关键事实（F1-Fn）的存在性与准确性，准确率指标 Accuracy = TP / (TP + FP + FN)，要求 ≥ 0.95；每个结论平均需验证 5±2 个关键事实

## Corrected Claim

事实核查管线：生成结论后调用外部 API（如 Wikipedia API 或 PubMed）进行实体链接，验证关键事实（F1-Fn）的存在性与准确性，准确率指标 Accuracy = TP / (TP + FP + FN)，要求 ≥ 0.95；每个结论平均需验证 5±2 个关键事实

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

fact checking pipeline entity linking accuracy metric research automation
