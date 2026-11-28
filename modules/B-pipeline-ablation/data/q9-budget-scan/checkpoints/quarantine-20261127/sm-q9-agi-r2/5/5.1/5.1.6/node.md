# N69: 交叉验证的推理成本倍数：Cost_Ratio = (1 + R_extra) * T_retrieval + T_verify，其中 R_extra 为触发额外

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24, N25, N26

## Claim

交叉验证的推理成本倍数：Cost_Ratio = (1 + R_extra) * T_retrieval + T_verify，其中 R_extra 为触发额外检索的概率，T_retrieval 为单次 API 调用延迟（arXiv/Semantic Scholar 平均 200-500ms），T_verify 为大模型判断一致性的 Token 消耗；需量化该机制使单次结论验证成本增加多少倍。

## Corrected Claim

交叉验证的推理成本倍数：Cost_Ratio = (1 + R_extra) * T_retrieval + T_verify，其中 R_extra 为触发额外检索的概率，T_retrieval 为单次 API 调用延迟（arXiv/Semantic Scholar 平均 200-500ms），T_verify 为大模型判断一致性的 Token 消耗；需量化该机制使单次结论验证成本增加多少倍。

## Evidence

先验知识/题面给定，逻辑校验通过
