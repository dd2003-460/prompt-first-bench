# N154: AMD Instinct MI300X 的 OpEx 计算：年电费 = 750W (TDP) * 0.9 * 8760h * $0.15/kWh ≈ $8,85

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

AMD Instinct MI300X 的 OpEx 计算：年电费 = 750W (TDP) * 0.9 * 8760h * $0.15/kWh ≈ $8,858/年；5年 OpEx ≈ $44,290。其能效比（Tokens/Watt）需结合 ROCm 实测吞吐量计算，若 ROCm 优化不佳导致吞吐量仅为 H200 的 70%，则单位 Token 电费将显著高于 NVIDIA 方案。

## Corrected Claim

AMD Instinct MI300X 的 OpEx 计算：年电费 = 750W (TDP) * 0.9 * 8760h * $0.15/kWh ≈ $8,858/年；5年 OpEx ≈ $44,290。其能效比（Tokens/Watt）需结合 ROCm 实测吞吐量计算，若 ROCm 优化不佳导致吞吐量仅为 H200 的 70%，则单位 Token 电费将显著高于 NVIDIA 方案。

## Evidence

先验知识/题面给定，逻辑校验通过：电费计算公式正确（750*0.9*8760*0.15=8857.5），5年累计计算正确（8857.5*5=44287.5≈44290），能效比逻辑推导自洽。
