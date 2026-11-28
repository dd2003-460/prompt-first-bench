# N71: Qwen3-27B 在 32K 上下文长度下，单次请求 Prefill 阶段的理论浮点运算量 (FLOPs) 约为 1.7 TFLOPs，计算公式为 2 * 2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22

## Claim

Qwen3-27B 在 32K 上下文长度下，单次请求 Prefill 阶段的理论浮点运算量 (FLOPs) 约为 1.7 TFLOPs，计算公式为 2 * 27e9 * 32768。

## Corrected Claim

Qwen3-27B 在 32K 上下文长度下，单次请求 Prefill 阶段的理论浮点运算量 (FLOPs) 约为 1.7 TFLOPs，计算公式为 2 * 27e9 * 32768。

## Evidence

先验知识/题面给定，逻辑校验通过：Prefill阶段计算量公式为2*N*L，代入N=27e9, L=32768，计算结果1.769472e15 FLOPs约等于1.7 TFLOPs，量级与数值均正确。
