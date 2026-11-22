# N74: 成交周期延长的非线性修正项：当曝光量 Q 降至 Q0 * 0.5 时，若低于买家搜索触发的最低阈值 Q_min，成交概率呈阶跃式下降而非线性，修正公式为 T' 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

成交周期延长的非线性修正项：当曝光量 Q 降至 Q0 * 0.5 时，若低于买家搜索触发的最低阈值 Q_min，成交概率呈阶跃式下降而非线性，修正公式为 T' = T0 * (1 + λ * 0.5) * (1 + γ * max(0, Q_min/Q0 - 0.5))，其中 γ 为阈值效应系数，通常 γ > 1。

## Corrected Claim

成交周期延长的非线性修正项：当曝光量 Q 降至 Q0 * 0.5 时，若低于买家搜索触发的最低阈值 Q_min，成交概率呈阶跃式下降而非线性，修正公式为 T' = T0 * (1 + λ * 0.5) * (1 + γ * max(0, Q_min/Q0 - 0.5))，其中 γ 为阈值效应系数，通常 γ > 1。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

search friction threshold effect transaction time nonlinearity
