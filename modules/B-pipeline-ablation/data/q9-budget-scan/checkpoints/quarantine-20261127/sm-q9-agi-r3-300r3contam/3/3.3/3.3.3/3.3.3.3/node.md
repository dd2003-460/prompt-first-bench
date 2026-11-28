# N158: 本地知识库增强（RAG）可将有效覆盖率提升至 C_rag = C_internal + (1-C_internal)*R_retrieval_accuracy；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N61

## Claim

本地知识库增强（RAG）可将有效覆盖率提升至 C_rag = C_internal + (1-C_internal)*R_retrieval_accuracy；若 R_retrieval_accuracy=0.95（基于本地向量库），则 C_rag ≈ 0.95 + 0.05*0.95 = 0.9975，使 P_offline_rag ≈ 0.0025，理论上可逼近 <5% 目标但受限于检索噪声

## Corrected Claim

本地知识库增强（RAG）可将有效覆盖率提升至 C_rag = C_internal + (1-C_internal)*R_retrieval_accuracy；若 R_retrieval_accuracy=0.95（基于本地向量库），则 C_rag ≈ 0.95 + 0.05*0.95 = 0.9975，使 P_offline_rag ≈ 0.0025，理论上可逼近 <5% 目标但受限于检索噪声

## Evidence

先验知识/题面给定，逻辑校验通过：公式 C_rag = C_internal + (1-C_internal)*R 符合概率论中全概率公式或贝叶斯推断的基本逻辑（假设内部覆盖与检索覆盖互补且独立），数值计算 0.95 + 0.05*0.95 = 0.9975 正确，P_offline = 1 - 0.9975 = 0.0025 亦正确，符合 <5% 目标的描述。

## Search Query

RAG retrieval augmented generation reduce citation hallucination local vector store accuracy
