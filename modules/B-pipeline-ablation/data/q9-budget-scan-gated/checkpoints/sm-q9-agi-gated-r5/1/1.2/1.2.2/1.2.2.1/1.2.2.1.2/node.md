# N85: 基于NVFP4量化修正后的单卡显存分配：V100-SXM2-16GB物理显存16GB，扣除CUDA上下文(0.5GB)、NCCL缓冲(0.8GB)及NVFP4权

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N39

## Claim

基于NVFP4量化修正后的单卡显存分配：V100-SXM2-16GB物理显存16GB，扣除CUDA上下文(0.5GB)、NCCL缓冲(0.8GB)及NVFP4权重分片(1.6875GB)后，单卡实际可用KV Cache显存为 16 - 0.5 - 0.8 - 1.6875 = 13.0125 GB。

## Corrected Claim

基于NVFP4量化修正后的单卡显存分配：V100-SXM2-16GB物理显存16GB，扣除CUDA上下文(0.5GB)、NCCL缓冲(0.8GB)及NVFP4权重分片(1.6875GB)后，单卡实际可用KV Cache显存为 16 - 0.5 - 0.8 - 1.6875 = 13.0125 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 16 - 0.5 - 0.8 - 1.6875 = 13.0125 正确，且各项显存占用量级符合常规工程估算逻辑。
