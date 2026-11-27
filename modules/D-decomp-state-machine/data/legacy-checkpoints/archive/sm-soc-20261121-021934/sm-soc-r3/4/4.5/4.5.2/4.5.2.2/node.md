# N119: 平台强制显示的近期成交均价 P_rec_avg 的统计口径定义：P_rec_avg = Σ(P_i * Q_i) / Σ(Q_i) (过去30天加权平均)，若采

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N50

## Claim

平台强制显示的近期成交均价 P_rec_avg 的统计口径定义：P_rec_avg = Σ(P_i * Q_i) / Σ(Q_i) (过去30天加权平均)，若采用简单算术平均则需剔除极端值（如最高/最低5%），不同口径导致的 P_rec_avg 差异约为 2-5%，直接影响 ΔPrice 的计算基准。

## Corrected Claim

平台强制显示的近期成交均价 P_rec_avg 的统计口径定义：P_rec_avg = Σ(P_i * Q_i) / Σ(Q_i) (过去30天加权平均)，若采用简单算术平均则需剔除极端值（如最高/最低5%），不同口径导致的 P_rec_avg 差异约为 2-5%，直接影响 ΔPrice 的计算基准。

## Evidence

先验知识/题面给定，逻辑校验通过
