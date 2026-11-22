# N16: 单卡 BF16 方案（如 80GB 显存卡）的 TCO 基准值：硬件成本 C_hw + 年电费 C_power，其中 C_power = 功率(W) × 876

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

单卡 BF16 方案（如 80GB 显存卡）的 TCO 基准值：硬件成本 C_hw + 年电费 C_power，其中 C_power = 功率(W) × 8760h × 电价($/kWh)

## Corrected Claim

单卡 BF16 方案（如 80GB 显存卡）的 TCO 基准值：硬件成本 C_hw + 年电费 C_power，其中 C_power = 功率(W) × 8760h × 电价($/kWh)

## Evidence

先验知识/题面给定，逻辑校验通过：TCO（总拥有成本）通常包含硬件成本与运营成本（电费），电费计算公式（功率×时间×单价）符合物理与经济常识，量纲正确。
