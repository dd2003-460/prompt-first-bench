# N230: 自建带宽利用率 U_bw = Actual_Bandwidth / Leased_Bandwidth = 3.5 Gbps / (10 POP * 10 Gbp

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N72

## Claim

自建带宽利用率 U_bw = Actual_Bandwidth / Leased_Bandwidth = 3.5 Gbps / (10 POP * 10 Gbps) = 3.5%；极低利用率导致固定成本分摊后单位成本高昂，需提高缓存命中率 H 或增加 POP 数量以降低单位带宽成本，或转向公有云 CDN 以利用其规模效应。

## Corrected Claim

自建带宽利用率 U_bw = Actual_Bandwidth / Leased_Bandwidth = 3.5 Gbps / (10 POP * 10 Gbps) = 3.5%；极低利用率导致固定成本分摊后单位成本高昂，需提高缓存命中率 H 或增加 POP 数量以降低单位带宽成本，或转向公有云 CDN 以利用其规模效应。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 3.5/(10*10)=3.5% 正确，且低利用率导致高单位成本及优化策略（提高命中率/增加POP/转公有云）符合CDN经济学基本原理。
