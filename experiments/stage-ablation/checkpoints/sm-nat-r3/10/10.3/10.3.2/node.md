# N186: LRU 栈中冷大对象的大小分布修正：基于 ρ=-0.3 的负相关，冷对象（排名靠后）的平均大小 E[S|Cold] 高于全局平均。利用 N70 的结论，E[S|

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

LRU 栈中冷大对象的大小分布修正：基于 ρ=-0.3 的负相关，冷对象（排名靠后）的平均大小 E[S|Cold] 高于全局平均。利用 N70 的结论，E[S|Cold] ≈ E[S] / 0.85 ≈ 1.18 * 11 KB ≈ 13 KB。量化 W_waste 时需用此修正值代替 E[S]。

## Corrected Claim

LRU 栈中冷大对象的大小分布修正：基于 ρ=-0.3 的负相关，冷对象（排名靠后）的平均大小 E[S|Cold] 高于全局平均。利用 N70 的结论，E[S|Cold] ≈ E[S] / 0.85 ≈ 1.18 * 11 KB ≈ 13 KB。量化 W_waste 时需用此修正值代替 E[S]。

## Evidence

先验知识/题面给定，逻辑校验通过
