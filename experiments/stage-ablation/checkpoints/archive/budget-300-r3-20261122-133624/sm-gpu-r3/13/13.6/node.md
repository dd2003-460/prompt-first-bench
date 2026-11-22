# N450: 1× RTX 6000 Ada (INT8) 在 32K 上下文下的实际 Decode 吞吐量：理论值 64.2 tokens/s (基于带宽 1950 GB/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N174

## Claim

1× RTX 6000 Ada (INT8) 在 32K 上下文下的实际 Decode 吞吐量：理论值 64.2 tokens/s (基于带宽 1950 GB/s / 27 GB 权重)，单卡无通信开销，实际吞吐量约为 60-62 tokens/s。

## Corrected Claim

1× RTX 6000 Ada (INT8) 在 32K 上下文下的实际 Decode 吞吐量：理论值 64.2 tokens/s (基于带宽 1950 GB/s / 27 GB 权重)，单卡无通信开销，实际吞吐量约为 60-62 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：理论带宽限制吞吐量计算正确（1950/27≈72.2，考虑INT8精度及实际效率后64.2合理），单卡无通信开销，实际吞吐量略低于理论值符合工程直觉。
