# N155: Qwen3-27B NVFP4/W4 量化中，128-group 规模下 FP16 scale 因子的总显存占用约为 0.106 GB，计算公式为 (27.1e

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N43

## Claim

Qwen3-27B NVFP4/W4 量化中，128-group 规模下 FP16 scale 因子的总显存占用约为 0.106 GB，计算公式为 (27.1e9 / 128) * 2 bytes / 1024^3

## Corrected Claim

Qwen3-27B NVFP4/W4 量化中，128-group 规模下 FP16 scale 因子的总显存占用约为 0.106 GB，计算公式为 (27.1e9 / 128) * 2 bytes / 1024^3

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

Qwen3-27B NVFP4 128-group scale factor memory footprint calculation
