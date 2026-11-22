# N23: 代表工作点 A（消费级高带宽）：以 NVIDIA RTX 4090 (24GB, ~1008 GB/s) 为例，运行 FP8 Qwen3-27B (27GB) 

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

代表工作点 A（消费级高带宽）：以 NVIDIA RTX 4090 (24GB, ~1008 GB/s) 为例，运行 FP8 Qwen3-27B (27GB) 需 2 卡，理论 Decode 吞吐上限约为 1008 / 27 ≈ 37.3 tokens/s（未计通信开销），这是单用户交互的高性能基准。

## Corrected Claim

代表工作点 A（消费级高带宽）：以 NVIDIA RTX 4090 (24GB, ~1008 GB/s) 为例，运行 FP8 Qwen3-27B (27GB) 需 2 卡，理论 Decode 吞吐上限约为 1008 / 27 ≈ 37.3 tokens/s（未计通信开销），这是单用户交互的高性能基准。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点并非正交的工作点，而是同一硬件配置（2x/4x RTX 4090）下不同精度/分片策略的变体，存在逻辑重叠；且A1与A2在CapEx上完全相同但性能描述矛盾（A1称单卡装下13.5GB，A2称27GB需分片，未解释为何同硬件下带宽模型不同）；A3作为冗余配置未体现‘工作点’的典型性，反而引入了非必要的通信开销假设，导致完备性不足。）

## Search Query

RTX 4090 memory bandwidth GB/s Qwen3-27B FP8 inference speed
