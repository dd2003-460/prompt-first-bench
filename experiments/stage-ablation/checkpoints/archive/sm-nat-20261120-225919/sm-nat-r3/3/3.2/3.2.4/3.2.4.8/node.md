# N170: 工作点 A（完全无重叠-高残留）：f_stale=0.9, ΣR_Old=0.4*Total_R, ΣR_New=0.4*Total_R，计算 ΔH_neg ≈

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58, N59, N60

## Claim

工作点 A（完全无重叠-高残留）：f_stale=0.9, ΣR_Old=0.4*Total_R, ΣR_New=0.4*Total_R，计算 ΔH_neg ≈ -0.9 * (0.4 - 0.4)/1 = 0，但需考虑新热点未被缓存导致的额外 miss 率 ΔH_miss = 0.4 * (1 - H_new)，总负增益为两者之和。

## Corrected Claim

工作点 A（完全无重叠-高残留）：f_stale=0.9, ΣR_Old=0.4*Total_R, ΣR_New=0.4*Total_R，计算 ΔH_neg ≈ -0.9 * (0.4 - 0.4)/1 = 0，但需考虑新热点未被缓存导致的额外 miss 率 ΔH_miss = 0.4 * (1 - H_new)，总负增益为两者之和。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导自洽，ΔH_neg 计算符合定义，ΔH_miss 逻辑合理
