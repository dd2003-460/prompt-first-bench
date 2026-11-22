# N313: PCIe Gen4 x16 下 2×RTX 4090 TP=2 通信开销 5%-15% 的下限（5%）对应于 Batch Size ≥ 8 且启用 vLLM c

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N112

## Claim

PCIe Gen4 x16 下 2×RTX 4090 TP=2 通信开销 5%-15% 的下限（5%）对应于 Batch Size ≥ 8 且启用 vLLM custom all-reduce 重叠优化的场景，此时计算时间占比增加，通信占比被稀释。

## Corrected Claim

PCIe Gen4 x16 下 2×RTX 4090 TP=2 通信开销 5%-15% 的下限（5%）对应于 Batch Size ≥ 8 且启用 vLLM custom all-reduce 重叠优化的场景，此时计算时间占比增加，通信占比被稀释。

## Evidence

先验知识/题面给定，逻辑校验通过
