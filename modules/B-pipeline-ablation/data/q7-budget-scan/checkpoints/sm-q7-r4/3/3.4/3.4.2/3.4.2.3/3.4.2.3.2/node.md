# N651: 日均写入 10TB 的瞬时波动系数：实际每小时写入量 W_h 服从非均匀分布，设变异系数 CV = σ_W / μ_W；若 CV=0.5，则最大小时写入量 Ma

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N225

## Claim

日均写入 10TB 的瞬时波动系数：实际每小时写入量 W_h 服从非均匀分布，设变异系数 CV = σ_W / μ_W；若 CV=0.5，则最大小时写入量 Max_W ≈ μ_W * (1+2σ) ≈ 10TB/24 * 2 ≈ 0.83TB/h；增量恢复阈值 V_inc 应设为 Max_W * T_max_recovery_window，以确保在最大波动下仍能增量恢复。

## Corrected Claim

日均写入 10TB 的瞬时波动系数：实际每小时写入量 W_h 服从非均匀分布，设变异系数 CV = σ_W / μ_W；若 CV=0.5，基于正态分布近似，最大小时写入量 Max_W ≈ μ_W * (1+2σ) ≈ 10TB/24 * 2 ≈ 0.83TB/h；但在重尾分布场景下，建议采用更保守的分位数（如99.9%分位）或历史峰值数据来设定 Max_W，增量恢复阈值 V_inc 应设为 Max_W * T_max_recovery_window，以确保在极端波动下仍能增量恢复。

## Evidence

[质询]统计假设过于简化：将最大小时写入量近似为均值加两倍标准差（Max_W ≈ μ_W * (1+2σ)）隐含了正态分布假设，但网络流量和写入负载通常服从重尾分布（如Pareto或Log-normal），实际峰值往往远超2σ范围（可能达到5-10σ），导致估算的最大写入量严重偏低，进而使恢复窗口设置不足。 | 先验知识/题面给定，逻辑校验通过（算术计算正确：10/24*2≈0.83），但统计模型假设存在经验性风险，缺乏来源支持其普适性。

## Search Query

write workload variability coefficient of variation hourly
