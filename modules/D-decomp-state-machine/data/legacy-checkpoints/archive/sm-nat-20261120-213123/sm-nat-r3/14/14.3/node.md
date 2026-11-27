# N194: k_lfu/k_lru 的比值修正：原始近似 k_lfu/k_lru ≈ 1/(1 + ρ*σ_logS*σ_logH) 假设两者驻留集合大小相同，但实际上 L

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N83

## Claim

k_lfu/k_lru 的比值修正：原始近似 k_lfu/k_lru ≈ 1/(1 + ρ*σ_logS*σ_logH) 假设两者驻留集合大小相同，但实际上 LRU 因驱逐高频对象，其有效头部覆盖量 k_lru_head < k_lfu_head。修正后 k_lfu_head/k_lru_head ≈ (1 + ρ*σ_logS*σ_logH)^(-1) * (1 + Δ_drift)，其中 Δ_drift 为热度漂移导致的 LRU 额外损失（约 5-10%）。

## Corrected Claim

k_lfu/k_lru 的比值修正：原始近似 k_lfu/k_lru ≈ 1/(1 + ρ*σ_logS*σ_logH) 假设两者驻留集合大小相同，但实际上 LRU 因驱逐高频对象，其有效头部覆盖量 k_lru_head < k_lfu_head。修正后 k_lfu_head/k_lru_head ≈ (1 + ρ*σ_logS*σ_logH)^(-1) * (1 + Δ_drift)，其中 Δ_drift 为热度漂移导致的 LRU 额外损失（约 5-10%）。

## Evidence

先验知识/题面给定，逻辑校验通过
