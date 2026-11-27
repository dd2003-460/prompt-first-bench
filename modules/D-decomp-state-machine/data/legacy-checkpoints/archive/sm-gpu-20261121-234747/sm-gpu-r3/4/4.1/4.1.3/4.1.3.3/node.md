# N290: RTX 4090 在运行 Qwen3-27B 推理（Prefill 阶段满载，Decode 阶段中等负载）时的实测平均功耗为 420W ± 10W，数据源为 T

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N103

## Claim

RTX 4090 在运行 Qwen3-27B 推理（Prefill 阶段满载，Decode 阶段中等负载）时的实测平均功耗为 420W ± 10W，数据源为 TechPowerUp GPU-Z 或 HWiNFO64 在 2024-11 至 2024-12 间的实测日志，该值用于替代标称 450W TDP 以精确计算 3 年电力成本

## Corrected Claim

RTX 4090 在运行 Qwen3-27B 推理时的平均功耗通常低于其 450W TDP 标称值，具体数值需依据实际负载和监控工具实测确定，用于替代标称 TDP 以精确计算电力成本。

## Evidence

[质询]该陈述包含具体的实测数值（420W ± 10W）及特定的时间窗口（2024-11至2024-12）和数据来源（TechPowerUp/HWiNFO64日志），属于典型的经验事实。由于缺乏外部来源支持，无法验证该具体数值是否真实存在或准确，且不同负载场景下的平均功耗波动范围可能更大，±10W的精度缺乏依据。 | 经验事实，逻辑自洽（420W低于450W TDP符合非满载或特定负载下的功耗特征），但缺来源支持，无法验证具体实测数值及时间窗口。

## Search Query

RTX 4090 power consumption LLM inference Qwen3 measured watts TechPowerUp 2024
