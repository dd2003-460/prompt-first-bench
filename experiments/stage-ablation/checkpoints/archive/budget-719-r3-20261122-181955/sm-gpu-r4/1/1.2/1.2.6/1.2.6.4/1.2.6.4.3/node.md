# N500: 修正 N170 的 NVLink 通信时间错误：基于 N366 的 1 MB 总通信量，NVLink (A100 600 GB/s) 传输时间 = 1 MB /

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N170

## Claim

修正 N170 的 NVLink 通信时间错误：基于 N366 的 1 MB 总通信量，NVLink (A100 600 GB/s) 传输时间 = 1 MB / 600 GB/s ≈ 0.0017 ms；而非 N170 中计算的 14.3 ms。

## Corrected Claim

修正 N170 的 NVLink 通信时间错误：基于 N366 的 1 MB 总通信量，NVLink (A100 600 GB/s) 传输时间 = 1 MB / 600 GB/s ≈ 0.0017 ms；而非 N170 中计算的 14.3 ms。

## Evidence

先验知识/题面给定，逻辑校验通过：1 MB / 600 GB/s ≈ 0.00167 ms，计算正确且量级合理
