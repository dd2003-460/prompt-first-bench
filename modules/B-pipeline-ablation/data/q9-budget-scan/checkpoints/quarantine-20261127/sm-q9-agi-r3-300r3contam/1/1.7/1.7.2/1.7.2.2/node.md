# N138: Topic Anchor 的构造算法：从用户指定的研究方向描述中提取 Top-K (K=5) 关键短语，对每个短语生成嵌入后取平均向量作为 E_topic_an

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

Topic Anchor 的构造算法：从用户指定的研究方向描述中提取 Top-K (K=5) 关键短语，对每个短语生成嵌入后取平均向量作为 E_topic_anchor；若描述长度 <50 tokens，直接整体嵌入。

## Corrected Claim

Topic Anchor 的构造算法：从用户指定的研究方向描述中提取 Top-K (K=5) 关键短语，对每个短语生成嵌入后取平均向量作为 E_topic_anchor；若描述长度 <50 tokens，直接整体嵌入。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

semantic drift detection topic anchor vector construction method
