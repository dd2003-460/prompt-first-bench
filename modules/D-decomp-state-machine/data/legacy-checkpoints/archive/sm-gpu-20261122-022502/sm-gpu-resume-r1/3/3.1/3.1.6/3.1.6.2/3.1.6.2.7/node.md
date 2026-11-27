# N701: RTX 4090 PCIe 4.0 x16 实际有效带宽：理论单向 32 GB/s，双向 64 GB/s，扣除 130B TLP 头部和 ACK 开销后，实际有

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N215, N216, N217

## Claim

RTX 4090 PCIe 4.0 x16 实际有效带宽：理论单向 32 GB/s，双向 64 GB/s，扣除 130B TLP 头部和 ACK 开销后，实际有效带宽约 51.2 GB/s (80% 效率)，与 N216 的 50 GB/s 一致

## Corrected Claim

RTX 4090 PCIe 4.0 x16 实际有效带宽：理论单向 32 GB/s，双向 64 GB/s，扣除 130B TLP 头部和 ACK 开销后，实际有效带宽约 51.2 GB/s (80% 效率)，与 N216 的 50 GB/s 一致

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 理论带宽 32GB/s，扣除协议开销后 80% 效率约为 25.6GB/s（单向），双向 51.2GB/s，与陈述一致。

## Search Query

PCIe 4.0 x16 effective bandwidth efficiency
