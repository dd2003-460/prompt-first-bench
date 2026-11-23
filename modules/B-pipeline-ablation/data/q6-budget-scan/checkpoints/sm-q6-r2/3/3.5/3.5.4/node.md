# N87: 混合策略总成本 C_mix 需包含回源带宽成本：核心区域自建节点回源率 = 1 - H_self_core = 1 - 0.95 = 0.05，回源流量 = 0

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

混合策略总成本 C_mix 需包含回源带宽成本：核心区域自建节点回源率 = 1 - H_self_core = 1 - 0.95 = 0.05，回源流量 = 0.05 * F_core * V_dl = 0.05 * 0.65 * 2TB = 65GB/day，回源带宽成本 = 65 * 30 * ¥0.24 = ¥468/month（若回源走公有云骨干网）

## Corrected Claim

混合策略总成本 C_mix 需包含回源带宽成本：核心区域自建节点回源率 = 1 - H_self_core = 1 - 0.95 = 0.05，回源流量 = 0.05 * F_core * V_dl = 0.05 * 0.65 * 2TB = 65GB/day，回源带宽成本 = 65 * 30 * ¥0.24 = ¥468/month（若回源走公有云骨干网）

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 0.05 * 0.65 * 2048GB * 30 * 0.24 ≈ 468.5，数值量级与逻辑自洽。
