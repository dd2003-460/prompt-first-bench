# N100: 修正自矛盾检测：N28 的 KV Cache 计算中 '128' (head_dim) 与 N32 定义的架构参数 'head_dim=128' 一致，但 N2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N28

## Claim

修正自矛盾检测：N28 的 KV Cache 计算中 '128' (head_dim) 与 N32 定义的架构参数 'head_dim=128' 一致，但 N28 的公式中 '64' (layers) 正确，然而 N28 声称结果为 8.59GB 是错误的；正确计算应为 64(layers) * 8(kv_heads) * 128(head_dim) * 32768(seq_len) * 2(K&V) * 2(bytes/BF16) = 17.18 GB，这与 N46/N47 中提到的 10-20GB 范围一致，N28 原数值低估了 50%。

## Corrected Claim

修正自矛盾检测：N28 的 KV Cache 计算中 '128' (head_dim) 与 N32 定义的架构参数 'head_dim=128' 一致，但 N28 的公式中 '64' (layers) 正确，然而 N28 声称结果为 8.59GB 是错误的；正确计算应为 64(layers) * 8(kv_heads) * 128(head_dim) * 32768(seq_len) * 2(K&V) * 2(bytes/BF16) = 17.18 GB，这与 N46/N47 中提到的 10-20GB 范围一致，N28 原数值低估了 50%。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 64*8*128*32768*2*2 = 17,179,869,184 bytes ≈ 17.18 GB，与陈述一致，且符合 BF16 KV Cache 标准计算公式。
