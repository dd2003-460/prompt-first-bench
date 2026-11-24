# N351: 双盘并发故障概率 P_dual_fault_yearly 估算：在 RAID6 中，系统崩溃需两盘同时故障。假设故障独立，P_dual ≈ C(N,2) * λ

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N155

## Claim

双盘并发故障概率 P_dual_fault_yearly 估算：在 RAID6 中，系统崩溃需两盘同时故障。假设故障独立，P_dual ≈ C(N,2) * λ_single^2 = (120*119/2) * (0.00438)^2 ≈ 7140 * 0.0000192 ≈ 0.137 次/年。即约 7.3 年发生一次导致数据丢失的双盘故障事件，这是 RTO 代价中最高风险的部分。

## Corrected Claim

双盘并发故障概率 P_dual_fault_yearly 估算：在 RAID6 中，系统崩溃需两盘同时故障。假设故障独立，P_dual ≈ C(N,2) * λ_single^2 = (120*119/2) * (0.00438)^2 ≈ 7140 * 0.0000192 ≈ 0.137 次/年。即约 7.3 年发生一次导致数据丢失的双盘故障事件，这是 RTO 代价中最高风险的部分。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 C(120,2)=7140，λ^2≈1.918e-5，乘积≈0.137，倒数≈7.3，数值与逻辑均自洽。
