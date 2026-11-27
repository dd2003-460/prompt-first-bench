# N371: A100 80GB 的 TDP 为 400W (SXM) 或 300W (PCIe)，在 $0.12/kWh 电价下，3 年电费成本为 400W * 8760h

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N134

## Claim

A100 80GB 的 TDP 为 400W (SXM) 或 300W (PCIe)，在 $0.12/kWh 电价下，3 年电费成本为 400W * 8760h * 3y * $0.12/kWh = $1,261.44 (SXM) 或 $946.08 (PCIe)，需根据具体形态选择计算。

## Corrected Claim

A100 80GB 的 TDP 为 400W (SXM) 或 300W (PCIe)，在 $0.12/kWh 电价下，3 年电费成本为 400W * 8760h * 3y * $0.12/kWh = $1,261.44 (SXM) 或 $946.08 (PCIe)，需根据具体形态选择计算。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 SXM TDP 400W 和 PCIe TDP 300W 符合 NVIDIA 官方规格；电费计算公式 400W * 8760h * 3y * $0.12/kWh = $1,261.44 和 300W * 8760h * 3y * $0.12/kWh = $946.08 数值计算正确，量纲合理。
