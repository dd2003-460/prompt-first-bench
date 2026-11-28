# N17: 单卡方案吞吐量计算模型：Batch Size=1 时的 Tokens/s 取决于显存带宽（GB/s）除以每 Token 需读取的字节数（Weight Bytes

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

单卡方案吞吐量计算模型：Batch Size=1 时的 Tokens/s 取决于显存带宽（GB/s）除以每 Token 需读取的字节数（Weight Bytes + KV Cache Read/Write Bytes）。

## Corrected Claim

单卡方案吞吐量计算模型：Batch Size=1 时的 Tokens/s 取决于显存带宽（GB/s）除以每 Token 需读取的字节数（Weight Bytes + KV Cache Read/Write Bytes）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM inference throughput formula memory bandwidth bound tokens per second
