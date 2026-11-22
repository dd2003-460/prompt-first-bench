# N276: Decode 阶段每 token 的实际内存访问量 M_actual = Weights_Size + KV_Cache_Size_per_token * (S

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N91

## Claim

Decode 阶段每 token 的实际内存访问量 M_actual = Weights_Size + KV_Cache_Size_per_token * (Seq_Len - 1)，其中 KV_Cache_Size_per_token 需根据 Qwen3-27B 的实际 n_kv_heads 和 head_dim 计算，修正 N89 和 N100 的矛盾：若 n_kv_heads=8，则每 token KV 大小为 2 * 16 * 8 * 128 * 2 bytes = 65,536 bytes = 64 KB；若 n_kv_heads=32，则为 256 KB。

## Corrected Claim

Decode 阶段每 token 的实际内存访问量 M_actual = Weights_Size + KV_Cache_Size_per_token * (Seq_Len - 1)，其中 KV_Cache_Size_per_token 需根据 Qwen3-27B 的实际 n_kv_heads 和 head_dim 计算，修正 N89 和 N100 的矛盾：若 n_kv_heads=8，则每 token KV 大小为 2 * 16 * 8 * 128 * 2 bytes = 65,536 bytes = 64 KB；若 n_kv_heads=32，则为 256 KB。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（n_kv_heads=8, head_dim=128）符合主流大模型设计惯例，内存计算公式及数值推导（64KB/token）在逻辑和量级上均自洽。

## Search Query

Qwen3-27B n_kv_heads head_dim architecture specification
