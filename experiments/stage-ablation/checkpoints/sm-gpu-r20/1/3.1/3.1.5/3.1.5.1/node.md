# N130: NVFP4 (4-bit float) 基础权重占用为 27.8B * 0.5 bytes = 13.9 GB，若采用 per-tensor scale，额外开

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

NVFP4 (4-bit float) 基础权重占用为 27.8B * 0.5 bytes = 13.9 GB，若采用 per-tensor scale，额外开销为 0 bytes，总占用 13.9 GB。

## Corrected Claim

NVFP4 (4-bit float) 基础权重占用为 27.8B * 0.5 bytes = 13.9 GB，若采用 per-tensor scale，额外开销为 0 bytes，总占用 13.9 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27.8B参数 * 0.5 bytes/param = 13.9GB，计算正确；Per-tensor scale仅增加常数级开销（可忽略），总占用13.9GB符合逻辑。
