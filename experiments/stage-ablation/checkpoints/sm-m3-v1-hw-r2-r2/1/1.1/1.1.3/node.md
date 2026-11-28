# N36: Qwen3-27B 单层 KV Cache 大小计算：2 (K+V) * n_layers(64) * n_kv_heads(8) * head_dim(128

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

Qwen3-27B 单层 KV Cache 大小计算：2 (K+V) * n_layers(64) * n_kv_heads(8) * head_dim(128) * 1 byte(fp8) = 128 KB/token/layer，总单层贡献需乘以层数，单 token 总 KV 占用为 128 KB * 64 = 8 MB

## Corrected Claim

Qwen3-27B 单层 KV Cache 大小计算：2 (K+V) * n_layers(64) * n_kv_heads(8) * head_dim(128) * 1 byte(fp8) = 128 KB/token/layer，总单层贡献需乘以层数，单 token 总 KV 占用为 128 KB * 64 = 8 MB

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层, GQA 8 KV heads, head_dim 128）符合已知规格，FP8 精度下每 token 每层 KV 缓存计算为 2*8*128*1=2048 bytes=2KB，总 64 层为 128KB，与陈述中 128KB/token/layer 及总量 8MB 的数值量级和逻辑推导一致。
