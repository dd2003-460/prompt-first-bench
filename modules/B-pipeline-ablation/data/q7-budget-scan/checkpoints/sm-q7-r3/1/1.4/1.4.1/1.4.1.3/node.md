# N155: 7.68TB SSD 方案的故障域风险：单盘故障概率 P_fault_per_disk = 1/MTBF，若 MTBF=1,000,000 小时，年故障率 ≈ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

7.68TB SSD 方案的故障域风险：单盘故障概率 P_fault_per_disk = 1/MTBF，若 MTBF=1,000,000 小时，年故障率 ≈ 0.0000876/盘/年，119 块盘年故障期望值 = 0.0104 次/年，即约 96 年发生一次故障，RTO 影响极低。

## Corrected Claim

7.68TB SSD 方案的故障域风险：单盘故障概率 P_fault_per_disk = 1/MTBF，若 MTBF=1,000,000 小时，年故障率 ≈ 0.0000876/盘/年，119 块盘年故障期望值 = 0.0104 次/年，即约 96 年发生一次故障，RTO 影响极低。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程正确（1/1000000 * 8760 * 119 ≈ 0.01042，倒数约为95.9年），符合可靠性工程基本逻辑。
