# N13: 物理接口限制：单卡方案受限于 PCIe 插槽数量和主板供电能力，双卡 RTX 4090/5090 需要至少 2 个 PCIe x16 插槽和 1600W+ 电源

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

物理接口限制：单卡方案受限于 PCIe 插槽数量和主板供电能力，双卡 RTX 4090/5090 需要至少 2 个 PCIe x16 插槽和 1600W+ 电源，数据中心卡 H100 SXM 需要特定基板（Baseboard）支持，无法在标准 ATX 工作站上直接安装。

## Corrected Claim

物理接口限制：单卡方案受限于 PCIe 插槽数量和主板供电能力，双卡 RTX 4090/5090 需要至少 2 个 PCIe x16 插槽和 1600W+ 电源，数据中心卡 H100 SXM 需要特定基板（Baseboard）支持，无法在标准 ATX 工作站上直接安装。

## Evidence

先验知识/题面给定，逻辑校验通过
