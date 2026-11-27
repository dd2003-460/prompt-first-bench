# N433: 针对Qwen3-27B FP8量化，假设采用group_size=128且scale/zero为FP16格式，计算具体元数据开销：(27e9 / 128) * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N140

## Claim

针对Qwen3-27B FP8量化，假设采用group_size=128且scale/zero为FP16格式，计算具体元数据开销：(27e9 / 128) * 2 bytes ≈ 421.875 MB，占27GB总权重的比例 ≈ 1.56%

## Corrected Claim

针对Qwen3-27B FP8量化，假设采用group_size=128且scale/zero为FP16格式，计算具体元数据开销：(27e9 / 128) * 2 bytes ≈ 421.875 MB，占27GB总权重的比例 ≈ 1.56%

## Evidence

先验知识/题面给定，逻辑校验通过：27e9/128*2 = 421,875,000 bytes ≈ 421.875 MB；421.875/27000 ≈ 1.5625%，计算无误。

## Search Query

Qwen3-27B FP8 quantization metadata size calculation 128 group size
