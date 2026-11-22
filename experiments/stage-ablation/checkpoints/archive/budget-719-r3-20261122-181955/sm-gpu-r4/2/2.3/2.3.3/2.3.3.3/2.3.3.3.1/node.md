# N701: llama.cpp 在 Batch Size=2 时，KV Cache 连续内存块大小 = 2 * 32768 tokens * 256 KB/token = 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N251, N252, N253

## Claim

llama.cpp 在 Batch Size=2 时，KV Cache 连续内存块大小 = 2 * 32768 tokens * 256 KB/token = 16 GB（基于 N252 确认的 n_kv_heads=8, 64层, head_dim=128, BF16 参数），该尺寸必须小于 (显存总量 - 权重占用 - 框架开销) 的连续可用区域，否则分配失败。

## Corrected Claim

llama.cpp 在 Batch Size=2 时，KV Cache 连续内存块大小 = 2 * 32768 tokens * 256 KB/token = 16 GB（基于 N252 确认的 n_kv_heads=8, 64层, head_dim=128, BF16 参数），该尺寸必须小于 (显存总量 - 权重占用 - 框架开销) 的连续可用区域，否则分配失败。

## Evidence

先验知识/题面给定，逻辑校验通过：基于 N252 确认的模型参数（64层, n_kv_heads=8, head_dim=128, BF16），单 token KV Cache 大小为 64 * 8 * 128 * 2 * 2 bytes = 262,144 bytes = 256 KB。Batch Size=2 时，总大小为 2 * 32768 * 256 KB = 16 GB。计算过程符合内存布局逻辑，量级合理。

## Search Query

llama.cpp contiguous memory allocation batch size failure
