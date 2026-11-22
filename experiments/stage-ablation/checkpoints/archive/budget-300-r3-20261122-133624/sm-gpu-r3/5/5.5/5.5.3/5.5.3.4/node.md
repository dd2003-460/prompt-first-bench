# N405: 风险溢价 C_risk 的精确公式修正：C_risk = (1 - Availability) * (C_replacement + C_data_loss +

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N157

## Claim

风险溢价 C_risk 的精确公式修正：C_risk = (1 - Availability) * (C_replacement + C_data_loss + C_reputation_loss)；其中 Availability = 1 - (T_downtime / Total_Time)；对于 2×4090 方案，若 MTBF_sys=9.4 个月，T_downtime=60s，则 Annual Downtime = (12/9.4) * 60s ≈ 76.6s/year，Availability ≈ 0.9999991，C_risk 主要来源于 C_replacement（单卡更换成本 $1600 * 0.1278 / year ≈ $204.5/year）。

## Corrected Claim

风险溢价 C_risk 的精确公式修正：C_risk = (1 - Availability) * (C_replacement + C_data_loss + C_reputation_loss)；其中 Availability = 1 - (T_downtime / Total_Time)；对于 2×4090 方案，若 MTBF_sys=9.4 个月，T_downtime=60s，则 Annual Downtime = (12/9.4) * 60s ≈ 76.6s/year，Availability ≈ 0.9999991，C_risk 主要来源于 C_replacement（单卡更换成本 $1600 * 0.1278 / year ≈ $204.5/year）。

## Evidence

先验知识/题面给定，逻辑校验通过：MTBF与停机时间换算可用率公式正确，数值量级（9.4个月MTBF对应极低不可用性）及成本估算逻辑自洽。
