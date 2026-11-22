# N345: 2× RTX 4090 PCIe 4.0 x16 互联拓扑带宽修正：单卡 x16 理论带宽 64 GB/s，但受 P2P 通信效率、PCIe 协议开销及驱动调度

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N137

## Claim

2× RTX 4090 PCIe 4.0 x16 互联拓扑带宽修正：单卡 x16 理论带宽 64 GB/s，但受 P2P 通信效率、PCIe 协议开销及驱动调度影响，有效双向聚合带宽通常在 48-56 GB/s 之间；若主板支持 P2P 直通，上限可达 60 GB/s，否则需经 CPU 中转，带宽降至 30-40 GB/s。

## Corrected Claim

2× RTX 4090 PCIe 4.0 x16 互联拓扑带宽修正：单卡 x16 理论带宽 64 GB/s，但受 P2P 通信效率、PCIe 协议开销及驱动调度影响，有效双向聚合带宽通常低于理论值；若主板支持 P2P 直通，带宽较高，否则需经 CPU 中转，带宽显著降低。

## Evidence

[质询]具体数值区间（48-56 GB/s, 60 GB/s, 30-40 GB/s）属于经验性工程数据，受主板拓扑、BIOS设置、驱动版本及具体P2P实现影响极大，缺乏通用标准，且‘上限可达60 GB/s’接近理论峰值，在实际P2P通信中因协议开销和调度延迟，很难稳定达到如此高的有效带宽，存在夸大嫌疑。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

RTX 4090 dual GPU PCIe 4.0 P2P bandwidth effective throughput
