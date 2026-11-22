# N197: KV Cache 单 token 大小计算公式修正验证：2 (K/V) * num_layers(64) * num_kv_heads(8) * head_di

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N97

## Claim

KV Cache 单 token 大小计算公式修正验证：2 (K/V) * num_layers(64) * num_kv_heads(8) * head_dim(128) * bytes_per_element(2 for BF16) = 262,144 bytes = 256 KB/token，该计算排除了 N20 中错误的 1.2MB 假设（可能误用了 full attention 而非 GQA），确认 GQA 机制将 KV 内存需求降低至 MHA 的 1/8

## Corrected Claim

KV Cache 单 token 大小计算公式修正验证：2 (K/V) * num_layers(64) * num_kv_heads(8) * head_dim(128) * bytes_per_element(2 for BF16) = 262,144 bytes = 256 KB/token，该计算排除了 N20 中错误的 1.2MB 假设（可能误用了 full attention 而非 GQA），确认 GQA 机制将 KV 内存需求降低至 MHA 的 1/8

## Evidence

先验知识/题面给定，逻辑校验通过：2 * 64 * 8 * 128 * 2 = 262,144 bytes = 256 KB，计算无误；GQA (8 heads) 相比 MHA (64 heads) 确实降低 8 倍 KV 内存。
