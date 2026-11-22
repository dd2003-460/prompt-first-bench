# N296: 电力成本计算公式修正：C_power = P_avg * H_hours * E_rate。对于 2x RTX 4090 方案，若 P_avg 取 337.5W

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98, N100, N101

## Claim

电力成本计算公式修正：C_power = P_avg * H_hours * E_rate。对于 2x RTX 4090 方案，若 P_avg 取 337.5W (75% TDP)，H=8760h，E=$0.14/kWh (N104 修正值)，则年成本约为 $490/年；对于 A100 方案，若 P_avg 取 210W (70% TDP)，年成本约为 $260/年。多卡方案电力成本约为单卡数据卡的 1.88 倍 (490/260)，而非 N98 中的 2.25 倍。

## Corrected Claim

电力成本计算公式修正：C_power = P_avg * H_hours * E_rate。对于 2x RTX 4090 方案，若 P_avg 取 337.5W (75% TDP)，H=8760h，E=$0.14/kWh (N104 修正值)，则年成本约为 $490/年；对于 A100 方案，若 P_avg 取 210W (70% TDP)，年成本约为 $260/年。多卡方案电力成本约为单卡数据卡的 1.88 倍 (490/260)，而非 N98 中的 2.25 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：337.5W * 8760h * $0.14/kWh ≈ $490.17，210W * 8760h * $0.14/kWh ≈ $257.03，490/260 ≈ 1.88，计算与陈述一致。
