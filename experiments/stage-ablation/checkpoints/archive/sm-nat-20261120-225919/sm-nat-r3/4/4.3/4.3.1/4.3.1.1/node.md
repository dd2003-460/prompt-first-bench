# N183: 工作点 A（高命中低驻留）：假设字节命中率 H_byte=0.9，则未命中字节流率 = 5e7 * 0.1 * E[S|miss]。若 E[S|miss] ≈ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

工作点 A（高命中低驻留）：假设字节命中率 H_byte=0.9，则未命中字节流率 = 5e7 * 0.1 * E[S|miss]。若 E[S|miss] ≈ 20KB（冷对象较大），则 τ_res = 128e9 / (5e7 * 0.1 * 20e3) = 128 天。此时缓存内容稳定，LRU 淘汰主要受新对象加入驱动，而非容量压力。

## Corrected Claim

工作点 A（高命中低驻留）：假设字节命中率 H_byte=0.9，则未命中字节流率 = 5e7 * 0.1 * E[S|miss]。若 E[S|miss] ≈ 20KB（冷对象较大），则 τ_res = 128e9 / (5e7 * 0.1 * 20e3) = 128 天。此时缓存内容稳定，LRU 淘汰主要受新对象加入驱动，而非容量压力。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 128e9 / (5e7 * 0.1 * 20e3) = 128e9 / 1e8 = 128 正确；量纲与物理直觉（高命中率导致低未命中流量，从而长驻留时间）自洽。
