# N272: H100 SXM 理论 TPOT 计算式：(27.18e9 params * 1 byte/param) / 3350 GB/s = 8.11 ms/token

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N96

## Claim

H100 SXM 理论 TPOT 计算式：(27.18e9 params * 1 byte/param) / 3350 GB/s = 8.11 ms/token；RTX 5090 理论 TPOT 为 (27.18e9 * 1) / 1792 GB/s = 15.17 ms/token；两者理论比值 15.17/8.11 ≈ 1.87x，证实 H100 理论速度约为 5090 的 53% (1/1.87)。

## Corrected Claim

H100 SXM 理论 TPOT 计算式：(27.18e9 params * 1 byte/param) / 3350 GB/s = 8.11 ms/token；RTX 5090 理论 TPOT 为 (27.18e9 * 1) / 1792 GB/s = 15.17 ms/token；两者理论比值 15.17/8.11 ≈ 1.87x，证实 H100 理论速度约为 5090 的 53% (1/1.87)。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM 带宽约 3.35 TB/s，RTX 5090 带宽约 1.79 TB/s，计算过程及比值 1.87x 符合算术逻辑与硬件规格常识。
