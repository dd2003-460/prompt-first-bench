# N118: 混合策略缓存命中率 (CHR_hybrid) 的计算公式：CHR_hybrid = w_core × CHR_self_core + w_tail × CHR_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

混合策略缓存命中率 (CHR_hybrid) 的计算公式：CHR_hybrid = w_core × CHR_self_core + w_tail × CHR_pub_tail，其中 w_core=0.6（N14），CHR_self_core≈75%（核心区域流量集中，命中率较高），CHR_pub_tail≈92%（长尾走公有云），因此 CHR_hybrid ≈ 0.6×0.75 + 0.4×0.92 = 0.818 或 81.8%

## Corrected Claim

混合策略缓存命中率 (CHR_hybrid) 的计算公式：CHR_hybrid = w_core × CHR_self_core + w_tail × CHR_pub_tail，其中 w_core=0.6（N14），CHR_self_core≈75%（核心区域流量集中，命中率较高），CHR_pub_tail≈92%（长尾走公有云），因此 CHR_hybrid ≈ 0.6×0.75 + 0.4×0.92 = 0.818 或 81.8%

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合加权平均定义，数值计算 0.6*0.75 + 0.4*0.92 = 0.45 + 0.368 = 0.818 准确无误，且权重之和为1，量纲一致。
