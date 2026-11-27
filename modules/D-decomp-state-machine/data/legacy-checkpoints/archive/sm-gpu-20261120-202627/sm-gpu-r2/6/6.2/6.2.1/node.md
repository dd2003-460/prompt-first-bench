# N128: RTX 4090 在持续 LLM 推理负载下的平均功耗（P_avg）实测值：需区分峰值 TDP（450W）与稳态推理功耗（通常报告范围 350-420W，需引用

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N29

## Claim

RTX 4090 在持续 LLM 推理负载下的平均功耗（P_avg）实测值：需区分峰值 TDP（450W）与稳态推理功耗（通常报告范围 350-420W，需引用具体基准测试如 MLPerf 或用户实测数据），用于精确计算 OpEx_energy。

## Corrected Claim

RTX 4090 在持续 LLM 推理负载下的平均功耗通常低于其 450W 峰值 TDP，具体数值取决于模型大小和批处理策略，需引用特定基准测试数据以精确计算 OpEx_energy。

## Evidence

[质询]该陈述包含具体的经验性数值范围（350-420W），属于硬件功耗规格，无法从第一性原理推导，且缺乏具体基准测试（如MLPerf）的直接数据支持，存在将不同负载场景（如训练vs推理、不同模型大小）的功耗数据混淆的风险。 | 经验事实，逻辑自洽（稳态功耗低于峰值TDP符合物理直觉）但缺来源支持（本轮检索无可用来源）。

## Search Query

RTX 4090 average power consumption LLM inference benchmark watts
