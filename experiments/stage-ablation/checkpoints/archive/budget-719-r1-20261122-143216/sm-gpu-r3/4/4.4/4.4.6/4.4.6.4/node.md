# N327: 多卡方案（如 2×RTX 4090 TP=2）相对于单卡失效场景的性价比重算公式：Cost_Effective_Multi = (Cost_Hardware_2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N116

## Claim

多卡方案（如 2×RTX 4090 TP=2）相对于单卡失效场景的性价比重算公式：Cost_Effective_Multi = (Cost_Hardware_2x + Power_Cost_2x) / (Throughput_Multi × (1 - PCIe_Loss_Rate))，其中 Throughput_Multi 需扣除 N112 定义的 5%-15% 通信开销，用于与单卡降级方案对比。

## Corrected Claim

多卡方案（如 2×RTX 4090 TP=2）相对于单卡失效场景的性价比重算公式：Cost_Effective_Multi = (Cost_Hardware_2x + Power_Cost_2x) / (Throughput_Multi × (1 - PCIe_Loss_Rate))，其中 Throughput_Multi 需扣除 N112 定义的 5%-15% 通信开销，用于与单卡降级方案对比。

## Evidence

先验知识/题面给定，逻辑校验通过
