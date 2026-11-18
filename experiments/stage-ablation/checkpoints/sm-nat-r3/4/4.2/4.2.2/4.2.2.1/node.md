# N145: 各热度分层（Top-1%, 1%-10%, 10%-90%, 90%-100%）的字节流量占比 ByteShare_k 的计算式：ByteShare_k = Σ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N62

## Claim

各热度分层（Top-1%, 1%-10%, 10%-90%, 90%-100%）的字节流量占比 ByteShare_k 的计算式：ByteShare_k = Σ_{i ∈ layer_k} (λ_i * s_i) / Σ_{i=1}^{10^5} (λ_i * s_i)，其中 λ_i 和 s_i 需基于 Pareto 分布参数 α=1.1, β=0.9 进行数值计算。

## Corrected Claim

各热度分层（Top-1%, 1%-10%, 10%-90%, 90%-100%）的字节流量占比 ByteShare_k 的计算式：ByteShare_k = Σ_{i ∈ layer_k} (λ_i * s_i) / Σ_{i=1}^{10^5} (λ_i * s_i)，其中 λ_i 和 s_i 需基于 Pareto 分布参数 α=1.1, β=0.9 进行数值计算。

## Evidence

先验知识/题面给定，逻辑校验通过
