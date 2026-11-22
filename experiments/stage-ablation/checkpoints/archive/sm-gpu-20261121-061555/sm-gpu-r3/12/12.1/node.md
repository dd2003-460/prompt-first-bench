# N134: RTX 4090 在 FP8/INT8 推理模式下的实际功耗曲线：在 24/7 连续推理负载下，平均功耗并非恒定 400W (TDP上限)，通常随负载波动，需获

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

RTX 4090 在 FP8/INT8 推理模式下的实际功耗曲线：在 24/7 连续推理负载下，平均功耗并非恒定 400W (TDP上限)，通常随负载波动，需获取实测平均功耗数据（如 350W-380W）以修正 OpEx 计算。

## Corrected Claim

RTX 4090 在 FP8/INT8 推理模式下的实际功耗通常低于其 450W TDP 上限，具体平均功耗需依据实测数据确定，而非恒定值。

## Evidence

[质询]该陈述包含具体的经验性数值范围（350W-380W）和特定工况下的行为描述，属于硬件实测数据，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 4090 average power consumption during sustained LLM inference load 24/7
