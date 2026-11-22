# N430: AMD MI300X 的 PCIe 5.0 x16 接口无需额外购买桥接器即可实现单卡安装，但需确认主板是否支持 PCIe 5.0 x16 插槽及 16x 物理

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N138, N139, N140

## Claim

AMD MI300X 的 PCIe 5.0 x16 接口无需额外购买桥接器即可实现单卡安装，但需确认主板是否支持 PCIe 5.0 x16 插槽及 16x 物理通道完整性，若需 PCIe 4.0 降级则带宽减半至 ~64GB/s。

## Corrected Claim

AMD MI300X 的 PCIe 5.0 x16 接口无需额外购买桥接器即可实现单卡安装，但需确认主板是否支持 PCIe 5.0 x16 插槽及 16x 物理通道完整性，若需 PCIe 4.0 降级则带宽减半至 ~64GB/s。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 5.0 x16 带宽约为 128GB/s，降级至 PCIe 4.0 x16 带宽减半为 64GB/s，符合物理规格；MI300X 作为标准 PCIe 卡无需额外桥接器即可安装，逻辑自洽。
