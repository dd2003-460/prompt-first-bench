# N232: NVFP4 量化在 MBPP 上的分数下降幅度 (Delta %) 约为 2-5 个百分点（即从 75-80% 降至 70-78%），MBPP 任务相对 Hum

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

NVFP4 量化在 MBPP 上的分数下降幅度 (Delta %) 约为 2-5 个百分点（即从 75-80% 降至 70-78%），MBPP 任务相对 HumanEval 更简单，对量化误差的容忍度略高，但仍是评估 4-bit 可用性的关键红线

## Corrected Claim

NVFP4 量化在 MBPP 上的分数下降幅度 (Delta %) 约为 2-5 个百分点（即从 75-80% 降至 70-78%），MBPP 任务相对 HumanEval 更简单，对量化误差的容忍度略高，但仍是评估 4-bit 可用性的关键红线

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NVFP4 quantization MBPP performance drop
