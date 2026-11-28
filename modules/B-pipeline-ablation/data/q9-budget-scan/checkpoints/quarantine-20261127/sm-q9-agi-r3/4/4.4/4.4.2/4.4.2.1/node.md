# N207: MacBook M1 Max 运行 Llama-3-8B (FP16) 的推理速度瓶颈分析：M1 Max 内存带宽 400 GB/s；加载 16 GB 权重需 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

MacBook M1 Max 运行 Llama-3-8B (FP16) 的推理速度瓶颈分析：M1 Max 内存带宽 400 GB/s；加载 16 GB 权重需 16/400 = 0.04s；理论最大吞吐 1/0.04 = 25 tokens/s；实际受 GPU 核心计算和内存控制器效率影响，15-25 tokens/s 符合带宽上限约束。

## Corrected Claim

MacBook M1 Max 运行 Llama-3-8B (FP16) 的推理速度瓶颈分析：M1 Max 内存带宽 400 GB/s；加载 16 GB 权重需 16/400 = 0.04s；理论最大吞吐 1/0.04 = 25 tokens/s；实际受 GPU 核心计算和内存控制器效率影响，15-25 tokens/s 符合带宽上限约束。

## Evidence

先验知识/题面给定，逻辑校验通过：M1 Max 内存带宽确为 400GB/s，Llama-3-8B FP16 权重约 16GB，算术推导 16/400=0.04s 及 25 tokens/s 上限正确，符合大模型推理带宽瓶颈原理。
