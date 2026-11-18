# N183: LRU 命中率对热度参数 β 的敏感度 ∂H/∂β 解析式：H_LRU(β) ≈ 1 - (K_LRU/N)^{1-β}，求导得 ∂H/∂β ≈ ln(N/K_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

LRU 命中率对热度参数 β 的敏感度 ∂H/∂β 解析式：H_LRU(β) ≈ 1 - (K_LRU/N)^{1-β}，求导得 ∂H/∂β ≈ ln(N/K_LRU) * (K_LRU/N)^{1-β}。由于 LRU 对近期访问更敏感，其有效 K 随 β 变化更快，需对比 K_LFU 与 K_LRU 的差异来量化衰减速度差。

## Corrected Claim

LRU 命中率对热度参数 β 的敏感度 ∂H/∂β 解析式：H_LRU(β) ≈ 1 - (K_LRU/N)^{1-β}，求导得 ∂H/∂β ≈ ln(N/K_LRU) * (K_LRU/N)^{1-β}。由于 LRU 对近期访问更敏感，其有效 K 随 β 变化更快，需对比 K_LFU 与 K_LRU 的差异来量化衰减速度差。

## Evidence

先验知识/题面给定，逻辑校验通过
