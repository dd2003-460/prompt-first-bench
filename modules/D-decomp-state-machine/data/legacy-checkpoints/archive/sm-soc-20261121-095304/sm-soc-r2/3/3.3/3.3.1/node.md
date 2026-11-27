# N53: 短期GMV下降的精确量化：设当前月均成交单量为Q0，平均成交价为P0。若价格下降15%（ΔP = -0.15P0）且短期成交量不变（ΔQ=0），则短期GMV损失

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

短期GMV下降的精确量化：设当前月均成交单量为Q0，平均成交价为P0。若价格下降15%（ΔP = -0.15P0）且短期成交量不变（ΔQ=0），则短期GMV损失量 ΔGMV_short = -0.15 * Q0 * P0。

## Corrected Claim

短期GMV下降的精确量化：设当前月均成交单量为Q0，平均成交价为P0。若价格下降15%（ΔP = -0.15P0）且短期成交量不变（ΔQ=0），则短期GMV损失量 ΔGMV_short = -0.15 * Q0 * P0。

## Evidence

先验知识/题面给定，逻辑校验通过：GMV=Q*P，在Q不变且P下降15%的情况下，GMV变化量确实为-0.15*Q0*P0，数学推导严谨。
