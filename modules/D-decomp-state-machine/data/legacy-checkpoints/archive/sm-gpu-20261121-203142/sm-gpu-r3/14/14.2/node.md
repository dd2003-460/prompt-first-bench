# N368: NVIDIA L4 在 INT4 量化下的理论 Decode TPS 计算：带宽 300 GB/s，权重 13.5GB + KV Cache 4GB ≈ 17.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N125

## Claim

NVIDIA L4 在 INT4 量化下的理论 Decode TPS 计算：带宽 300 GB/s，权重 13.5GB + KV Cache 4GB ≈ 17.5GB 读取量，理论 TPS ≈ 300/17.5 ≈ 17 tokens/s；考虑实际带宽利用率 (60-70%) 和计算开销，实际 TPS 预计为 10-12 tokens/s，仅为 RTX 4090 (INT4, ~40-50 tokens/s) 的 25-30%。

## Corrected Claim

NVIDIA L4 在 INT4 量化下的理论 Decode TPS 计算：带宽 300 GB/s，权重 13.5GB + KV Cache 4GB ≈ 17.5GB 读取量，理论 TPS ≈ 300/17.5 ≈ 17 tokens/s；考虑实际带宽利用率 (60-70%) 和计算开销，实际 TPS 预计为 10-12 tokens/s，仅为 RTX 4090 (INT4, ~40-50 tokens/s) 的 25-30%。

## Evidence

先验知识/题面给定，逻辑校验通过：L4带宽300GB/s与17.5GB读取量计算出的理论TPS约17，考虑利用率后10-12 TPS符合工程直觉，且与4090性能对比合理。
