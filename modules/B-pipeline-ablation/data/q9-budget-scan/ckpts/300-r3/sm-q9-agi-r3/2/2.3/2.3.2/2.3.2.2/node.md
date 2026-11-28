# N207: 混合检索打分函数 Score(d,q) = w_semantic * S_sem(d,q) + w_keyword * S_kw(d,q)，其中 S_sem 为

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

混合检索打分函数 Score(d,q) = w_semantic * S_sem(d,q) + w_keyword * S_kw(d,q)，其中 S_sem 为归一化余弦相似度 [0,1]，S_kw 为 BM25 分数归一化值 [0,1]，当前基线参数 w_semantic=0.7, w_keyword=0.3

## Corrected Claim

混合检索打分函数 Score(d,q) = w_semantic * S_sem(d,q) + w_keyword * S_kw(d,q)，其中 S_sem 为归一化余弦相似度 [0,1]，S_kw 为 BM25 分数归一化值 [0,1]，当前基线参数 w_semantic=0.7, w_keyword=0.3

## Evidence

先验知识/题面给定，逻辑校验通过
