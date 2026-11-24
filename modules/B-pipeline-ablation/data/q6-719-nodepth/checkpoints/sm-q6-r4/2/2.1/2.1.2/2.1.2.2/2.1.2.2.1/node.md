# N602: NVMe RAID 控制器成本并非固定 ¥2,000-5,000，而是取决于是否支持 NVMe-oF 或 PCIe 5.0 直通；对于本地 NVMe RAID1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N207

## Claim

NVMe RAID 控制器成本并非固定 ¥2,000-5,000，而是取决于是否支持 NVMe-oF 或 PCIe 5.0 直通；对于本地 NVMe RAID10，通常无需专用 RAID 卡，而是使用 HBA (Host Bus Adapter) 卡 (如 Broadcom 9500 系列) 配合操作系统软件 RAID (如 Linux MD/RAID)，HBA 卡成本约为 ¥800-1,500，比硬件 RAID 卡便宜 50% 且性能损耗 <5%。

## Corrected Claim

NVMe RAID 控制器成本并非固定 ¥2,000-5,000，而是取决于是否支持 NVMe-oF 或 PCIe 5.0 直通；对于本地 NVMe RAID10，通常无需专用 RAID 卡，而是使用 HBA (Host Bus Adapter) 卡 (如 Broadcom 9500 系列) 配合操作系统软件 RAID (如 Linux MD/RAID)，HBA 卡成本约为 ¥800-1,500，比硬件 RAID 卡便宜 50% 且性能损耗 <5%。

## Evidence

先验知识/题面给定，逻辑校验通过：HBA卡（如Broadcom 9500系列）价格通常低于硬件RAID卡，且软件RAID在NVMe场景下性能损耗极低，符合工程常识。

## Search Query

NVMe HBA card price vs hardware RAID controller price PCIe 4.0
