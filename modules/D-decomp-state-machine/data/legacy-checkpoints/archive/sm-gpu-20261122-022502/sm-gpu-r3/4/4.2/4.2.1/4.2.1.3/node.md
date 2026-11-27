# N193: 量化精度对GPU利用率的影响系数：INT8量化相比BF16使GPU利用率提升5-10个百分点（因权重加载减少），对应功耗增加15-25W；FP8量化使GPU利用

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N62

## Claim

量化精度对GPU利用率的影响系数：INT8量化相比BF16使GPU利用率提升5-10个百分点（因权重加载减少），对应功耗增加15-25W；FP8量化使GPU利用率提升3-5个百分点，对应功耗增加8-15W，需实测验证

## Corrected Claim

INT8量化相比BF16通常能提升GPU利用率并降低功耗，具体提升幅度（如利用率提升5-10个百分点，功耗变化等）需根据具体硬件架构和模型结构实测验证。

## Evidence

[质询]该陈述包含具体的经验性数值（利用率提升5-10%、功耗增加15-25W等），属于硬件性能与能效的经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

INT8 FP8 quantization GPU utilization power consumption LLM inference comparison
