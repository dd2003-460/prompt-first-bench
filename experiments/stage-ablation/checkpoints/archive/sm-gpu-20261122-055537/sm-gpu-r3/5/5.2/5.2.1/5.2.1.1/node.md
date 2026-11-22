# N269: Qwen3-27B INT4 (AWQ) 权重大小的精确计算值：27B * 4bits / 8 = 13.5 GB，加上 AWQ 量化所需的 Scale Fac

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

Qwen3-27B INT4 (AWQ) 权重大小的精确计算值：27B * 4bits / 8 = 13.5 GB，加上 AWQ 量化所需的 Scale Factors 和 Zero Points (约 0.5 GB) 及模型配置元数据，总权重占用约为 14.0-14.5 GB。

## Corrected Claim

Qwen3-27B INT4 (AWQ) 权重大小的精确计算值：27B * 4bits / 8 = 13.5 GB，加上 AWQ 量化所需的 Scale Factors 和 Zero Points (约 0.5 GB) 及模型配置元数据，总权重占用约为 14.0-14.5 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数INT4量化基础体积为13.5GB，加上AWQ所需的Scale/Zero点及元数据，总占用14.0-14.5GB符合工程常识与数学推导。
