# N347: QoE 评分模型中，P99 延迟 T 与用户主观满意度评分 S 的定量关系公式：S = 100 - k_qoe * max(0, T - T_threshold

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N109

## Claim

QoE 评分模型中，P99 延迟 T 与用户主观满意度评分 S 的定量关系公式：S = 100 - k_qoe * max(0, T - T_threshold)，其中 T_threshold 为感知阈值（通常 200ms），k_qoe 为敏感度系数（约 0.5-1.0 分/ms），当 S < 80 时视为不合规

## Corrected Claim

QoE 评分模型中，P99 延迟 T 与用户主观满意度评分 S 的定量关系公式：S = 100 - k_qoe * max(0, T - T_threshold)，其中 T_threshold 为感知阈值（通常 200ms），k_qoe 为敏感度系数（约 0.5-1.0 分/ms），当 S < 80 时视为不合规

## Evidence

先验知识/题面给定，逻辑校验通过
