# N53: KV Cache 卸载至 CPU 内存后，每次 token 生成需从内存读取 KV 数据，若 KV Cache 为 2.15 GB (BF16, 32K)，每次

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

KV Cache 卸载至 CPU 内存后，每次 token 生成需从内存读取 KV 数据，若 KV Cache 为 2.15 GB (BF16, 32K)，每次读取理论延迟为 2.15 GB / 32 GB/s ≈ 67 ms，远高于 GPU 内部读取延迟 (<1 ms)，导致 token 生成速度下降 90% 以上，KV Cache 卸载通常不可行

## Corrected Claim

KV Cache 卸载至 CPU 内存后，每次 token 生成需从内存读取 KV 数据，若 KV Cache 为 2.15 GB (BF16, 32K)，每次读取理论延迟为 2.15 GB / 32 GB/s ≈ 67 ms，远高于 GPU 内部读取延迟 (<1 ms)，导致 token 生成速度下降 90% 以上，KV Cache 卸载通常不可行

## Evidence

先验知识/题面给定，逻辑校验通过：2.15GB / 32GB/s ≈ 67ms 计算正确，且远高于 GPU 内部延迟，符合硬件性能常识
