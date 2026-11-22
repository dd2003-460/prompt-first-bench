# N306: PCIe 5.0 vs NVLink通信延迟比值在极端负载下的敏感性：当batch size B增加至8时，AllReduce数据量线性增加至34.4 GB。P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99

## Claim

PCIe 5.0 vs NVLink通信延迟比值在极端负载下的敏感性：当batch size B增加至8时，AllReduce数据量线性增加至34.4 GB。PCIe 5.0 (48 GB/s) 延迟升至716 ms，NVLink (800 GB/s) 延迟升至43 ms。比值从14.06倍扩大至16.6倍，证明高并发场景下PCIe多卡方案的通信瓶颈加剧，性价比进一步恶化。

## Corrected Claim

PCIe 5.0 vs NVLink通信延迟比值在极端负载下的敏感性：当batch size B增加至8时，AllReduce数据量线性增加至34.4 GB。PCIe 5.0 (48 GB/s) 延迟升至716 ms，NVLink (800 GB/s) 延迟升至43 ms。比值从14.06倍扩大至16.6倍，证明高并发场景下PCIe多卡方案的通信瓶颈加剧，性价比进一步恶化。

## Evidence

先验知识/题面给定，逻辑校验通过：数据量34.4GB与带宽48/800GB/s计算出的延迟716ms/43ms及比值16.6倍在数学上完全自洽，符合PCIe与NVLink的典型性能量级。
