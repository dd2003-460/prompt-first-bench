# N38: RTX 4090 单卡推理吞吐上限估算公式：Throughput ≈ (Memory_Bandwidth_GB/s * Batch_Size) / (Model

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N7

## Claim

RTX 4090 单卡推理吞吐上限估算公式：Throughput ≈ (Memory_Bandwidth_GB/s * Batch_Size) / (Model_Bytes_per_Token + KV_Bytes_per_Token)，其中 Memory_Bandwidth = 1008 GB/s，Model_Bytes_per_Token 取决于精度 (W4=0.5B, FP8=1B, BF16=2B)，该公式在 Batch_Size=1 时退化为带宽受限的解码速率，需结合实测校准系数 (通常为理论值的 60-80%)。

## Corrected Claim

RTX 4090 单卡推理吞吐上限估算公式：Throughput ≈ (Memory_Bandwidth_GB/s * Batch_Size) / (Model_Bytes_per_Token + KV_Bytes_per_Token)，其中 Memory_Bandwidth = 1008 GB/s，Model_Bytes_per_Token 取决于精度 (W4=0.5B, FP8=1B, BF16=2B)，该公式在 Batch_Size=1 时退化为带宽受限的解码速率，需结合实测校准系数 (通常为理论值的 60-80%)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM inference throughput formula memory bandwidth bound batch size 1
