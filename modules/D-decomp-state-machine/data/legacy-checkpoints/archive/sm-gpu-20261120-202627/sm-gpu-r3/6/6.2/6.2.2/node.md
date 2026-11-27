# N129: NVIDIA A100 80GB 和 L40S 在持续 LLM 推理负载下的平均功耗（P_avg）实测值：A100 TDP 400W，L40S TDP 350W

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N29

## Claim

NVIDIA A100 80GB 和 L40S 在持续 LLM 推理负载下的平均功耗（P_avg）实测值：A100 TDP 400W，L40S TDP 350W，需获取其实际稳态推理功耗数据以计算能效比（Tokens/Joule）和 OpEx_energy。

## Corrected Claim

NVIDIA A100 80GB 的 TDP 为 400W，L40S 的 TDP 为 350W；在持续 LLM 推理负载下，其实际平均功耗（P_avg）通常低于 TDP，需获取具体实测数据以准确计算能效比（Tokens/Joule）和 OpEx_energy。

## Evidence

[质询]该陈述将 TDP（热设计功耗，峰值/上限指标）与“持续 LLM 推理负载下的平均功耗（P_avg）实测值”混为一谈。TDP 不等于实际稳态推理功耗，实际功耗通常低于 TDP 且随负载波动，直接引用 TDP 作为 P_avg 会导致能效比计算偏差。 | 经验事实，逻辑自洽但缺来源支持；TDP 数值（A100 400W, L40S 350W）符合公开规格，但无法从第一性原理推出实际稳态推理功耗，且无外部来源支持具体 P_avg 实测值。

## Search Query

NVIDIA A100 L40S average power consumption LLM inference benchmark watts
