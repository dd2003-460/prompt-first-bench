# N90: 平台盈亏平衡点 ΔR_threshold 的求解方程：ΔR_threshold * GMV_total * take_rate = Δs_churn * GMV

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23

## Claim

平台盈亏平衡点 ΔR_threshold 的求解方程：ΔR_threshold * GMV_total * take_rate = Δs_churn * GMV_high * take_rate，解得 ΔR_threshold = (Δs_churn * GMV_high) / GMV_total，需代入 r_high 和 GMV 分布参数计算具体阈值。

## Corrected Claim

平台盈亏平衡点 ΔR_threshold 的求解方程：ΔR_threshold * GMV_total * take_rate = Δs_churn * GMV_high * take_rate，解得 ΔR_threshold = (Δs_churn * GMV_high) / GMV_total，需代入 r_high 和 GMV 分布参数计算具体阈值。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别定义了公式中的关键变量 GMV_high、Δs_churn 以及最终的计算实例，三者功能独立且互不重叠，共同覆盖了父节点公式的求解要素和具体应用。）
