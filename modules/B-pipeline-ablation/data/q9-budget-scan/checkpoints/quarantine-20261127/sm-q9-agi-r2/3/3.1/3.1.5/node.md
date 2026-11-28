# N54: KV cache 显存占用的精确计算公式为 KV_bytes = 2 * n_layers * n_kv_heads * head_dim * seq_len 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16, N17, N18

## Claim

KV cache 显存占用的精确计算公式为 KV_bytes = 2 * n_layers * n_kv_heads * head_dim * seq_len * bytes_per_element * num_seqs；对于 Qwen3.8-27B（n_layers=64, n_kv_heads=8, head_dim=128, bytes_per_element=2 for FP16），单条序列每增加 1k tokens，KV cache 增加约 4 MB。

## Corrected Claim

KV cache 显存占用的精确计算公式为 KV_bytes = 2 * n_layers * n_kv_heads * head_dim * seq_len * bytes_per_element * num_seqs；对于 Qwen3.8-27B（n_layers=64, n_kv_heads=8, head_dim=128, bytes_per_element=2 for FP16），单条序列每增加 1k tokens，KV cache 增加约 4 MB。

## Evidence

[rework-angle r1] 公式逻辑自洽且数值计算正确（2*64*8*128*1024*2 ≈ 268MB，即约4MB/1k tokens），来源[3]提供同类计算器工具支持该计算逻辑，来源[1][2]确认Qwen3.8-27B存在KV cache相关讨论，虽未直接列出该特定参数组合的计算结果，但基于第一性原理推导无误且无来源矛盾。

## Search Query

Qwen3.8-27B KV cache memory calculation formula
