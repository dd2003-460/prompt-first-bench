# N214: 工作点 B（中精度中成本）：使用本地 27B 模型进行原子事实抽取，Prompt 工程优化后 F1 分数为 0.85，单次抽取耗时 5s（约 500 token

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

工作点 B（中精度中成本）：使用本地 27B 模型进行原子事实抽取，Prompt 工程优化后 F1 分数为 0.85，单次抽取耗时 5s（约 500 tokens），成本约为 0.0035 元，存在自一致性偏差风险。

## Corrected Claim

工作点 B（中精度中成本）：使用本地 27B 模型进行原子事实抽取，Prompt 工程优化后 F1 分数为 0.85，单次抽取耗时 5s（约 500 tokens），成本约为 0.0035 元，存在自一致性偏差风险。

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型本地部署推理5秒处理500 tokens符合硬件性能预期，成本估算基于电力/折旧分摊合理，F1 0.85在优化后属正常范围，自一致性偏差是LLM已知特性。
