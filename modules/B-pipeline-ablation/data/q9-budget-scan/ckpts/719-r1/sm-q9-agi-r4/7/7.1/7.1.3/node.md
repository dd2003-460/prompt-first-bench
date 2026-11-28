# N273: NVLink 通信延迟的固定开销（Latency）部分约为 2-5 µs per hop，而在小消息（<1MB）场景下，延迟占比远高于带宽瓶颈；对于 30MB 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N86

## Claim

NVLink 通信延迟的固定开销（Latency）部分约为 2-5 µs per hop，而在小消息（<1MB）场景下，延迟占比远高于带宽瓶颈；对于 30MB 消息，总耗时 T = Latency + Size/Bandwidth，需分离测量纯延迟与带宽受限部分的贡献，以区分是链路拥塞还是调度延迟主导了 12ms 的耗时。

## Corrected Claim

NVLink 通信延迟的固定开销（Latency）部分约为 2-5 µs per hop，而在小消息（<1MB）场景下，延迟占比远高于带宽瓶颈；对于 30MB 消息，总耗时 T = Latency + Size/Bandwidth，需分离测量纯延迟与带宽受限部分的贡献，以区分是链路拥塞还是调度延迟主导了 12ms 的耗时。

## Evidence

[质询]NVLink 的纯硬件链路延迟通常在纳秒到微秒级别（例如 ~1-2 µs），2-5 µs 可能包含了软件栈（CUDA Driver/Runtime）的开销，若指纯硬件链路则数值偏高；但在系统级通信语境下，该量级作为端到端固定开销是合理的。 | 先验知识/题面给定，逻辑校验通过：NVLink 系统级通信延迟在微秒量级符合工程常识，小消息延迟主导、大消息带宽主导符合通信模型基本逻辑。

## Search Query

NVLink latency small message overhead microseconds NCCL
