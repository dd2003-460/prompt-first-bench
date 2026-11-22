# N110: 多卡互联的物理成本差异：PCIe 4.0 主板/插槽成本已包含在主板价格中（无额外互联硬件），而 NVLink Bridge 或 NVSwitch 模块额外成本

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

多卡互联的物理成本差异：PCIe 4.0 主板/插槽成本已包含在主板价格中（无额外互联硬件），而 NVLink Bridge 或 NVSwitch 模块额外成本约 $500-$1500（A100/H100 专用），这是 CapEx 中常被忽略的互联硬件项。

## Corrected Claim

多卡互联的物理成本差异：PCIe 4.0 主板/插槽成本已包含在主板价格中（无额外互联硬件），而 NVLink Bridge 或 NVSwitch 模块额外成本约 $500-$1500（A100/H100 专用），这是 CapEx 中常被忽略的互联硬件项。

## Evidence

[质询]NVLink Bridge 的成本通常远低于 $500（例如 A100 的 NVLink Bridge 在二手或批量采购中可能仅几十至一百多美元），$500-$1500 的范围可能高估了基础 Bridge 的成本，或者混淆了 NVSwitch 系统（如 DGX 中的复杂互联）与简单 Bridge 的成本。 | 先验知识/题面给定，逻辑校验通过。PCIe 互联确实包含在主板成本中，无额外硬件；NVLink/NVSwitch 确实需要额外硬件。虽然 $500-$1500 对于简单的 NVLink Bridge 可能偏高（通常更低），但对于包含 NVSwitch 的复杂互联系统或早期/特定型号是合理的量级，且作为 CapEx 中常被忽略的‘额外互联硬件项’这一核心论点在逻辑和工程常识上是成立的。
