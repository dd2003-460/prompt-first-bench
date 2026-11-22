# N94: 校准开销时间成本：GPTQ/AWQ 量化过程需运行校准数据集（通常 128-512 样本），在消费级 GPU 上耗时约 2-4 小时，这是一次性成本，不纳入日常

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

校准开销时间成本：GPTQ/AWQ 量化过程需运行校准数据集（通常 128-512 样本），在消费级 GPU 上耗时约 2-4 小时，这是一次性成本，不纳入日常 TCO，但影响初始部署时间。

## Corrected Claim

校准开销时间成本：GPTQ/AWQ 量化过程需运行校准数据集（通常 128-512 样本），在消费级 GPU 上耗时约 2-4 小时，这是一次性成本，不纳入日常 TCO，但影响初始部署时间。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GPTQ AWQ quantization calibration time cost hours
