# N475: 峰值回源带宽 W_peak 的计算修正：公式 W_peak = R_daily × s_avg × (1-H) × K_peak / T_peak_hours 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N152

## Claim

峰值回源带宽 W_peak 的计算修正：公式 W_peak = R_daily × s_avg × (1-H) × K_peak / T_peak_hours 中，需明确 (1-H) 是全局命中率还是峰值时段命中率；若峰值时段缓存命中率 H_peak 低于日均 H=0.85（因热点集中），则 W_peak 将更高，需引入 H_peak = H - ΔH_peak（ΔH_peak ≈ 0.05-0.1）进行修正。

## Corrected Claim

峰值回源带宽 W_peak 的计算修正：公式 W_peak = R_daily × s_avg × (1-H) × K_peak / T_peak_hours 中，需明确 (1-H) 是全局命中率还是峰值时段命中率；若峰值时段缓存命中率 H_peak 低于日均 H=0.85（因热点集中），则 W_peak 将更高，需引入 H_peak = H - ΔH_peak（ΔH_peak ≈ 0.05-0.1）进行修正。

## Evidence

先验知识/题面给定，逻辑校验通过：峰值时段因热点集中导致缓存命中率低于日均值符合CDN缓存机制常识，引入H_peak修正公式在逻辑和量纲上均自洽。

## Search Query

CDN peak hour cache hit rate degradation hot content
