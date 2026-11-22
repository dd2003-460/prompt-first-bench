# N22: LRU 稳态字节命中率下界 H_LRU_lb 的积分表达式：H_LRU_lb = (∫_0^{K_max} f_size(s) * f_rank(r(s)) *

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU 稳态字节命中率下界 H_LRU_lb 的积分表达式：H_LRU_lb = (∫_0^{K_max} f_size(s) * f_rank(r(s)) * s ds) / (∫_0^∞ f_size(s) * f_rank(r(s)) * s ds)，其中 r(s) 是大小为 s 的对象对应的热度排名，K_max 为容量限制下的最大驻留对象数，分母为总请求字节数。

## Corrected Claim

LRU 稳态字节命中率下界 H_LRU_lb 的积分表达式：H_LRU_lb = (∫_0^{K_max} f_size(s) * f_rank(r(s)) * s ds) / (∫_0^∞ f_size(s) * f_rank(r(s)) * s ds)，其中 r(s) 是大小为 s 的对象对应的热度排名，K_max 为容量限制下的最大驻留对象数，分母为总请求字节数。

## Evidence

父节点级核验失败（LLM 错误）：curl rc=28 b''
