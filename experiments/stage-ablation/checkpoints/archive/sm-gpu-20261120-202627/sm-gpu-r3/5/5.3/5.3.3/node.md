# N124: 最终性价比比值对比：CE_A = (15 tokens/s × 0.97) / ($3350 + $2070 + $500) ≈ 0.0018 tokens/$

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27

## Claim

最终性价比比值对比：CE_A = (15 tokens/s × 0.97) / ($3350 + $2070 + $500) ≈ 0.0018 tokens/$；CE_B = (40 tokens/s × 1.0) / ($10000 + $1140 + $100) ≈ 0.0032 tokens/$。在 3 年持有期内，工作点 B (A100) 性价比更高，除非 CapEx_B 超过 $20,000 或 OpEx_A 显著降低。

## Corrected Claim

最终性价比比值对比：CE_A = (15 tokens/s × 0.97) / ($3350 + $2070 + $500) ≈ 0.0018 tokens/$；CE_B = (40 tokens/s × 1.0) / ($10000 + $1140 + $100) ≈ 0.0032 tokens/$。在 3 年持有期内，工作点 B (A100) 性价比更高，除非 CapEx_B 超过 $20,000 或 OpEx_A 显著降低。

## Evidence

父节点级核验未通过：不完备（子节点分别针对CapEx和吞吐率两个不同维度进行敏感性分析，彼此正且不矛盾。但父节点明确提到的两个关键边界条件中，'OpEx_A 显著降低'未被任何子节点覆盖，导致完备性不足。）

## Search Query

GPU TCO analysis consumer vs datacenter LLM inference cost efficiency
