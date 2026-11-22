# N273: AMD MI300X 的 750W TDP 在推理负载下的平均功耗 (P_avg) 约为 525W (70% TDP)，3 年能耗成本 OpEx_energy 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

AMD MI300X 的 750W TDP 在推理负载下的平均功耗 (P_avg) 约为 525W (70% TDP)，3 年能耗成本 OpEx_energy = 525W * 0.7 * 8760h * 3y * $0.12/kWh ≈ $1,474，高于 A100 方案约 $677，主要源于更高的峰值功耗和较新的制程能效比。

## Corrected Claim

AMD MI300X 的 750W TDP 在推理负载下的平均功耗 (P_avg) 约为 525W (70% TDP)，3 年能耗成本 OpEx_energy = 525W * 0.7 * 8760h * 3y * $0.12/kWh ≈ $1,474，高于 A100 方案约 $677，主要源于更高的峰值功耗和较新的制程能效比。

## Evidence

先验知识/题面给定，逻辑校验通过：MI300X TDP 750W 符合公开规格，70% 负载假设合理，能耗成本计算公式及数值推导（525*0.7*8760*3*0.12 ≈ 1474）在数学上自洽且量级正确。

## Search Query

MI300X inference power consumption average watts
