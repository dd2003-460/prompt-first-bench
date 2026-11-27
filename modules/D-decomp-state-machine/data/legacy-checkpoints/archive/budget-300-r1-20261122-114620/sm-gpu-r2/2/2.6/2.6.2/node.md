# N80: Decode 阶段（内存带宽受限）的吞吐量近似公式为 T_decode ≈ Bandwidth / (N_weights_bytes + N_kv_bytes_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

Decode 阶段（内存带宽受限）的吞吐量近似公式为 T_decode ≈ Bandwidth / (N_weights_bytes + N_kv_bytes_per_token)，其中 N_weights_bytes 为权重总字节数，N_kv_bytes_per_token 为每 token KV Cache 增量

## Corrected Claim

Decode 阶段（内存带宽受限）的吞吐量近似公式为 T_decode ≈ Bandwidth / (N_weights_bytes + N_kv_bytes_per_token)，其中 N_weights_bytes 为权重总字节数，N_kv_bytes_per_token 为每 token KV Cache 增量

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM decode throughput formula memory bandwidth weights kv cache
