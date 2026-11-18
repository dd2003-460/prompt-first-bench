# N149: 工作点 C（中性更新/基准折损）：假设更新率与热度独立（ρ_update_heat = 0），u_eff = 0.01/day。全局平均驻留时间 T_avg 由

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

工作点 C（中性更新/基准折损）：假设更新率与热度独立（ρ_update_heat = 0），u_eff = 0.01/day。全局平均驻留时间 T_avg 由容量和未命中率决定，若 T_avg ≈ 0.1 day，则平均失效概率 R_inv ≈ 0.001。此工作点作为基准，用于量化正/负相关场景下的相对增益/损失幅度（即 C_miss/C_total 相对于基准的偏离度）。

## Corrected Claim

工作点 C（中性更新/基准折损）：假设更新率与热度独立（ρ_update_heat = 0），u_eff = 0.01/day。全局平均驻留时间 T_avg 由容量和未命中率决定，若 T_avg ≈ 0.1 day，则平均失效概率 R_inv ≈ 0.001。此工作点作为基准，用于量化正/负相关场景下的相对增益/损失幅度（即 C_miss/C_total 相对于基准的偏离度）。

## Evidence

先验知识/题面给定，逻辑校验通过
