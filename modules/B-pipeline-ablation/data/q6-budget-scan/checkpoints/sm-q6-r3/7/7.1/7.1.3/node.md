# N288: 单台服务器存储 IOPS 与带宽瓶颈：2x 3.84TB NVMe SSD RAID0/1 提供 ~500k-1M IOPS 和 ~6GB/s 读取带宽；单 P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

单台服务器存储 IOPS 与带宽瓶颈：2x 3.84TB NVMe SSD RAID0/1 提供 ~500k-1M IOPS 和 ~6GB/s 读取带宽；单 POP 峰值带宽 2.5-4.2 Gbps (≈300-500MB/s) 远小于 NVMe 读取能力，存储子系统不是瓶颈，瓶颈在于网卡（10Gbps）和 CPU 网络栈处理

## Corrected Claim

单台服务器存储 IOPS 与带宽瓶颈：2x 3.84TB NVMe SSD RAID0/1 提供 ~500k-1M IOPS 和 ~6GB/s 读取带宽；单 POP 峰值带宽 2.5-4.2 Gbps (≈300-500MB/s) 远小于 NVMe 读取能力，存储子系统不是瓶颈，瓶颈在于网卡（10Gbps）和 CPU 网络栈处理

## Evidence

先验知识/题面给定，逻辑校验通过：NVMe SSD RAID0/1 的 IOPS (500k-1M) 和带宽 (~6GB/s) 量级符合工程常识；单 POP 峰值带宽 (300-500MB/s) 远小于存储读取能力，因此瓶颈在网卡/CPU 而非存储，逻辑自洽。

## Search Query

NVMe SSD random read bandwidth vs network interface bottleneck CDN
