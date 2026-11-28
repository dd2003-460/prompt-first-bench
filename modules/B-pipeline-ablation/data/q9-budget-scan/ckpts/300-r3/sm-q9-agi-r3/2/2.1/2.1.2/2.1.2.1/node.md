# N176: Top-K检索的Token开销公式：Cost_K = K * Avg_Doc_Tokens，假设Avg_Doc_Tokens=500，则K=3时开销1.5k，K

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

Top-K检索的Token开销公式：Cost_K = K * Avg_Doc_Tokens，假设Avg_Doc_Tokens=500，则K=3时开销1.5k，K=5时开销2.5k，K=10时开销5k；K=5时的2.5k开销符合<2k的预期边界（需微调Avg_Doc_Tokens至400以内以满足<2k）

## Corrected Claim

Top-K检索的Token开销公式：Cost_K = K * Avg_Doc_Tokens。假设Avg_Doc_Tokens=500，则K=3时开销1.5k，K=5时开销2.5k，K=10时开销5k。K=5时的2.5k开销超出了<2k的预期边界，需将Avg_Doc_Tokens微调至400以内（即 Cost_5 = 5*400 = 2.0k，若严格小于2k则需<400）才能满足该约束。

## Evidence

[质询]陈述内部存在逻辑矛盾：前半部分基于 Avg_Doc_Tokens=500 计算出 K=5 时开销为 2.5k，后半部分却声称该 2.5k 开销“符合 <2k 的预期边界”，这在数值上是不成立的（2.5k > 2k）。此外，将“需要微调参数才能满足边界”描述为“符合边界”属于概念混淆。 | 先验知识/题面给定，逻辑校验发现内部数值矛盾（2.5k 不符合 <2k 边界），故降级。
