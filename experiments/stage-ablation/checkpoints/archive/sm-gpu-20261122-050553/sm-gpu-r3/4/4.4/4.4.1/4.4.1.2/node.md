# N272: A100 PCIe 方案的总 TCO 修正公式：TCO_A100_corrected = C_hw_A100 + C_power_A100_Pcie + C_i

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N89

## Claim

A100 PCIe 方案的总 TCO 修正公式：TCO_A100_corrected = C_hw_A100 + C_power_A100_Pcie + C_infra_A100；其中 C_hw_A100 = $16,100 (N78), C_infra_A100 ≈ $0 (假设已包含在硬件或忽略不计)，故 TCO_A100_corrected ≈ $16,100 + $788.4 = $16,888.4 (E_price=$0.10)。注意：N89 原 claim 中的 $15,788 可能未包含完整配件成本或使用了不同的硬件基准，需以 N78 的 $16,100 为基准进行最终校准。

## Corrected Claim

A100 PCIe 方案的总 TCO 修正公式：TCO_A100_corrected = C_hw_A100 + C_power_A100_Pcie + C_infra_A100；其中 C_hw_A100 = $16,100 (N78), C_infra_A100 ≈ $0 (假设已包含在硬件或忽略不计)，故 TCO_A100_corrected ≈ $16,100 + $788.4 = $16,888.4 (E_price=$0.10)。注意：N89 原 claim 中的 $15,788 可能未包含完整配件成本或使用了不同的硬件基准，需以 N78 的 $16,100 为基准进行最终校准。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 16100 + 788.4 = 16888.4 正确，且符合 TCO 构成逻辑（硬件+电力+基础设施）。

## Search Query

A100 40GB PCIe total cost of ownership 3 year calculation
