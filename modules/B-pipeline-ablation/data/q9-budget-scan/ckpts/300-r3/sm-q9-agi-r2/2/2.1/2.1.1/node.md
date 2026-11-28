# N51: 量化[Research Question]字段的生成质量：定义模糊度指数 Ambiguity = H(Q) / log(|V|)，其中H为香农熵，要求生成后 A

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

量化[Research Question]字段的生成质量：定义模糊度指数 Ambiguity = H(Q) / log(|V|)，其中H为香农熵，要求生成后 Ambiguity < 0.3 以确保可执行性，否则触发重试

## Corrected Claim

量化[Research Question]字段的生成质量：定义模糊度指数 Ambiguity = H(Q) / log(|V|)，其中H为香农熵，要求生成后 Ambiguity < 0.3 以确保可执行性，否则触发重试

## Evidence

先验知识/题面给定，逻辑校验通过：香农熵归一化定义正确，阈值设定符合信息论中低不确定性（高确定性/可执行性）的工程惯例。
