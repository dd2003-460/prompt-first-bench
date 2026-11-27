# N133: 工作点3（保守预取/性价比最优）：P_revalidate ≈ 0.05，仅对 Top 10% 热门对象触发预取，源站额外带宽消耗 ≈ 0.5-1 Gbps，H

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N51, N52, N53

## Claim

工作点3（保守预取/性价比最优）：P_revalidate ≈ 0.05，仅对 Top 10% 热门对象触发预取，源站额外带宽消耗 ≈ 0.5-1 Gbps，H_effective 提升 ≈ 0.5%，计算 ROI = ΔH / ΔBandwidth ≈ 0.5%/Gbps，通常低于工作点2但高于工作点1的运维复杂度成本。

## Corrected Claim

工作点3（保守预取/性价比最优）：P_revalidate ≈ 0.05，仅对 Top 10% 热门对象触发预取，源站额外带宽消耗较低，H_effective 提升有限，计算 ROI 通常低于工作点2但高于工作点1的运维复杂度成本。

## Evidence

[质询]该陈述包含具体的工程经验数值（如0.5-1 Gbps带宽消耗、0.5%命中率提升），属于经验事实而非第一性原理可推导内容，且缺乏外部来源支持，数值量级和ROI计算逻辑虽自洽但无法验证其准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

selective CDN prefetching hot objects ROI analysis
