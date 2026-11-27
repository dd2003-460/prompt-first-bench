# N9: 本地工作站物理兼容性硬约束：主流消费级/工作站级机箱的 PCIe 插槽数量上限、PCIe 通道分布（x16/x4/x1）、以及双卡/四卡布局的最小机箱尺寸要求

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

本地工作站物理兼容性硬约束：主流消费级/工作站级机箱的 PCIe 插槽数量上限、PCIe 通道分布（x16/x4/x1）、以及双卡/四卡布局的最小机箱尺寸要求

## Corrected Claim

主流消费级机箱通常支持2-4个全尺寸PCIe x16插槽，而高端工作站级主板（如华硕W890）可提供多达7个PCIe x16插槽及96条PCIe通道；双卡/四卡布局对机箱尺寸的要求取决于具体主板布局和散热设计，通常四卡布局需要E-ATX或更大型号机箱以容纳物理空间和散热风道。

## Evidence

[质询]陈述试图给出一个通用的“上限”和“最小尺寸要求”，但不同平台（消费级 vs 工作站级）差异巨大，且“最小机箱尺寸”并非由PCIe插槽数量单一决定，还受散热、电源、主板布局等影响，缺乏具体数值支撑，属于模糊的经验性描述。 | 来源[2]提供了工作站级主板（华硕W890）的具体PCIe插槽数量（7条x16）和通道数（96条），间接支持了工作站级硬件的高扩展性，但未提供消费级上限或具体的机箱尺寸物理约束数据，无法直接验证“最小机箱尺寸要求”这一具体量化结论。

## Search Query

workstation case PCIe slot limit dual GPU physical clearance requirements

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_33525298/article/details/169303337&rut=4f83381810ab627bd091b64e7c4afe21d507a30bad7604cf1ffd61fd1a89d3b1', 'type': 'ddg', 'title': '本地部署大模型的四大硬约束：显存、带宽、PCIe与软件兼容性-CSDN博客'}
- {'url': 'https://www.ithome.com/0/913/301.htm&rut=8bd23bf3a6c93192312b74ad03bba1b9656daa6bf874b4e1fa6513a233cf5afc', 'type': 'ddg', 'title': '华硕展示新一代 W890 工作站主板：支持 7 条 PCIe 5.0 与 8 槽 DDR5，面向英特尔 Granite Rapids-WS ...'}
