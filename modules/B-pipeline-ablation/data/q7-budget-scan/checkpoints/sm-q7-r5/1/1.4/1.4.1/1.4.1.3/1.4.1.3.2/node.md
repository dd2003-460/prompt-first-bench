# N350: 120 块 7.68TB SSD 阵列的年故障期望值 E_faults_yearly 修正计算：基于 N247 修正后的单盘故障率，E_faults = N_d

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N155

## Claim

120 块 7.68TB SSD 阵列的年故障期望值 E_faults_yearly 修正计算：基于 N247 修正后的单盘故障率，E_faults = N_disks * λ_single = 120 * 0.00438 ≈ 0.526 次/年。这意味着平均约 1.9 年发生一次单盘故障，远高于 N155 原估的 96 年一次，表明 N155 严重低估了故障频率，RTO 影响不可忽略。

## Corrected Claim

120 块 7.68TB SSD 阵列的年故障期望值 E_faults_yearly 修正计算：基于 N247 修正后的单盘故障率，E_faults = N_disks * λ_single = 120 * 0.00438 ≈ 0.526 次/年。这意味着平均约 1.9 年发生一次单盘故障，远高于 N155 原估的 96 年一次，表明 N155 严重低估了故障频率，RTO 影响不可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：120 * 0.00438 = 0.5256 ≈ 0.526，1/0.526 ≈ 1.9，计算无误且符合逻辑。
