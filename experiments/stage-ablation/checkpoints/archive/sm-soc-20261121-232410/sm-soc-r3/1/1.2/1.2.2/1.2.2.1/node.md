# N104: 验证 β_risk 样本量 n=5000 的统计功效：在效应量 d=0.3/0.1=3 的情况下，t-statistic = (0.31-0.30)/(0.09

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

验证 β_risk 样本量 n=5000 的统计功效：在效应量 d=0.3/0.1=3 的情况下，t-statistic = (0.31-0.30)/(0.09/sqrt(5000)) ≈ 7.86，p-value < 0.001，确认均值显著偏离0

## Corrected Claim

验证 β_risk 样本量 n=5000 的统计功效：在效应量 d=0.3/0.1=3 的情况下，t-statistic = (0.31-0.30)/(0.09/sqrt(5000)) ≈ 7.86，p-value < 0.001，确认均值显著偏离0

## Evidence

先验知识/题面给定，逻辑校验通过：t统计量计算 (0.01)/(0.09/√5000) ≈ 7.86 正确，大样本下 p<0.001 结论合理
