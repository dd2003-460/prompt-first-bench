# N14: GPU显存带宽（GB/s）决定推理吞吐上限：Tokens/s ≈ 显存带宽 / (每token读取字节数)，其中每token读取字节数包括权重分片与KV Cac

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

GPU显存带宽（GB/s）决定推理吞吐上限：Tokens/s ≈ 显存带宽 / (每token读取字节数)，其中每token读取字节数包括权重分片与KV Cache增量。

## Corrected Claim

GPU显存带宽（GB/s）决定推理吞吐上限：Tokens/s ≈ 显存带宽 / (每token读取字节数)，其中每token读取字节数包括权重分片与KV Cache增量。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GPU memory bandwidth inference throughput tokens per second formula
