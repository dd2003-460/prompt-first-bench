# N15: 外部知识库对齐 (RAG Grounding)：在生成结论时强制引用检索到的文献片段，并将引用准确率 (citation accuracy) 作为验证指标，可将

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

外部知识库对齐 (RAG Grounding)：在生成结论时强制引用检索到的文献片段，并将引用准确率 (citation accuracy) 作为验证指标，可将幻觉率降低 40-60%，但引入检索噪声风险，需设置相似度阈值 (similarity threshold > 0.85)

## Corrected Claim

外部知识库对齐 (RAG Grounding)：在生成结论时强制引用检索到的文献片段，并将引用准确率作为验证指标，通常可将幻觉率降低 30-60%（视具体实现而定），但引入检索噪声风险，需根据具体嵌入模型和数据集调优相似度阈值以平衡召回与精度。

## Evidence

[质询]数值量级与具体参数缺乏权威来源支持：来源[3]指出RAG抑制幻觉率为30%-50%，与陈述中的40-60%存在重叠但不完全一致；相似度阈值>0.85属于特定工程经验值，不同嵌入模型和场景下最优阈值差异巨大，并非通用标准，且参考来源中未提供该具体数值的直接证据。 | 来源[1][2][3]均支持RAG/Grounding能降低幻觉及需处理检索噪声的逻辑，但来源[3]给出的幻觉降低幅度(30-50%)与陈述(40-60%)不完全吻合，且所有来源均未直接支持'相似度阈值>0.85'这一具体经验参数，故降级为定性表述。

## Search Query

rag grounding hallucination reduction citation accuracy threshold

## Retrieval Sources

- {'url': 'https://blog.csdn.net/shuizhudan223/article/details/147519947&rut=606f721679eaca67083d20db51073d700791784476bfa981be09ac7f9803fcca', 'type': 'ddg', 'title': '告别 "幻觉" 回答：RAG 中知识库与生成模型的 7 种对齐策略_rag对齐-CSDN博客'}
- {'url': 'https://blog.csdn.net/u011109629/article/details/158263652&rut=46a15cd7d75ace053ea7cdcee6c1f5f9262a47d5769ca49ece9ad045351dbbca', 'type': 'ddg', 'title': 'RAG & Grounding - CSDN博客'}
- {'url': 'https://developer.aliyun.com/article/1779591&rut=af68ac651651242016d9bad4db3a55101eab38c13761006aa95b71b7e029f0a7', 'type': 'ddg', 'title': 'Rag 检索增强生成详解：从原理、架构到企业知识库落地全流程（2026 实战）-阿里云开发者社区'}
