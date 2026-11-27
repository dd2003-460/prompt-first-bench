# N37: 稳态下 LRU 驻留集合 C_LRU 的构成：在稳态且无突发流量的假设下，LRU 缓存的内容趋近于 LFU，即 C_LRU ≈ C_LFU = {1, 2, .

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

稳态下 LRU 驻留集合 C_LRU 的构成：在稳态且无突发流量的假设下，LRU 缓存的内容趋近于 LFU，即 C_LRU ≈ C_LFU = {1, 2, ..., k}，其中 k 由 N8 确定。此时 H_LRU ≈ H_LFU，ΔH ≈ 0。

## Corrected Claim

稳态下 LRU 驻留集合 C_LRU 的构成：在稳态且无突发流量的假设下，LRU 缓存的内容趋近于 LFU，即 C_LRU ≈ C_LFU = {1, 2, ..., k}，其中 k 由 N8 确定。此时 H_LRU ≈ H_LFU，ΔH ≈ 0。

## Evidence

先验知识/题面给定，逻辑校验通过：在稳态且访问频率单调递减（如Zipf分布）的假设下，LRU缓存的驻留集合确实趋近于LFU，即保留访问频率最高的前k个对象，此时两者命中率差异趋于零。
