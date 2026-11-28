# N26: 统计异常判定：计算 450 W/(m·K) 相对于铝合金均值 (190) 的 z-score = (450-190)/σ，若取 σ≈15 W/(m·K)，z=1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13, N15, N16

## Claim

统计异常判定：计算 450 W/(m·K) 相对于铝合金均值 (190) 的 z-score = (450-190)/σ，若取 σ≈15 W/(m·K)，z=17.3，远超 3σ 阈值，确认为离群值

## Corrected Claim

统计异常判定：计算 450 W/(m·K) 相对于铝合金均值 (190) 的 z-score = (450-190)/σ，若取 σ≈15 W/(m·K)，z=17.3，远超 3σ 阈值，确认为离群值

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 (450-190)/15 = 17.33 正确，且 17.3 > 3 符合统计学离群值判定标准。

## Search Query

statistical outlier detection z-score threshold 3sigma
