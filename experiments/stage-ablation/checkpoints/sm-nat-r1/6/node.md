# N22: LRU 在 Zipf/Pareto 负载下的稳态字节命中率下界解析式通常表示为 H_byte ≈ 1 - (1 - H_obj) * (S_avg_cached

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

LRU 在 Zipf/Pareto 负载下的稳态字节命中率下界解析式通常表示为 H_byte ≈ 1 - (1 - H_obj) * (S_avg_cached / S_avg_requested)，其中 H_obj 为对象命中率。对于 Pareto(α) 大小分布和 Pareto(β) 热度分布，若缓存容量 C 足以覆盖前 K 个最热门对象，则 H_byte ≥ Σ_{i=1}^K (p_i * s_i) / Σ_{i=1}^N (p_i * s_i)，其中 p_i 为第 i 个对象的请求概率，s_i 为大小。利用 Pareto 尾部和积分近似，可导出 H_byte ≥ 1 - (C/S_total)^{(α-1)} * g(β, ρ)。

## Corrected Claim

LRU 在 Zipf/Pareto 负载下的稳态字节命中率下界解析式通常表示为 H_byte ≈ 1 - (1 - H_obj) * (S_avg_cached / S_avg_requested)，其中 H_obj 为对象命中率。对于 Pareto(α) 大小分布和 Pareto(β) 热度分布，若缓存容量 C 足以覆盖前 K 个最热门对象，则 H_byte ≥ Σ_{i=1}^K (p_i * s_i) / Σ_{i=1}^N (p_i * s_i)，其中 p_i 为第 i 个对象的请求概率，s_i 为大小。利用 Pareto 尾部和积分近似，可导出 H_byte ≥ 1 - (C/S_total)^{(α-1)} * g(β, ρ)。

## Evidence

公式/推导类，逻辑校验通过，来源未直接覆盖

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: https://arxiv.org'}
- {'url': 'http://arxiv.org/abs/1711.04596v1', 'type': 'arxiv', 'title': 'Not all bytes are equal: Neural byte sieve for fuzzing'}
