# N45: 幻觉抑制的边际成本分析：将 Score 从 80% 提升至 90% 所需的额外计算资源主要集中在检索阶段的向量数据库查询与重排序 (Reranking)；使用 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N11

## Claim

幻觉抑制的边际成本分析：将 Score 从 80% 提升至 90% 所需的额外计算资源主要集中在检索阶段的向量数据库查询与重排序 (Reranking)；使用 Cross-Encoder (如 bge-reranker-base) 对 Top-20 候选进行重排序，单次查询延迟增加约 50-100 ms，GPU 利用率增加 5%；若 Score 仍需提升至 95% 以上，需引入外部 API (如 GPT-4o) 进行事实核查，成本增加约 $0.01-0.02 每 1000 tokens，此时云端 API 成为主要成本驱动项。

## Corrected Claim

幻觉抑制的边际成本分析：将 Score 从 80% 提升至 90% 所需的额外计算资源主要集中在检索阶段的向量数据库查询与重排序 (Reranking)；使用 Cross-Encoder 对 Top-20 候选进行重排序通常会带来显著的延迟增加（具体取决于硬件与并发量）及 GPU 负载上升；若 Score 需进一步提升至 95% 以上，引入外部大模型 API 进行事实核查往往会使云端 API 调用成为主要成本驱动项。

## Evidence

[质询]数值量级与具体参数缺乏普适性：Cross-Encoder 的延迟和 GPU 利用率高度依赖硬件配置（如 A100 vs T4）和 Batch Size，50-100ms 和 5% 利用率并非固定常数；GPT-4o 的成本随版本迭代波动，$0.01-0.02/1k tokens 仅为特定时间点的快照，作为通用事实陈述过于绝对。 | 先验知识/题面给定，逻辑校验通过（量级符合工程常识，无内部矛盾），但具体数值为经验参数且无外部来源支持，依据经验事实排除条款降级。
