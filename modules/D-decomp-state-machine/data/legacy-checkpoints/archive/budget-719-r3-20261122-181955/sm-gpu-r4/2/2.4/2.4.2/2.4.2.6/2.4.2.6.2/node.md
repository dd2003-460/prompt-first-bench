# N738: 基于正确参数 (L=64, H_kv=8, D=128) 的 BF16 KV Cache 单 Token 内存占用计算：Size_per_token = 2 (

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N260

## Claim

基于正确参数 (L=64, H_kv=8, D=128) 的 BF16 KV Cache 单 Token 内存占用计算：Size_per_token = 2 (K/V) * L * H_kv * D * 2 bytes = 2 * 64 * 8 * 128 * 2 = 262,144 bytes = 256 KB。此值修正 N260 中基于 L=32 计算的 128 KB/token 错误。

## Corrected Claim

基于正确参数 (L=64, H_kv=8, D=128) 的 BF16 KV Cache 单 Token 内存占用计算：Size_per_token = 2 (K/V) * L * H_kv * D * 2 bytes = 2 * 64 * 8 * 128 * 2 = 262,144 bytes = 256 KB。此值修正 N260 中基于 L=32 计算的 128 KB/token 错误。

## Evidence

先验知识/题面给定，逻辑校验通过：2*64*8*128*2 = 262144 bytes = 256 KB，计算无误且量纲正确
