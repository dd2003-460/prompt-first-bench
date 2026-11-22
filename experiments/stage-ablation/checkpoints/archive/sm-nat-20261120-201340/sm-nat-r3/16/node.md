# N165: LRU稳态字节命中率下界的数学模型应表述为 H_byte_LRU = 1 - (Σ_{i∉Cache} r_i * s_i) / (Σ_{i=1}^{N} r_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU稳态字节命中率下界的数学模型应表述为 H_byte_LRU = 1 - (Σ_{i∉Cache} r_i * s_i) / (Σ_{i=1}^{N} r_i * s_i)，其中Cache集合由LRU策略在稳态下保留的对象组成；在缓存容量C=128GB且W_total≈10.72GB的充分覆盖场景下，理论下界为1.0，但若考虑更新导致的失效，下界需修正为 H_eff = H_byte_LRU * (1 - P_stale_weighted)，其中P_stale_weighted是请求频率加权的失效概率。

## Corrected Claim

LRU稳态字节命中率下界的数学模型应表述为 H_byte_LRU = 1 - (Σ_{i∉Cache} r_i * s_i) / (Σ_{i=1}^{N} r_i * s_i)，其中Cache集合由LRU策略在稳态下保留的对象组成；在缓存容量C=128GB且W_total≈10.72GB的充分覆盖场景下，理论下界为1.0，但若考虑更新导致的失效，下界需修正为 H_eff = H_byte_LRU * (1 - P_stale_weighted)，其中P_stale_weighted是请求频率加权的失效概率。

## Evidence

检索失败: no sources from any channel (all 5 failed)
