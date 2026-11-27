# N23: 代表工作点 A（消费级高带宽）：以 NVIDIA RTX 4090 (24GB, ~1008 GB/s) 为例，运行 FP8 Qwen3-27B (27GB) 

- **status**: verified
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

父节点级核验通过：正交+完备+无冗余（子节点A1、A2、A3分别代表了不同的量化精度（INT4/FP8/BF16）、硬件配置（2卡/4卡）和性能-成本权衡点。它们在技术参数（显存占用、理论吞吐、CapEx）上互不重叠且逻辑自洽，共同构成了对‘消费级高带宽’工作点下不同部署策略的完整覆盖。虽然A2和A3都涉及多卡通信开销，但侧重点不同（A2为平衡型双卡，A3为冗余型四卡），因此不构成冗余。）

## Search Query

RTX 4090 memory bandwidth GB/s Qwen3-27B FP8 inference speed
