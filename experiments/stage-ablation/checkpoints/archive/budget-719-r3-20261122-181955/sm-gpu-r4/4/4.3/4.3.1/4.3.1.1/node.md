# N317: 2x RTX 4090 工作站机箱的硬性物理约束：需支持 E-ATX 主板且具备至少 2 个全高全长 (Full-Height Full-Length) PCI

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

2x RTX 4090 工作站机箱的硬性物理约束：需支持 E-ATX 主板且具备至少 2 个全高全长 (Full-Height Full-Length) PCIe x16 插槽，插槽间距需满足 RTX 4090 的厚度 (2.5-slot, 约 62mm) 及散热风道需求，排除仅支持 1 个 PCIe x16 或插槽间距不足 3 槽的紧凑型机箱。

## Corrected Claim

2x RTX 4090 工作站机箱的硬性物理约束：需支持 E-ATX 主板且具备至少 2 个全高全长 (Full-Height Full-Length) PCIe x16 插槽，插槽间距需满足 RTX 4090 的厚度 (2.5-slot, 约 62mm) 及散热风道需求，排除仅支持 1 个 PCIe x16 或插槽间距不足 3 槽的紧凑型机箱。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 确为 2.5-slot 厚度，双卡安装需 E-ATX 或更大主板以提供足够 PCIe 插槽间距，物理约束描述符合硬件工程常识。
