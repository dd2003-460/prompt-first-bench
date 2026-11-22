# N179: RTX 4090 显存带宽 1008GB/s 是推理吞吐的理论上限瓶颈：对于 INT8 27B 模型，每 token 需读取 27GB 权重，理论最大吞吐 = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

RTX 4090 显存带宽 1008GB/s 是推理吞吐的理论上限瓶颈：对于 INT8 27B 模型，每 token 需读取 27GB 权重，理论最大吞吐 = 1008GB/s / 27GB = 37.3 tokens/s，实测 28 tokens/s 达到理论峰值的 75%，符合 AR 模型推理的典型效率范围

## Corrected Claim

RTX 4090 显存带宽 1008GB/s 是推理吞吐的理论上限瓶颈：对于 INT8 27B 模型，每 token 需读取 27GB 权重，理论最大吞吐 = 1008GB/s / 27GB = 37.3 tokens/s，实测 28 tokens/s 达到理论峰值的 75%，符合 AR 模型推理的典型效率范围

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090显存带宽1008GB/s与27GB权重读取量级符合硬件规格，37.3 tokens/s理论上限计算正确，75%效率符合AR模型推理典型范围

## Search Query

RTX 4090 memory bandwidth inference throughput theoretical limit
