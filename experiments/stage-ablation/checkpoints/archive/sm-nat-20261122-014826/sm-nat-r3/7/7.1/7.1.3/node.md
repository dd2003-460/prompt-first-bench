# N152: LRU 稳态收敛时间常数 τ_seq：基于 LRU 栈深度分布，收敛所需的请求序列长度 N_seq ≈ k * τ_seq，其中 k 为收敛系数（通常 k≈3-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N56, N57, N58

## Claim

LRU 稳态收敛时间常数 τ_seq：基于 LRU 栈深度分布，收敛所需的请求序列长度 N_seq ≈ k * τ_seq，其中 k 为收敛系数（通常 k≈3-5 对应 95%-99% 置信度），τ_seq 取决于缓存内对象的平均访问间隔。

## Corrected Claim

LRU 稳态收敛时间常数 τ_seq：基于 LRU 栈深度分布，收敛所需的请求序列长度 N_seq ≈ k * τ_seq，其中 k 为收敛系数（通常 k≈3-5 对应 95%-99% 置信度），τ_seq 取决于缓存内对象的平均访问间隔。

## Evidence

先验知识/题面给定，逻辑校验通过
