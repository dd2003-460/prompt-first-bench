# N641: RTO=4h 目标下 NVMe 热备策略的合规性差距成本 C_gap_rto：若采用热备，T_actual ≈ 0h，无差距成本；但若采用冷备 (Cold St

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N222

## Claim

RTO=4h 目标下 NVMe 热备策略的合规性差距成本 C_gap_rto：若采用热备，T_actual ≈ 0h，无差距成本；但若采用冷备 (Cold Standby)，T_actual = T_boot + T_sync ≈ 2h + 1h = 3h，仍满足 4h；若采用温备 (Warm Standby)，T_actual = 4h，刚好达标；若实际 T_actual = 6h，则 C_gap_rto = (6 - 4) * Business_Loss_Per_Hour = 2 * ¥50,000 = ¥100,000/次故障。

## Corrected Claim

RTO=4h 目标下 NVMe 热备策略的合规性差距成本 C_gap_rto：若采用热备，T_actual ≈ 0h，无差距成本；但若采用冷备 (Cold Standby)，T_actual = T_boot + T_sync ≈ 2h + 1h = 3h，仍满足 4h；若采用温备 (Warm Standby)，T_actual = 4h，刚好达标；若实际 T_actual = 6h，则 C_gap_rto = (6 - 4) * Business_Loss_Per_Hour = 2 * ¥50,000 = ¥100,000/次故障。

## Evidence

先验知识/题面给定，逻辑校验通过：RTO差距成本计算公式及数值代入（(6-4)*50000=100000）逻辑自洽，符合灾备恢复时间目标（RTO）的基本定义与成本估算逻辑。
