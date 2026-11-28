# N44: Qwen3.8-27B 在无 RAG 辅助下的基线事实一致性得分 Score_base ≈ 55-65% (基于 LLM-as-a-Judge 在 Truthf

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N11

## Claim

Qwen3.8-27B 在无 RAG 辅助下的基线事实一致性得分 Score_base ≈ 55-65% (基于 LLM-as-a-Judge 在 TruthfulQA 或类似基准上的表现)；引入 RAG 后，若检索召回率 Recall@5 > 0.9 且检索精度 Precision@5 > 0.8，Score_rag 可提升至 85-92%；要达到 >90% 的目标，需确保 RAG 系统的 MRR (Mean Reciprocal Rank) > 0.85，且嵌入模型 (bge-large-en-v1.5) 在特定科研领域微调后的 nDCG@10 提升至少 0.1。

## Corrected Claim

Qwen3.8-27B 在无 RAG 辅助下的基线事实一致性得分通常在中等水平（约 50-70% 区间，视具体基准而定）；引入高召回率和高精度的 RAG 系统后，得分通常有显著提升（可达 80-90%+）；要达到 >90% 的高一致性目标，通常需要 RAG 系统具备较高的排序质量（如 MRR > 0.8）以及针对特定领域优化的嵌入模型。

## Evidence

[质询]该陈述包含大量具体的经验性数值阈值（如 Score_base 55-65%, MRR > 0.85, nDCG 提升 0.1 等），这些并非从第一性原理或数学公理可严格推导出的必然结论，而是依赖于特定数据集、评估协议和模型版本的经验观测值。此外，Qwen3.8-27B 这一具体型号及其在特定基准上的精确表现属于经验事实，缺乏通用性保证。 | 经验事实，逻辑自洽但缺来源支持
