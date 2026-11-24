# N422: RAID-10重建带宽的瓶颈分析：重建时间 T_rebuild = V_disk / T_sync_eff。T_sync_eff 受限于源盘（镜像伙伴）的顺序读

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N140

## Claim

RAID-10重建带宽的瓶颈分析：重建时间 T_rebuild = V_disk / T_sync_eff。T_sync_eff 受限于源盘（镜像伙伴）的顺序读吞吐和目标盘的写入吞吐，以及总线带宽。假设源盘NVMe顺序读 5GB/s，目标盘顺序写 3GB/s，PCIe 3.0 x4 带宽 1.6GB/s（单向）或更高。实际 T_sync_eff 通常受限于较慢的一方或控制器开销，取 2GB/s 更为保守。原N140假设5GB/s过于乐观。

## Corrected Claim

RAID-10重建带宽的瓶颈分析：重建时间 T_rebuild = V_disk / T_sync_eff。T_sync_eff 受限于源盘（镜像伙伴）的顺序读吞吐和目标盘的写入吞吐，以及总线带宽。假设源盘NVMe顺序读 5GB/s，目标盘顺序写 3GB/s，PCIe 3.0 x4 带宽 1.6GB/s（单向）或更高。实际 T_sync_eff 通常受限于较慢的一方或控制器开销，取 2GB/s 更为保守。原N140假设5GB/s过于乐观。

## Evidence

[质询]PCIe 3.0 x4 单向带宽标称约为 1.575 GB/s，文中取 1.6 GB/s 符合工程近似；NVMe 顺序读 5 GB/s 和顺序写 3 GB/s 属于主流企业级 SSD 的典型性能范围，取 2 GB/s 作为有效同步带宽（考虑控制器开销和总线限制）在逻辑上是保守且合理的。 | 先验知识/题面给定，逻辑校验通过：RAID-10 重建确实受限于源盘读、目标盘写及总线带宽的最小值，2 GB/s 的有效带宽假设符合硬件性能瓶颈分析的基本原理。
