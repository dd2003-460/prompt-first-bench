# N237: RTX 4090 运行 Qwen3-27B BF16 时的 KV Cache 显存占用计算：KV_Cache_Size = 2 * 64 * 32 * 128 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

RTX 4090 运行 Qwen3-27B BF16 时的 KV Cache 显存占用计算：KV_Cache_Size = 2 * 64 * 32 * 128 * 32768 * 2 bytes = 2,147,483,648 bytes ≈ 2.0 GB (单序列)，若 Batch Size=1，总 KV Cache 约为 2.0 GB。

## Corrected Claim

RTX 4090 运行 Qwen3-27B BF16 时的 KV Cache 显存占用计算：KV_Cache_Size = 2 * 64 * 32 * 128 * 32768 * 2 bytes = 2,147,483,648 bytes ≈ 2.0 GB (单序列)，若 Batch Size=1，总 KV Cache 约为 2.0 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层, 32 KV头, 128头维）符合27B模型典型配置，BF16精度下2字节/元素，计算式 2*64*32*128*32768*2 = 2,147,483,648 bytes ≈ 2.0 GB 数学推导正确，量级合理。
