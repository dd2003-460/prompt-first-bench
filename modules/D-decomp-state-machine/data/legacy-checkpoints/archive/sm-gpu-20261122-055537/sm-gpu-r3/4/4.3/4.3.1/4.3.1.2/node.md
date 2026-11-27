# N234: RTX 4090 散热风扇的额外功耗估算：典型高性能机箱风扇（如 Noctua NF-A14）满载功耗约 1.5-2W/个，假设配置 4 个机箱风扇 + 1 个

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69, N70, N71

## Claim

RTX 4090 散热风扇的额外功耗估算：典型高性能机箱风扇（如 Noctua NF-A14）满载功耗约 1.5-2W/个，假设配置 4 个机箱风扇 + 1 个显卡内置风扇（已计入 GPU TDP），额外系统冷却功耗 P_cool_extra ≈ 6-8W。在 24/7 运行 ($0.15/kWh) 下，年成本 ΔC_fan ≈ 0.007 kW * 8760 h * $0.15 ≈ $9.2/年。

## Corrected Claim

RTX 4090 散热风扇的额外功耗估算：典型高性能机箱风扇（如 Noctua NF-A14）满载功耗约 1.5-2W/个，假设配置 4 个机箱风扇 + 1 个显卡内置风扇（已计入 GPU TDP），额外系统冷却功耗 P_cool_extra ≈ 6-8W。在 24/7 运行 ($0.15/kWh) 下，年成本 ΔC_fan ≈ 0.007 kW * 8760 h * $0.15 ≈ $9.2/年。

## Evidence

先验知识/题面给定，逻辑校验通过：Noctua NF-A14 满载功耗约 1.5-2W 符合工程常识，4 个风扇总功耗 6-8W 量级合理；年成本计算 0.007kW * 8760h * $0.15/kWh ≈ $9.2 数学推导正确。
