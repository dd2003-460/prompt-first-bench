# N309: 修正后的单次扫描性能惩罚增量成本 C_penalty_single = (T_read_hdd_misjudge - T_read_ssd_base) * Cl

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

修正后的单次扫描性能惩罚增量成本 C_penalty_single = (T_read_hdd_misjudge - T_read_ssd_base) * Cluster_Hourly_Cost * Scan_Freq_Daily；代入N133和N134的数值：ΔT = 0.54h - 0.198h = 0.342h；C_penalty_single_daily = 0.342h * ¥5000/h * 2次/天 ≈ ¥3,420/天；年化成本 C_penalty_yearly = ¥3,420 * 365 ≈ ¥1,248,300/年（远小于N104原估算的¥41M/年，证明聚合吞吐是关键修正项）。

## Corrected Claim

修正后的单次扫描性能惩罚增量成本 C_penalty_single = (T_read_hdd_misjudge - T_read_ssd_base) * Cluster_Hourly_Cost * Scan_Freq_Daily；代入N133和N134的数值：ΔT = 0.54h - 0.198h = 0.342h；C_penalty_single_daily = 0.342h * ¥5000/h * 2次/天 ≈ ¥3,420/天；年化成本 C_penalty_yearly = ¥3,420 * 365 ≈ ¥1,248,300/年（远小于N104原估算的¥41M/年，证明聚合吞吐是关键修正项）。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（0.342 * 5000 * 2 = 3420; 3420 * 365 = 1,248,300），量纲一致，且符合成本计算的基本逻辑。
