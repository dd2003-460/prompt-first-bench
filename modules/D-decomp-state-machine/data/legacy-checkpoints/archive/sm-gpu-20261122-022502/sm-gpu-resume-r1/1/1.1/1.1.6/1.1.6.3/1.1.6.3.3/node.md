# N481: 验证 32K 上下文下 INT4 实际准确率的推荐基准：LongBench (长文本理解) 或 RULER (长上下文检索能力)，具体子任务如 'Multi-N

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N148

## Claim

验证 32K 上下文下 INT4 实际准确率的推荐基准：LongBench (长文本理解) 或 RULER (长上下文检索能力)，具体子任务如 'Multi-Needle Retrieval' 或 'Variable Tracking'，用于量化 'Lost in the Middle' 的额外损失。

## Corrected Claim

验证 32K 上下文下 INT4 实际准确率的推荐基准：LongBench (长文本理解) 或 RULER (长上下文检索能力)，具体子任务如 'Multi-Needle Retrieval' 或 'Variable Tracking'，用于量化 'Lost in the Middle' 的额外损失。

## Evidence

先验知识/题面给定，逻辑校验通过：LongBench和RULER是公认的长文本/长上下文基准，Multi-Needle Retrieval和Variable Tracking是RULER中专门用于评估长上下文中间位置信息检索能力（即'Lost in the Middle'现象）的标准子任务，逻辑自洽且符合领域共识。
