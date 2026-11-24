# N404: 工作点A (RAID-6) 聚合读取吞吐的理论上限分解：理论聚合吞吐 T_theoretical = N_disks * T_single_disk = 24 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N135

## Claim

工作点A (RAID-6) 聚合读取吞吐的理论上限分解：理论聚合吞吐 T_theoretical = N_disks * T_single_disk = 24 * 5GB/s = 120GB/s。原claim中提到的'控制器瓶颈限制为24%'缺乏依据，NVMe RAID通常通过多路径PCIe或JBOD架构可接近线性扩展，除非是单控制器PCIe 4.0 x16 (约64GB/s双向)瓶颈。

## Corrected Claim

工作点A (RAID-6) 聚合读取吞吐的理论上限分解：理论聚合吞吐 T_theoretical = N_disks * T_single_disk = 24 * 5GB/s = 120GB/s。原claim中提到的'控制器瓶颈限制为24%'缺乏依据，NVMe RAID通常通过多路径PCIe或JBOD架构可接近线性扩展，除非是单控制器PCIe 4.0 x16 (约64GB/s双向)瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：24*5=120计算正确，NVMe多路径/JBOD线性扩展及PCIe 4.0 x16带宽瓶颈描述符合硬件常识

## Search Query

NVMe RAID aggregate throughput PCIe bottleneck
