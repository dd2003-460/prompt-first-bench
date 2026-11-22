# N261: 修正 N85 中的功耗参数：A100 PCIe 版 TDP 为 300W（修正自矛盾检测 N45 vs N89，N89 来源更可信），因此 3 年电力成本基础变

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

修正 N85 中的功耗参数：A100 PCIe 版 TDP 为 300W（修正自矛盾检测 N45 vs N89，N89 来源更可信），因此 3 年电力成本基础变量 E_A100 = 1 × 0.3 kW × 8760 h × 3 = 7884 kWh。

## Corrected Claim

修正 N85 中的功耗参数：A100 PCIe 版 TDP 为 300W（修正自矛盾检测 N45 vs N89，N89 来源更可信），因此 3 年电力成本基础变量 E_A100 = 1 × 0.3 kW × 8760 h × 3 = 7884 kWh。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 PCIe TDP 300W 符合工程常识，计算 1 * 0.3 * 8760 * 3 = 7884 准确无误。

## Search Query

A100 PCIe TDP watts datasheet
