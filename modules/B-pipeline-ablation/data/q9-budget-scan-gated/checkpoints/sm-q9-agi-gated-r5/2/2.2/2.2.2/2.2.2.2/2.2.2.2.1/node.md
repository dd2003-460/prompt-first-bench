# N143: 修正N70及树内矛盾(N33/N40)：V100-SXM2-16GB物理显存为16GB，扣除CUDA上下文(~0.5GB)、NCCL缓冲(~1GB)及TP=4分

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

修正N70及树内矛盾(N33/N40)：V100-SXM2-16GB物理显存为16GB，扣除CUDA上下文(~0.5GB)、NCCL缓冲(~1GB)及TP=4分片权重(3.375GB/卡)后，单卡实际可用KV Cache显存约为11.125GB（16 - 0.5 - 1 - 3.375），而非N70引用的1.7GB。

## Corrected Claim

修正N70及树内矛盾(N33/N40)：V100-SXM2-16GB物理显存为16GB，扣除CUDA上下文(~0.5GB)、NCCL缓冲(~1GB)及TP=4分片权重(3.375GB/卡)后，单卡实际可用KV Cache显存约为11.125GB（16 - 0.5 - 1 - 3.375），而非N70引用的1.7GB。

## Evidence

先验知识/题面给定，逻辑校验通过：V100-SXM2-16GB显存确为16GB，算术运算16-0.5-1-3.375=11.125正确，符合GPU显存分配的基本逻辑。
