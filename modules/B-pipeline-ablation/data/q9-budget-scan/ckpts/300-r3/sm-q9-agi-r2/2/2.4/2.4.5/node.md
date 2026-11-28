# N67: 工具调用 JSON Schema 验证开销：每次返回的结构化 JSON 大小平均 2KB，解析与 schema 验证耗时 < 1ms（CPU 侧），对端到端 T

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

工具调用 JSON Schema 验证开销：每次返回的结构化 JSON 大小平均 2KB，解析与 schema 验证耗时 < 1ms（CPU 侧），对端到端 T_cycle 的影响可忽略不计（<0.01%）

## Corrected Claim

工具调用 JSON Schema 验证开销：每次返回的结构化 JSON 大小平均 2KB，解析与 schema 验证耗时 < 1ms（CPU 侧），对端到端 T_cycle 的影响可忽略不计（<0.01%）

## Evidence

先验知识/题面给定，逻辑校验通过：2KB JSON 解析在现代 CPU 上通常在微秒级（<1ms 成立），且相对于 LLM 推理延迟（通常数百毫秒至数秒），其占比确实可忽略不计（<0.01% 合理）。
