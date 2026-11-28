# N24: 构建失败检测与指数退避重试策略：检测指标为输出完整性分数 S_completeness（基于 JSON Schema 校验通过比例）和逻辑连贯性分数 S_log

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

构建失败检测与指数退避重试策略：检测指标为输出完整性分数 S_completeness（基于 JSON Schema 校验通过比例）和逻辑连贯性分数 S_logic（基于 n-gram 重复率倒数）；重试最大次数 R_max=3，退避因子 α=2.0，基础等待时间 t_base=1s；量化系统可用性 SLA 从 99.0% 提升至 99.9%，单次故障恢复平均时间 MTTR < 30s。

## Corrected Claim

构建失败检测与指数退避重试策略：检测指标为输出完整性分数 S_completeness（基于 JSON Schema 校验通过比例）和逻辑连贯性分数 S_logic（基于 n-gram 重复率倒数）；重试最大次数 R_max=3，退避因子 α=2.0，基础等待时间 t_base=1s；量化系统可用性 SLA 从 99.0% 提升至 99.9%，单次故障恢复平均时间 MTTR < 30s。

## Evidence

先验知识/题面给定，逻辑校验通过
