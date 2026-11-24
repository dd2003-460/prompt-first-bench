# N62: Overhead_Time 中数据校验耗时分量：基于 SHA-256 校验，NVMe 吞吐 2GB/s 下 100TB 校验需 13.9h，HDD 吞吐 200

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

Overhead_Time 中数据校验耗时分量：基于 SHA-256 校验，NVMe 吞吐 2GB/s 下 100TB 校验需 13.9h，HDD 吞吐 200MB/s 下 400TB 校验需 55.6h

## Corrected Claim

Overhead_Time 中数据校验耗时分量：基于 SHA-256 校验，NVMe 吞吐 2GB/s 下 100TB 校验需 13.9h，HDD 吞吐 200MB/s 下 400TB 校验需 55.6h

## Evidence

先验知识/题面给定，逻辑校验通过：100TB/2GB/s ≈ 13.9h，400TB/200MB/s ≈ 55.6h，数值量级与计算逻辑自洽
