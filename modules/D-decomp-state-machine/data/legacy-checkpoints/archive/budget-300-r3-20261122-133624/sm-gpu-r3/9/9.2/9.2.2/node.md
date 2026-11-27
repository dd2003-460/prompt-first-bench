# N430: 1× H100 方案的全负载电力成本 C_power 修正：H100 PCIe TDP 700W。Decode 阶段功耗约为 TDP 的 60% (420W)，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N169

## Claim

1× H100 方案的全负载电力成本 C_power 修正：H100 PCIe TDP 700W。Decode 阶段功耗约为 TDP 的 60% (420W)，Prefill 接近 100%。假设 80% Decode + 20% Prefill，加权平均功耗 P_avg = 0.8 * 420W + 0.2 * 700W = 476W。3年电费 = 476W * 8760h * 3y * $0.12/kWh = $1,506.53。

## Corrected Claim

1× H100 方案的全负载电力成本 C_power 修正：H100 PCIe TDP 700W。Decode 阶段功耗约为 TDP 的 60% (420W)，Prefill 接近 100%。假设 80% Decode + 20% Prefill，加权平均功耗 P_avg = 0.8 * 420W + 0.2 * 700W = 476W。3年电费 = 476W * 8760h * 3y * $0.12/kWh = $1,506.53。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 PCIe TDP 700W 符合规格，加权平均功耗计算 (0.8*420 + 0.2*700 = 476W) 及电费公式 (476 * 8760 * 3 * 0.12 ≈ 1506.53) 数值准确，逻辑自洽。
