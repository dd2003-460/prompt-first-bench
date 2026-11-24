# N238: NVMe SSD预加载带宽为3 GB/s（受PCIe 4.0 x4链路理论上限3.5 GB/s及文件系统开销限制），100TB温数据预加载时间为9.26小时（1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N80

## Claim

NVMe SSD预加载带宽为3 GB/s（受PCIe 4.0 x4链路理论上限3.5 GB/s及文件系统开销限制），100TB温数据预加载时间为9.26小时（100×1024/3/3600）

## Corrected Claim

NVMe SSD预加载带宽为3 GB/s（受PCIe 4.0 x4链路理论上限3.5 GB/s及文件系统开销限制），100TB温数据预加载时间为9.26小时（100×1024/3/3600）

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x4理论带宽约3.5GB/s，扣除协议与文件系统开销后3GB/s为合理工程值；100TB(102400GB)/3GB/s/3600s/h ≈ 9.26h，计算无误。
