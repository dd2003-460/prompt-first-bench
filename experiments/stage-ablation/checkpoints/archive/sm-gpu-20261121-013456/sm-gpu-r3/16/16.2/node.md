# N309: 当 Batch Size > 2 时，2×RTX 4090 多卡并行推理的效率衰减率约为 15-25%，即实际吞吐量仅为理论单卡吞吐量的 75-85%；例如，若

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N127

## Claim

当 Batch Size > 2 时，2×RTX 4090 多卡并行推理的效率衰减率约为 15-25%，即实际吞吐量仅为理论单卡吞吐量的 75-85%；例如，若单卡理论吞吐量为 50 tokens/s，双卡实际吞吐量约为 75-85 tokens/s，而非 100 tokens/s。

## Corrected Claim

当 Batch Size > 2 时，2×RTX 4090 多卡并行推理的效率衰减率约为 15-25%，即实际吞吐量仅为理论单卡吞吐量的 75-85%；例如，若单卡理论吞吐量为 50 tokens/s，双卡实际吞吐量约为 75-85 tokens/s，而非 100 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Dual GPU inference efficiency degradation batch size PCIe bottleneck
