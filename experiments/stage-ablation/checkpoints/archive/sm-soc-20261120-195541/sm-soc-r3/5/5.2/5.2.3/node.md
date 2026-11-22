# N168: 公式 P_match = exp(-σ²) 在 σ > 0.5 时失效，因为此时 P_match < 0.778，未考虑多轮匹配尝试（重试机制）；修正公式应引入

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

公式 P_match = exp(-σ²) 在 σ > 0.5 时失效，因为此时 P_match < 0.778，未考虑多轮匹配尝试（重试机制）；修正公式应引入尝试次数 N_attempts，P_match_corrected = 1 - (1 - exp(-σ²))^N_attempts，需通过平台数据校准 N_attempts 的分布（假设平均 N_attempts = 3）。

## Corrected Claim

公式 P_match = exp(-σ²) 在考虑多轮匹配尝试时需修正为 P_match_corrected = 1 - (1 - exp(-σ²))^N_attempts，其中 N_attempts 需根据平台实际重试策略校准（例如假设平均为 3 次）。

## Evidence

[质询]该陈述包含具体的工程参数假设（如平均尝试次数 N_attempts = 3）和特定的失效阈值（σ > 0.5），这些属于经验事实或特定系统配置，无法从第一性原理严格推导，且缺乏外部来源支持其具体数值。 | 逻辑自洽：修正公式 P = 1 - (1-p)^N 在数学上正确描述了独立重试机制下的累积成功率；但 N_attempts=3 为经验假设，无来源支持，故降级。
