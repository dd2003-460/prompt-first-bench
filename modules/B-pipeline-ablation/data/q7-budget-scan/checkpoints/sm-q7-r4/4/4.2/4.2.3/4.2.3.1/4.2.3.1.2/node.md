# N456: 16TB CMR HDD 方案的 5 年电力成本 C_elec_CMR = P_total_CMR * 8760h * ¥0.6/kWh，其中 P_total_

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N202

## Claim

16TB CMR HDD 方案的 5 年电力成本 C_elec_CMR = P_total_CMR * 8760h * ¥0.6/kWh，其中 P_total_CMR = 26 * 4.5W (Active) + 90W (Infra) ≈ 207W，故 C_elec_CMR ≈ 207 * 8760 * 0.6 ≈ ¥1,084/年，5 年总计约 ¥5,420。

## Corrected Claim

16TB CMR HDD 方案的 5 年电力成本 C_elec_CMR = P_total_CMR * 8760h * ¥0.6/kWh，其中 P_total_CMR = 26 * 4.5W (Active) + 90W (Infra) ≈ 207W，故 C_elec_CMR ≈ 207 * 8760 * 0.6 ≈ ¥1,084/年，5 年总计约 ¥5,420。

## Evidence

先验知识/题面给定，逻辑校验通过：26*4.5+90=207W，207*8760*0.6≈1083.97元/年，5年≈5419.85元，计算无误且量级合理。
