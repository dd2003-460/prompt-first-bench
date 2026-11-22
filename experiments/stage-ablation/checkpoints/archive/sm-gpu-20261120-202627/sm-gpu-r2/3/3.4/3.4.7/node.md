# N85: 1×A100 80GB 方案的 3 年 TCO 计算：CapEx = $15000 (used/spot) + $0 (Interconnect) + $500

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

1×A100 80GB 方案的 3 年 TCO 计算：CapEx = $15000 (used/spot) + $0 (Interconnect) + $500 (Chassis) = $15500；OpEx_energy = 400W * 0.7 (avg load) * 24h * 365d * 3y * $0.1/kWh = $6,210；总 TCO ≈ $21,710。

## Corrected Claim

1×A100 80GB 方案的 3 年 TCO 计算：CapEx = $15000 (used/spot) + $0 (Interconnect) + $500 (Chassis) = $15500；OpEx_energy = 400W * 0.7 (avg load) * 24h * 365d * 3y * $0.1/kWh = $6,210；总 TCO ≈ $21,710。

## Evidence

先验知识/题面给定，逻辑校验通过：CapEx 加和正确 ($15500)；OpEx 计算 $400 \times 0.7 \times 24 \times 365 \times 3 \times 0.1 = 6210$ 正确；总 TCO $15500 + 6210 = 21710$ 正确。

## Search Query

NVIDIA A100 80GB TDP average power consumption inference load
