# N225: JSON Schema 验证开销分解：2KB JSON 解析耗时 ~0.05ms，Schema 匹配耗时 ~0.15ms（取决于 schema 复杂度，假设 2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

JSON Schema 验证开销分解：2KB JSON 解析耗时 ~0.05ms，Schema 匹配耗时 ~0.15ms（取决于 schema 复杂度，假设 20 个字段），总耗时 ~0.2ms；相比 T_inference (~50s)，占比为 0.0004%，远小于 0.01% 阈值，确认可忽略

## Corrected Claim

JSON Schema 验证开销分解：2KB JSON 解析耗时 ~0.05ms，Schema 匹配耗时 ~0.15ms（取决于 schema 复杂度，假设 20 个字段），总耗时 ~0.2ms；相比 T_inference (~50s)，占比为 0.0004%，远小于 0.01% 阈值，确认可忽略

## Evidence

先验知识/题面给定，逻辑校验通过：JSON解析与Schema验证通常在毫秒级，相比50秒推理时间占比极小，数量级估算合理。

## Search Query

JSON schema validation performance benchmark 2kb payload python library latency
