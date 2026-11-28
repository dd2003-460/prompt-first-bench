# N206: MRR@10 的计算公式定义为 MRR@10 = (1/|Q|) * Σ (1/rank_i)，其中 rank_i 是第 i 个查询在 Top-10 结果中第一

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

MRR@10 的计算公式定义为 MRR@10 = (1/|Q|) * Σ (1/rank_i)，其中 rank_i 是第 i 个查询在 Top-10 结果中第一个正确文档的排名位置，若前10无正确文档则该项为0

## Corrected Claim

MRR@10 的计算公式定义为 MRR@10 = (1/|Q|) * Σ (1/rank_i)，其中 rank_i 是第 i 个查询在 Top-10 结果中第一个正确文档的排名位置，若前10无正确文档则该项为0

## Evidence

先验知识/题面给定，逻辑校验通过
