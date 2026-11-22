# N83: LRU 有效命中率折损因子 D_LRU_bytes 的最终表达式：D_LRU_bytes = 1 - P_invalidate_bytes。若 P_invali

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

LRU 有效命中率折损因子 D_LRU_bytes 的最终表达式：D_LRU_bytes = 1 - P_invalidate_bytes。若 P_invalidate_bytes ≈ 0.001，则 D_LRU_bytes ≈ 0.999。具体数值需基于 N72 的积分结果确定。

## Corrected Claim

LRU 有效命中率折损因子 D_LRU_bytes 的最终表达式：D_LRU_bytes = 1 - P_invalidate_bytes。若 P_invalidate_bytes ≈ 0.001，则 D_LRU_bytes ≈ 0.999。具体数值需基于 N72 的积分结果确定。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU 有效命中率折损因子定义为 1 减去失效概率，数值代入 1 - 0.001 = 0.999 符合算术逻辑，且明确依赖 N72 积分结果，无内部矛盾。
