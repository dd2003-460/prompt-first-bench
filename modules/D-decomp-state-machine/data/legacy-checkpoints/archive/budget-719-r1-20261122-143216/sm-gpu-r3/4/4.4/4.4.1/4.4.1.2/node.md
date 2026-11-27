# N312: 在 Batch=1 时，内存带宽利用率受 KV Cache 读取模式影响，GQA 架构下 KV 头数减少使得单次 Decode 的 KV 读取量降低，从而可能提

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N111

## Claim

在 Batch=1 时，内存带宽利用率受 KV Cache 读取模式影响，GQA 架构下 KV 头数减少使得单次 Decode 的 KV 读取量降低，从而可能提升有效带宽利用率至 90%+，具体提升幅度需结合 Qwen3-27B 的 num_kv_heads (8) 与 num_heads (32) 比例计算。

## Corrected Claim

在 Batch=1 时，内存带宽利用率受 KV Cache 读取模式影响，GQA 架构下 KV 头数减少使得单次 Decode 的 KV 读取量降低，从而可能提升有效带宽利用率至 90%+，具体提升幅度需结合 Qwen3-27B 的 num_kv_heads (8) 与 num_heads (32) 比例计算。

## Evidence

先验知识/题面给定，逻辑校验通过
