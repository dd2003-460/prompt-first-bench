# N153: Apple Mac Studio (M2 Ultra, 192GB) 在 24/7 运行 LLM 推理时的平均功耗 P_avg_MacStudio 约为 150

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N48

## Claim

Apple Mac Studio (M2 Ultra, 192GB) 在 24/7 运行 LLM 推理时的平均功耗 P_avg_MacStudio 约为 150-200W (介于 Idle 100W 与 Peak 250W 之间，取决于上下文长度与 Batch Size)，而非简单的峰值 250W，需根据 Qwen3-27B 32K 上下文的具体负载曲线进行加权平均计算。

## Corrected Claim

Apple Mac Studio (M2 Ultra, 192GB) 在 24/7 运行 LLM 推理时的平均功耗 P_avg_MacStudio 预计介于空闲功耗与峰值功耗之间，具体数值需根据 Qwen3-27B 32K 上下文的具体负载曲线进行加权平均计算，而非简单取峰值。

## Evidence

[质询]该陈述包含具体的硬件功耗数值（Idle 100W, Peak 250W, Avg 150-200W），属于经验事实。由于检索失败，无法验证这些具体数值是否准确对应 M2 Ultra Mac Studio 在特定 LLM 负载下的实际表现，且不同上下文长度和 Batch Size 对功耗的影响曲线缺乏数据支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Apple Mac Studio M2 Ultra power consumption LLM inference average watts 24/7
