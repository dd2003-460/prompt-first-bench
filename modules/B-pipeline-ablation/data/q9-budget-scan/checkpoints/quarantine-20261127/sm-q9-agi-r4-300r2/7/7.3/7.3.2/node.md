# N200: Map-Territory 策略中 Territory 检索的精度-召回权衡公式：Recall_k = 1 - (1 - P_hit)^k，其中 k 为检索片段

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N78

## Claim

Map-Territory 策略中 Territory 检索的精度-召回权衡公式：Recall_k = 1 - (1 - P_hit)^k，其中 k 为检索片段数，P_hit 为单片段命中概率；在 262k 上下文中，若需维持 Recall > 90%，且 P_hit ≈ 0.6 (基于 RAG 基准)，则需 k ≥ 3 个片段，总检索 Token 开销 C_territory = k * Chunk_Size * P_in

## Corrected Claim

Map-Territory 策略中 Territory 检索的精度-召回权衡公式：Recall_k = 1 - (1 - P_hit)^k，其中 k 为检索片段数，P_hit 为单片段命中概率；在 262k 上下文中，若需维持 Recall > 90%，且 P_hit ≈ 0.6 (基于 RAG 基准)，则需 k ≥ 3 个片段，总检索 Token 开销 C_territory = k * Chunk_Size * P_in

## Evidence

先验知识/题面给定，逻辑校验通过：公式 Recall_k = 1 - (1 - P_hit)^k 符合独立事件并集概率逻辑；代入 P_hit=0.6, k=3 计算得 1-(0.4)^3 = 0.936 > 0.9，数值推导正确；Token 开销公式定义清晰，无逻辑矛盾。
