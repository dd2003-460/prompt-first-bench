# N270: 计算 1x H100 SXM (FP8) 方案的 TCO_year：硬件成本 $29000 + 电力 $490 (基于 N90 修正值) + 维护 $580 (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N100

## Claim

计算 1x H100 SXM (FP8) 方案的 TCO_year：硬件成本 $29000 + 电力 $490 (基于 N90 修正值) + 维护 $580 (2% of $29000, 基于 N96) - 残值摊销 ($29000 * 0.4 / 3 ≈ $3867, 假设40%残值)，得出 TCO_year ≈ $26203。该值远高于 2x RTX 4090，但在高吞吐场景下需除以吞吐量差异进行归一化。

## Corrected Claim

计算 1x H100 SXM (FP8) 方案的 TCO_year：硬件成本 $29000 + 电力 $490 (基于 N90 修正值) + 维护 $580 (2% of $29000, 基于 N96) - 残值摊销 ($29000 * 0.4 / 3 ≈ $3867, 假设40%残值)，得出 TCO_year ≈ $26203。该值远高于 2x RTX 4090，但在高吞吐场景下需除以吞吐量差异进行归一化。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（29000+490+580-3867=26203），残值摊销逻辑合理（40%残值/3年），符合TCO计算基本范式。

## Search Query

H100 SXM 3 year residual value rate data center
