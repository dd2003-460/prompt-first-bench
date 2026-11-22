# N187: 在 W4 精度下，Qwen3-27B (权重 ~14.57GB) 在 Apple M2 Ultra (800 GB/s) 上的理论 Decode 吞吐量上限为 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

在 W4 精度下，Qwen3-27B (权重 ~14.57GB) 在 Apple M2 Ultra (800 GB/s) 上的理论 Decode 吞吐量上限为 54.9 tokens/s (800 / 14.57)，在 M3 Ultra (819 GB/s) 上为 56.2 tokens/s (819 / 14.57)。

## Corrected Claim

在 W4 精度下，Qwen3-27B (权重 ~14.57GB) 在 Apple M2 Ultra (800 GB/s) 上的理论 Decode 吞吐量上限为 54.9 tokens/s (800 / 14.57)，在 M3 Ultra (819 GB/s) 上为 56.2 tokens/s (819 / 14.57)。

## Evidence

先验知识/题面给定，逻辑校验通过：800/14.57≈54.89，819/14.57≈56.21，计算无误且符合内存带宽瓶颈下的理论吞吐量定义。
