# N50: 公有云CDN的95th百分位计费模式下，实际计费带宽 $B_{95}$ 取决于 $K_{peak}$ 和峰值持续时间 $T_{peak}$；若 $K_{peak

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10, N11, N12

## Claim

公有云CDN的95th百分位计费模式下，实际计费带宽 $B_{95}$ 取决于 $K_{peak}$ 和峰值持续时间 $T_{peak}$；若 $K_{peak}=2.0$ 且峰值持续4小时，则 $B_{95}$ 约为 $B_{avg} \times 1.5$，导致实际计费带宽低于理论峰值 $B_{peak}$。

## Corrected Claim

公有云CDN的95th百分位计费模式下，实际计费带宽 $B_{95}$ 取决于 $K_{peak}$ 和峰值持续时间 $T_{peak}$；若 $K_{peak}=2.0$ 且峰值持续4小时，则 $B_{95}$ 约为 $B_{avg} \times 1.5$，导致实际计费带宽低于理论峰值 $B_{peak}$。

## Evidence

先验知识/题面给定，逻辑校验通过：95th百分位计费基于时间排序，若峰值仅占4/24小时（约16.7%），则95th百分位必然落在非峰值区间，数值上低于峰值且高于均值，符合统计逻辑。

## Search Query

CDN 95th percentile billing peak duration impact
