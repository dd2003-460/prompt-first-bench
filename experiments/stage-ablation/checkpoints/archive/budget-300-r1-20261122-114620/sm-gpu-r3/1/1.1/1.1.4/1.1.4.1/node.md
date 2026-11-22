# N153: Qwen3-27B GPTQ/AWQ INT8 量化中，128-group 规模下 FP32 scale 因子的总显存占用约为 0.135 GB，计算公式为 (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

Qwen3-27B GPTQ/AWQ INT8 量化中，128-group 规模下 FP32 scale 因子的总显存占用约为 0.135 GB，计算公式为 (27.1e9 / 128) * 4 bytes / 1024^3

## Corrected Claim

Qwen3-27B GPTQ/AWQ INT8 量化中，128-group 规模下 FP32 scale 因子的总显存占用约为 0.135 GB，计算公式为 (27.1e9 / 128) * 4 bytes / 1024^3

## Evidence

先验知识/题面给定，逻辑校验通过：27.1e9 / 128 * 4 / 1024^3 ≈ 0.135 GB，计算无误且符合INT8量化显存估算常识。
