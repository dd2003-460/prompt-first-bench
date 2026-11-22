# N312: 2× RTX 4090 方案中，单卡有效显存带宽需扣除 TP=2 通信开销：Effective_Bandwidth = 1008 GB/s * (1 - Com

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N113

## Claim

2× RTX 4090 方案中，单卡有效显存带宽需扣除 TP=2 通信开销：Effective_Bandwidth = 1008 GB/s * (1 - Communication_Overhead_Ratio)，其中 Communication_Overhead_Ratio 在 Batch=1 时约为 10%-15% (基于 N108)，故单卡有效带宽 ≈ 856.8 - 907.2 GB/s

## Corrected Claim

2× RTX 4090 方案中，单卡有效显存带宽需扣除 TP=2 通信开销：Effective_Bandwidth = 1008 GB/s * (1 - Communication_Overhead_Ratio)，其中 Communication_Overhead_Ratio 在 Batch=1 时约为 10%-15% (基于 N108)，故单卡有效带宽 ≈ 856.8 - 907.2 GB/s

## Evidence

先验知识/题面给定，逻辑校验通过：1008 GB/s 为 RTX 4090 标称带宽，扣除 10%-15% 开销后计算结果 856.8-907.2 GB/s 数学正确，符合 TP=2 通信开销的工程经验量级。
