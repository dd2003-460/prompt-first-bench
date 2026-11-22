# N290: 关键数值冲突解决规则：当同一参数（如 H100 价格）存在 [Verified] 和 [Memory] 两个不同值时，最终答案必须采用 [Verified] 值

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

关键数值冲突解决规则：当同一参数（如 H100 价格）存在 [Verified] 和 [Memory] 两个不同值时，最终答案必须采用 [Verified] 值，并在注释中说明 [Memory] 值的偏差及原因（如 'Memory 值基于 2023Q1 市场报价，未反映 2024Q4 降价'）。若两个 [Verified] 来源冲突，必须标记为 [Conflict] 并暂停使用该节点，直到找到更高权威来源（如官方定价 vs 第三方新闻）。

## Corrected Claim

关键数值冲突解决规则：当同一参数（如 H100 价格）存在 [Verified] 和 [Memory] 两个不同值时，最终答案必须采用 [Verified] 值，并在注释中说明 [Memory] 值的偏差及原因（如 'Memory 值基于 2023Q1 市场报价，未反映 2024Q4 降价'）。若两个 [Verified] 来源冲突，必须标记为 [Conflict] 并暂停使用该节点，直到找到更高权威来源（如官方定价 vs 第三方新闻）。

## Evidence

先验知识/题面给定，逻辑校验通过
