# N386: RTX 5090 FP8推理吞吐量估算值89.5 tokens/s（来自N165）的每Token成本置信区间为$0.0000027-$0.0000041/tok

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N159

## Claim

RTX 5090 FP8推理吞吐量估算值89.5 tokens/s（来自N165）的每Token成本置信区间为$0.0000027-$0.0000041/token，基于吞吐量置信区间71.6-107.4 tokens/s反推

## Corrected Claim

RTX 5090 FP8推理吞吐量估算值89.5 tokens/s（来自N165）的每Token成本置信区间为$0.0000027-$0.0000041/token，基于吞吐量置信区间71.6-107.4 tokens/s反推

## Evidence

先验知识/题面给定，逻辑校验通过：成本与吞吐量成反比，基于给定的吞吐量区间[71.6, 107.4]和基准吞吐量89.5，反推的成本区间[0.0000027, 0.0000041]在数学上自洽且量级合理。
