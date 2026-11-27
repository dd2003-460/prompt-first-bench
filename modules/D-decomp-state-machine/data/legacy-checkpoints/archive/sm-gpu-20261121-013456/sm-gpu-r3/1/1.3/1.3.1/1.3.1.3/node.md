# N144: Qwen3-27B INT4 权重主体显存占用 = 27.18e9 * 4 bits / 8 / 1e9 = 13.59 GB。加上 Overhead 0.84

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N53

## Claim

Qwen3-27B INT4 权重主体显存占用 = 27.18e9 * 4 bits / 8 / 1e9 = 13.59 GB。加上 Overhead 0.849 GB，总权重显存 ≈ 14.44 GB（来源：计算推导）

## Corrected Claim

Qwen3-27B INT4 权重主体显存占用 = 27.18e9 * 4 bits / 8 / 1e9 = 13.59 GB。加上 Overhead 0.849 GB，总权重显存 ≈ 14.44 GB（来源：计算推导）

## Evidence

先验知识/题面给定，逻辑校验通过：27.18e9 * 0.5 bytes / 1e9 = 13.59 GB，加上 0.849 GB 开销，总和 14.439 GB ≈ 14.44 GB，计算无误。

## Search Query

Qwen3-27B INT4 weight memory footprint
