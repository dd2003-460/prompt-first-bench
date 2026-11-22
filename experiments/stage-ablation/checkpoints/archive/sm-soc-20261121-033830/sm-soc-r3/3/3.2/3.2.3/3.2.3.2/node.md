# N193: R_capture的计算基准对比：无筛选基准下 R_capture_base = (P_median - C) / (E[WTP] - C)，筛选后 R_cap

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N62

## Claim

R_capture的计算基准对比：无筛选基准下 R_capture_base = (P_median - C) / (E[WTP] - C)，筛选后 R_capture_filtered = (P_high - C) / (E[WTP|WTP>P_high] - C)，需计算两者差值 ΔR = R_capture_filtered - R_capture_base，并检验其是否显著大于0（如p<0.05），以确认筛选机制是否实质性提高了剩余捕获率

## Corrected Claim

R_capture的计算基准对比：无筛选基准下 R_capture_base = (P_median - C) / (E[WTP] - C)，筛选后 R_capture_filtered = (P_high - C) / (E[WTP|WTP>P_high] - C)，需计算两者差值 ΔR = R_capture_filtered - R_capture_base，并检验其是否显著大于0（如p<0.05），以确认筛选机制是否实质性提高了剩余捕获率

## Evidence

先验知识/题面给定，逻辑校验通过
