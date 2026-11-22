# N74: 计算噪声方差占比：σ_noise² / σ_total² = Var(P_actual - P_avg) / Var(P_actual)，若该比值 > 0.5 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

计算噪声方差占比：σ_noise² / σ_total² = Var(P_actual - P_avg) / Var(P_actual)，若该比值 > 0.5 则判定噪声主导，否则信号主导。

## Corrected Claim

计算噪声方差占比：σ_noise² / σ_total² = Var(P_actual - P_avg) / Var(P_actual)，若该比值 > 0.5 则判定噪声主导，否则信号主导。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1和2基于阈值0.5互斥地覆盖了‘噪声主导’与‘信号主导’两种确定性状态，子节点3独立处理了统计不确定性（灰色地带）及边界情况，三者逻辑上互斥且无重叠，共同构成了对父节点判定逻辑的完整覆盖。虽然子节点1和2在形式上类似，但分别对应不同的业务策略（低置信度/高透明度 vs 高置信度/算法纠偏），属于必要的分支而非单纯参数冗余。）
