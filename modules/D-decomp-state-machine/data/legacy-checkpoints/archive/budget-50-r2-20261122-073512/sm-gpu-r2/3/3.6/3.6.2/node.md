# N139: HellaSwag 基准测试的量化评估参数：数据版本为 validation set (10K samples)，评估指标为 accuracy，计算方式为 (c

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

HellaSwag 基准测试的量化评估参数：数据版本为 validation set (10K samples)，评估指标为 accuracy，计算方式为 (correct_choice / total_samples) × 100%，用于评估常识推理能力。

## Corrected Claim

HellaSwag 基准测试的量化评估参数：数据版本为 validation set (10K samples)，评估指标为 accuracy，计算方式为 (correct_choice / total_samples) × 100%，用于评估常识推理能力。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

HuggingFace evaluate HellaSwag benchmark validation set accuracy calculation
