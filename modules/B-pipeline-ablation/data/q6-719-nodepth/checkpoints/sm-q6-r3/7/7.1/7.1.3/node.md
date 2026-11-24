# N364: 敏感性分析区间：对 α_img 在 [0.9, 1.1]、α_vid 在 [0.7, 0.9] 范围内进行网格搜索，计算对应 Hit_Rate_mix 的变化幅

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N126

## Claim

敏感性分析区间：对 α_img 在 [0.9, 1.1]、α_vid 在 [0.7, 0.9] 范围内进行网格搜索，计算对应 Hit_Rate_mix 的变化幅度，若 ΔHit_Rate < 1%，则 α 取值对最终成本影响不显著，可固定为 1.0/0.8；若 ΔHit_Rate > 5%，则必须实测校准。

## Corrected Claim

敏感性分析区间：对 α_img 在 [0.9, 1.1]、α_vid 在 [0.7, 0.9] 范围内进行网格搜索，计算对应 Hit_Rate_mix 的变化幅度，若 ΔHit_Rate < 1%，则 α 取值对最终成本影响不显著，可固定为 1.0/0.8；若 ΔHit_Rate > 5%，则必须实测校准。

## Evidence

先验知识/题面给定，逻辑校验通过
