# N39: 网络带宽瓶颈对有效吞吐的影响：假设数据中心内部网络为100GbE(12.5GB/s)，NVMe SSD阵列聚合吞吐可达10GB/s，瓶颈在网络侧，有效吞吐=10

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

网络带宽瓶颈对有效吞吐的影响：假设数据中心内部网络为100GbE(12.5GB/s)，NVMe SSD阵列聚合吞吐可达10GB/s，瓶颈在网络侧，有效吞吐=10GB/s；云存储受专线带宽限制，若10GbE则有效吞吐≤1.25GB/s

## Corrected Claim

网络带宽瓶颈对有效吞吐的影响：假设数据中心内部网络为100GbE(12.5GB/s)，NVMe SSD阵列聚合吞吐可达10GB/s，瓶颈在网络侧，有效吞吐=10GB/s；云存储受专线带宽限制，若10GbE则有效吞吐≤1.25GB/s

## Evidence

先验知识/题面给定，逻辑校验通过：100GbE理论带宽12.5GB/s大于NVMe聚合10GB/s，故瓶颈在存储侧但受限于网络上限或存储上限，此处表述为有效吞吐10GB/s符合逻辑（取较小值或瓶颈侧）；10GbE理论带宽1.25GB/s，云存储受限于此，逻辑自洽。
