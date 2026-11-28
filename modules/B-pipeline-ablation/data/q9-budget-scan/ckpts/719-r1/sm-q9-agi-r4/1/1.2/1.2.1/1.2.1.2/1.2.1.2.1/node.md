# N381: 位置偏差修正公式：Recall_corrected(pos) = Recall_raw(pos) - Δ_bias(pos)，其中 Δ_bias(pos) 为在

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N124

## Claim

位置偏差修正公式：Recall_corrected(pos) = Recall_raw(pos) - Δ_bias(pos)，其中 Δ_bias(pos) 为在相同 pos 位置下，随机内容（无针）被误召回的概率。若针在前 10% 位置 Recall_raw=90%，中间位置 Recall_raw=80%，则 Δ_bias(前10%) ≈ 10%，需通过对照实验（无针组）量化此偏移量

## Corrected Claim

位置偏差修正公式：Recall_corrected(pos) = Recall_raw(pos) - Δ_bias(pos)，其中 Δ_bias(pos) 为在相同 pos 位置下，随机内容（无针）被误召回的概率。若针在前 10% 位置 Recall_raw=90%，中间位置 Recall_raw=80%，则 Δ_bias(前10%) ≈ 10%，需通过对照实验（无针组）量化此偏移量

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

position bias correction LLM long context retrieval recall raw vs corrected
