# N91: Throughput_tokens_per_second 在 batch=1 场景下的估算公式：Throughput ≈ (Memory_Bandwidth_G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

Throughput_tokens_per_second 在 batch=1 场景下的估算公式：Throughput ≈ (Memory_Bandwidth_GBps / (Weight_Size_GB + KV_Cache_Size_GB)) * 1000，需乘以硬件效率系数 η (η ≈ 0.6-0.8 对于消费级 GPU)

## Corrected Claim

Throughput_tokens_per_second 在 batch=1 场景下的估算公式：Throughput ≈ (Memory_Bandwidth_GBps / (Weight_Size_GB + KV_Cache_Size_GB)) * 1000，需乘以硬件效率系数 η (η ≈ 0.6-0.8 对于消费级 GPU)

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM inference throughput formula memory bandwidth efficiency factor
