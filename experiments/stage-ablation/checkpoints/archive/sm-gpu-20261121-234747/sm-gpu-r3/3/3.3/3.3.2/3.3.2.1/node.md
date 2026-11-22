# N257: 2×RTX 3090 BF16推理Qwen3-27B的内存带宽瓶颈量化：单卡936 GB/s，双卡聚合1872 GB/s；BF16权重读取需求 = 27e9 p

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N93

## Claim

2×RTX 3090 BF16推理Qwen3-27B的内存带宽瓶颈量化：单卡936 GB/s，双卡聚合1872 GB/s；BF16权重读取需求 = 27e9 params * 2 bytes = 54 GB；理论最大Decode吞吐 = 1872 GB/s / 54 GB ≈ 34.7 tokens/s；但考虑PCIe同步开销（假设10%损失）及KV Cache读取（32K上下文下KV Cache约4-8GB，每步读取一次），实际吞吐降至 34.7 * 0.9 * (54 / (54+6)) ≈ 28.8 tokens/s，与实测8-12 tokens/s存在巨大差距，表明瓶颈不在纯带宽而在软件调度或显存交换

## Corrected Claim

2×RTX 3090 BF16推理Qwen3-27B的内存带宽瓶颈量化：单卡936 GB/s，双卡聚合1872 GB/s；BF16权重读取需求 = 27e9 params * 2 bytes = 54 GB；理论最大Decode吞吐 = 1872 GB/s / 54 GB ≈ 34.7 tokens/s；但考虑PCIe同步开销（假设10%损失）及KV Cache读取（32K上下文下KV Cache约4-8GB，每步读取一次），实际吞吐降至 34.7 * 0.9 * (54 / (54+6)) ≈ 28.8 tokens/s，与实测8-12 tokens/s存在巨大差距，表明瓶颈不在纯带宽而在软件调度或显存交换

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090带宽936GB/s及Qwen3-27B参数量级符合常识，带宽瓶颈计算逻辑自洽，且正确指出了纯带宽理论值与实测值的差距源于软件/调度开销而非单纯硬件带宽不足。

## Search Query

RTX 3090 dual card BF16 inference throughput bottleneck memory bandwidth calculation
