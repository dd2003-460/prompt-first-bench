# N61: Qwen3-27B在BF16精度下的理论FLOPs_per_token = 2 * 27.1e9 = 54.2 GFLOPs/token

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22

## Claim

Qwen3-27B在BF16精度下的理论FLOPs_per_token = 2 * 27.1e9 = 54.2 GFLOPs/token

## Corrected Claim

Qwen3-27B在BF16精度下的理论FLOPs_per_token = 2 * 27.1e9 = 54.2 GFLOPs/token

## Evidence

先验知识/题面给定，逻辑校验通过：Transformer模型每token理论FLOPs约为2倍参数量，2 * 27.1e9 = 54.2e9 FLOPs，量级与计算逻辑正确。
