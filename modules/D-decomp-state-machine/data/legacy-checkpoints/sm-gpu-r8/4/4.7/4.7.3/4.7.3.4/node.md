# N247: 每 GB 显存成本计算公式：Cost_per_GB = (Card_Price + Power_Cost_Yearly) / VRAM_GB。对于 MI250X

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N77

## Claim

每 GB 显存成本计算公式：Cost_per_GB = (Card_Price + Power_Cost_Yearly) / VRAM_GB。对于 MI250X (128GB, $20k, 1000W) vs H100 (80GB, $25k, 700W)，在相同电价下，MI250X 的每 GB 初始硬件成本更低，但电力成本占比更高

## Corrected Claim

每 GB 显存成本计算公式：Cost_per_GB = (Card_Price + Power_Cost_Yearly) / VRAM_GB。对于 MI250X (128GB, $20k, 1000W) vs H100 (80GB, $25k, 700W)，在相同电价下，MI250X 的每 GB 初始硬件成本更低，但电力成本占比更高

## Evidence

先验知识/题面给定，逻辑校验通过：MI250X初始硬件成本 $156.25/GB 低于 H100 的 $312.5/GB，且 MI250X 功率密度更高导致电力成本占比更高，陈述与计算逻辑一致。
