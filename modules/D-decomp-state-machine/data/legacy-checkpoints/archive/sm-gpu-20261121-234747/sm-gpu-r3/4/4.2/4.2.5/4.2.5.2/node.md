# N307: 电力成本正态分布的方差量化：基于负载率ρ(t)的波动，假设ρ服从N(0.7, 0.1^2)，则年电力成本C_power = P_card * ρ * 8760 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N109

## Claim

电力成本正态分布的方差量化：基于负载率ρ(t)的波动，假设ρ服从N(0.7, 0.1^2)，则年电力成本C_power = P_card * ρ * 8760 * r，其标准差σ_power = P_card * σ_ρ * 8760 * r；对于4090（450W）和r=$0.15/kWh，σ_power ≈ $4.9/年

## Corrected Claim

电力成本正态分布的方差量化：基于负载率ρ(t)的波动，假设ρ服从N(0.7, 0.1^2)，则年电力成本C_power = P_card * ρ * 8760 * r，其标准差σ_power = P_card * σ_ρ * 8760 * r；对于4090（450W）和r=$0.15/kWh，σ_power ≈ $4.9/年

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

4090 GPU annual power cost standard deviation load factor 0.1
