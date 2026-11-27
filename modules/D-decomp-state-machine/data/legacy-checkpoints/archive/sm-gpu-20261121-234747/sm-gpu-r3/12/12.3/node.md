# N504: RTX 4090 的满载功耗需区分 TDP（450W）与实测平均功耗，在 24/7 连续推理场景下，平均功耗通常为 TDP 的 60-80%（约 270-360

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N159

## Claim

RTX 4090 的满载功耗需区分 TDP（450W）与实测平均功耗，在 24/7 连续推理场景下，平均功耗通常为 TDP 的 60-80%（约 270-360W），需通过功率计实测或基于 NVIDIA 官方功耗曲线估算，具体数值取决于负载类型（Prefill vs Decode） [待核验]

## Corrected Claim

RTX 4090 的满载功耗需区分 TDP（450W）与实测平均功耗，在 24/7 连续推理场景下，平均功耗通常低于 TDP，具体数值取决于负载类型（Prefill vs Decode），需通过功率计实测或基于 NVIDIA 官方功耗曲线估算。

## Evidence

[质询]该陈述包含具体的经验性数值范围（60-80%），属于硬件功耗规格及负载特性，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 4090 average power consumption LLM inference 24/7 watts measured
