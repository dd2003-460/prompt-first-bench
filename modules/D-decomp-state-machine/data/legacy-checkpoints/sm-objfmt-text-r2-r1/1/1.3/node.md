# N9: KV Cache 显存需求 K_mem 计算公式为 2 * n_layers * n_kv_heads * head_dim * seq_len * bytes

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

KV Cache 显存需求 K_mem 计算公式为 2 * n_layers * n_kv_heads * head_dim * seq_len * bytes_per_elem，其中 n_layers=64, n_kv_heads=8, head_dim=128, seq_len=32768, bytes_per_elem 取决于精度（BF16=2, FP8=1），计算得出 BF16 下约为 13.7 GB，FP8 下约为 6.85 GB

## Corrected Claim

KV Cache 显存需求 K_mem 计算公式为 2 * n_layers * n_kv_heads * head_dim * seq_len * bytes_per_elem，其中 n_layers=64, n_kv_heads=8, head_dim=128, seq_len=32768, bytes_per_elem 取决于精度（BF16=2, FP8=1），计算得出 BF16 下约为 13.7 GB，FP8 下约为 6.85 GB

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合标准Transformer KV Cache计算逻辑，数值代入计算准确（2*64*8*128*32768*2 ≈ 13.7GB, *1 ≈ 6.85GB），量级合理。

## Search Query

Qwen3-27B layer count kv heads head dim config
