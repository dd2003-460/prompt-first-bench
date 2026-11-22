# N90: 平台盈亏平衡点 ΔR_threshold 的求解方程：ΔR_threshold * GMV_total * take_rate = Δs_churn * GMV

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

平台盈亏平衡点 ΔR_threshold 的求解方程：ΔR_threshold * GMV_total * take_rate = Δs_churn * GMV_high * take_rate，解得 ΔR_threshold = (Δs_churn * GMV_high) / GMV_total，需代入 r_high 和 GMV 分布参数计算具体阈值。

## Corrected Claim

平台盈亏平衡点 ΔR_threshold 的求解方程：ΔR_threshold * GMV_total * take_rate = Δs_churn * GMV_high * take_rate，解得 ΔR_threshold = (Δs_churn * GMV_high) / GMV_total，需代入 r_high 和 GMV 分布参数计算具体阈值。

## Evidence

先验知识/题面给定，逻辑校验通过
