# N711: 瓶颈分量1（SSD写入上限）：典型企业级NVMe SSD（如Samsung PM9A3 7.68TB）顺序写吞吐上限为 6,800 MB/s ≈ 6.8 GB/

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N248

## Claim

瓶颈分量1（SSD写入上限）：典型企业级NVMe SSD（如Samsung PM9A3 7.68TB）顺序写吞吐上限为 6,800 MB/s ≈ 6.8 GB/s；在RAID-6中，每次写入需额外写入2个校验块，有效重建写入速率受限于单盘写入能力，即 Write_Limit = 6.8 GB/s。

## Corrected Claim

瓶颈分量1（SSD写入上限）：典型企业级NVMe SSD（如Samsung PM9A3 7.68TB）顺序写吞吐上限为 6,800 MB/s ≈ 6.8 GB/s；在RAID-6中，每次写入需额外写入2个校验块，有效重建写入速率受限于单盘写入能力，即 Write_Limit = 6.8 GB/s。

## Evidence

先验知识/题面给定，逻辑校验通过
