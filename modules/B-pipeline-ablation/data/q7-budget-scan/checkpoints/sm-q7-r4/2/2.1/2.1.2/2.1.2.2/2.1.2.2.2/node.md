# N487: 服务器硬件 CapEx 明细展开：¥40,000 的服务器成本需分解为 CPU/内存/主板/电源/机箱五项；对于承载 20 块 NVMe 的高性能存储节点，典型

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N164

## Claim

服务器硬件 CapEx 明细展开：¥40,000 的服务器成本需分解为 CPU/内存/主板/电源/机箱五项；对于承载 20 块 NVMe 的高性能存储节点，典型配置（双路 Xeon + 512GB RAM + 冗余电源）的 BOM 成本约为 ¥35,000-¥45,000，该数值处于合理区间，但需明确是否包含 RAID 卡或 HBA 卡（若使用软件 RAID 如 ZFS/LVM 则无额外卡费，若硬件 RAID 需加 ¥5,000-¥10,000）。

## Corrected Claim

服务器硬件 CapEx 明细展开：¥40,000 的服务器成本需分解为 CPU/内存/主板/电源/机箱五项；对于承载 20 块 NVMe 的高性能存储节点，典型配置（双路 Xeon + 512GB RAM + 冗余电源）的 BOM 成本约为 ¥35,000-¥45,000，该数值处于合理区间，但需明确是否包含 RAID 卡或 HBA 卡（若使用软件 RAID 如 ZFS/LVM 则无额外卡费，若硬件 RAID 需加 ¥5,000-¥10,000）。

## Evidence

先验知识/题面给定，逻辑校验通过：双路Xeon+512GB RAM+冗余电源的BOM成本在¥35k-45k区间符合当前硬件市场行情，RAID/HBA卡费用估算亦合理

## Search Query

high performance storage server BOM cost dual Xeon 512GB RAM
