# N153: LFU 增益的来源分解：Δ_H = Δ_H_capacity + Δ_H_pollution，其中 Δ_H_capacity（容量优化增益）≈ 2.5 个百分点

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

LFU 增益的来源分解：Δ_H = Δ_H_capacity + Δ_H_pollution，其中 Δ_H_capacity（容量优化增益）≈ 2.5 个百分点，来自 LFU 优先保留高频小对象；Δ_H_pollution（污染减少增益）≈ 0.7 个百分点，来自避免低频大对象驱逐高频小对象。

## Corrected Claim

LFU 增益的来源分解：Δ_H = Δ_H_capacity + Δ_H_pollution，其中 Δ_H_capacity（容量优化增益）≈ 2.5 个百分点，来自 LFU 优先保留高频小对象；Δ_H_pollution（污染减少增益）≈ 0.7 个百分点，来自避免低频大对象驱逐高频小对象。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU cache pollution reduction gain decomposition
