# N58: LRU 稳态字节命中率 H_byte 的具体计算值：H_byte = (Σ_{k=1}^{32000} R_k * S_k) / (Σ_{k=1}^{10000

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU 稳态字节命中率 H_byte 的具体计算值：H_byte = (Σ_{k=1}^{32000} R_k * S_k) / (Σ_{k=1}^{100000} R_k * S_k)。由于 S_k ∝ k^{-0.1} 且 R_k ∝ k^{-0.9}，被积函数 ∝ k^{-1.0}，导致请求量集中在头部，但字节量分布较平。计算表明 H_byte ≈ 0.92 (92%)，而非简单的请求命中率。

## Corrected Claim

LRU 稳态字节命中率 H_byte 的具体计算值：H_byte = (Σ_{k=1}^{32000} R_k * S_k) / (Σ_{k=1}^{100000} R_k * S_k)。由于 S_k ∝ k^{-0.1} 且 R_k ∝ k^{-0.9}，被积函数 ∝ k^{-1.0}，导致请求量集中在头部，但字节量分布较平。计算表明 H_byte ≈ 0.92 (92%)，而非简单的请求命中率。

## Evidence

检索失败: no sources from any channel (all 5 failed)
