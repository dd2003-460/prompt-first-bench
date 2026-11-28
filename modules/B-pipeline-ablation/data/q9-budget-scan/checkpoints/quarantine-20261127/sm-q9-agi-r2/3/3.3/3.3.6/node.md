# N63: 增量更新机制：当新增文献 N_new=500 篇/月时，全量重建索引耗时 T_rebuild ≈ 22 小时，而增量插入耗时 T_incremental ≈ N

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16, N17, N18

## Claim

增量更新机制：当新增文献 N_new=500 篇/月时，全量重建索引耗时 T_rebuild ≈ 22 小时，而增量插入耗时 T_incremental ≈ N_new * (T_embed + T_insert_HNSW) ≈ 500 * (0.8 + 0.02) ≈ 7 分钟。因此，采用月度增量更新策略可将系统可用性停机时间从 22 小时降至 < 15 分钟，且保证文献新鲜度滞后 < 30 天。

## Corrected Claim

采用月度增量更新策略通常能显著降低系统可用性停机时间（相比全量重建），并保证文献新鲜度滞后在一个月以内，具体耗时取决于系统规模与硬件配置。

## Evidence

[质询]陈述中的具体数值（T_rebuild=22h, T_embed=0.8s, T_insert_HNSW=0.02s）属于特定系统配置下的经验参数，并非通用物理常数或数学定理，无法从第一性原理严格推导得出；不同硬件、向量维度及HNSW参数下这些数值会有显著差异。 | 逻辑计算自洽（500*0.82s≈410s≈7min），且来源[1][2][3]均支持“增量更新优于全量重建”的工程结论，但未提供具体的耗时数值支持，故依据经验事实排除条款降级。

## Search Query

vector database incremental update FAISS HNSW insertion latency vs full rebuild time

## Retrieval Sources

- {'url': 'https://javaguide.cn/ai/rag/rag-knowledge-update.html&rut=83f669ac4b7c95dea2fbd8d46ad775c5b579f6003de7876d5dc6f0711b210bf2', 'type': 'ddg', 'title': 'RAG 知识库文档如何更新：增量更新、版本控制、去重与全量重建 | JavaGuide'}
- {'url': 'https://blog.csdn.net/qq_21103417/article/details/157799274&rut=d0a7a7a4e241a9a9ccb43903cb45fc7969689695f46cded816db9da98e3d0cb6', 'type': 'ddg', 'title': '大模型实战：Rag 知识库的实时更新与增量同步实战_知识库的增量同步机-csdn博客'}
- {'url': 'https://blog.csdn.net/2401_87746054/article/details/162574723&rut=106cd196d6c064fe7ee69866b09447a81ef668592fe0b3c023092cef080ba5ae', 'type': 'ddg', 'title': 'Rag 增量索引：知识库更新不能靠全量重建硬扛-csdn博客'}
