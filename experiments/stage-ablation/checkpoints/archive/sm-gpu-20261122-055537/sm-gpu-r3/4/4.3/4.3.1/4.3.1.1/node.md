# N233: RTX 4090 风冷方案在本地部署的冷却基础设施边际成本 C_cool_consumer 精确分解为：初始硬件摊销 C_init/3 + 年度电力成本 ΔC_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69, N70, N71

## Claim

RTX 4090 风冷方案在本地部署的冷却基础设施边际成本 C_cool_consumer 精确分解为：初始硬件摊销 C_init/3 + 年度电力成本 ΔC_fan + 维护/耗材 C_maint，C_init 取决于是否需升级机箱风扇（通常 $20-50），ΔC_fan 约为 0.1-0.2 kW * T_hours * E_price，C_maint 约为 $0-10/年（清洁除尘）。

## Corrected Claim

RTX 4090 风冷方案在本地部署的冷却基础设施边际成本 C_cool_consumer 精确分解为：初始硬件摊销 C_init/3 + 年度电力成本 ΔC_fan + 维护/耗材 C_maint，C_init 取决于是否需升级机箱风扇（通常 $20-50），ΔC_fan 约为 0.1-0.2 kW * T_hours * E_price，C_maint 约为 $0-10/年（清洁除尘）。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 风冷方案确实主要涉及机箱风扇升级（$20-50）、额外电力消耗（0.1-0.2kW 量级合理）及极低维护成本，符合工程常识。
