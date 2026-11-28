# N39: 在 fp8 (1 byte/element) 精度下，单层单 token 的 KV Cache 占用为 2 * L * KV_heads * head_dim 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

在 fp8 (1 byte/element) 精度下，单层单 token 的 KV Cache 占用为 2 * L * KV_heads * head_dim * 1 = 2 * 64 * 8 * 128 = 131,072 bytes = 128KB

## Corrected Claim

在 fp8 (1 byte/element) 精度下，单层单 token 的 KV Cache 占用为 2 * L * KV_heads * head_dim * 1 = 2 * 64 * 8 * 128 = 131,072 bytes = 128KB

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 包含 Key 和 Value 两部分，故系数为 2；计算 2 * 64 * 8 * 128 * 1 byte = 131,072 bytes，换算为 128 KB，数值与量纲均正确。
