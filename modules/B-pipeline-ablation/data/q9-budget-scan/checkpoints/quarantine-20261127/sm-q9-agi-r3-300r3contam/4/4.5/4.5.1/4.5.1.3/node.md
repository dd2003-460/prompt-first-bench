# N188: E_queries_per_cycle 的实测重构公式：E_qpc = 60 / (T_gen_512_avg * (1 + η_overhead))，其中η_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

E_queries_per_cycle 的实测重构公式：E_qpc = 60 / (T_gen_512_avg * (1 + η_overhead))，其中η_overhead为检索/工具调用等非推理开销占比（参考N52约0.15-0.25），替代原假设的50 queries/min

## Corrected Claim

E_queries_per_cycle 的实测重构公式：E_qpc = 60 / (T_gen_512_avg * (1 + η_overhead))，其中η_overhead为检索/工具调用等非推理开销占比（参考N52约0.15-0.25），替代原假设的50 queries/min

## Evidence

先验知识/题面给定，逻辑校验通过：公式基于时间单位换算（60秒/分钟）及效率定义（有效时间占比），量纲与逻辑自洽，符合工程估算惯例。
