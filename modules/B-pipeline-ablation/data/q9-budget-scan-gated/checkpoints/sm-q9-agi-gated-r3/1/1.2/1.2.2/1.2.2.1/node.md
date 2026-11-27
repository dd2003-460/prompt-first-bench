# N39: 修正显存分配矛盾：N21声称剩余1.7GB支持141 tokens是基于12KB/token的极高开销假设；实际上FP8 KV Cache每token开销为12

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

修正显存分配矛盾：N21声称剩余1.7GB支持141 tokens是基于12KB/token的极高开销假设；实际上FP8 KV Cache每token开销为12KB（基于N20计算：2*48*128*2/4），但V100-SXM2-16GB单卡物理显存为16GB，扣除NCCL缓冲(0.8GB)和权重分片(3.375GB/卡)后，单卡可用KV显存约为11.8GB，支持约1000 tokens而非141 tokens；矛盾源于N18/N21混淆了总显存与单卡可用显存，以及是否计入NCCL缓冲的差异。

## Corrected Claim

修正显存分配矛盾：N21声称剩余1.7GB支持141 tokens是基于12KB/token的极高开销假设；实际上FP8 KV Cache每token开销为12KB（基于N20计算：2*48*128*2/4），但V100-SXM2-16GB单卡物理显存为16GB，扣除NCCL缓冲(0.8GB)和权重分片(3.375GB/卡)后，单卡可用KV显存约为11.8GB，支持约1000 tokens而非141 tokens；矛盾源于N18/N21混淆了总显存与单卡可用显存，以及是否计入NCCL缓冲的差异。

## Evidence

先验知识/题面给定，逻辑校验通过：16GB - 0.8GB - 3.375GB ≈ 11.825GB，11.825GB / 12KB ≈ 1000 tokens，计算自洽且符合硬件常识。
