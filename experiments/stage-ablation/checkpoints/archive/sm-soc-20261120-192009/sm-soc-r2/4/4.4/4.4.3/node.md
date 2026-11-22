# N88: 工具变量识别策略：若混杂不可控，使用平台算法推送时间戳 Push_t 作为工具变量，需满足相关性（Cov(Push_t, Price_High) ≠ 0）和排他

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

工具变量识别策略：若混杂不可控，使用平台算法推送时间戳 Push_t 作为工具变量，需满足相关性（Cov(Push_t, Price_High) ≠ 0）和排他性（Push_t 仅通过 Price_High 影响 Y）。

## Corrected Claim

工具变量识别策略：若混杂不可控，使用平台算法推送时间戳 Push_t 作为工具变量，需满足相关性（Cov(Push_t, Price_High) ≠ 0）和排他性（Push_t 仅通过 Price_High 影响 Y）。

## Evidence

[质询]排他性假设（Exclusion Restriction）在实证中难以严格验证，且平台推送时间戳可能通过影响用户注意力或购买意愿直接作用于结果变量 Y，而不仅仅通过价格机制，这构成了对排他性的潜在威胁。 | 先验知识/题面给定，逻辑校验通过。该陈述准确描述了工具变量法（IV）在因果推断中的标准识别条件（相关性与非排他性/排他性），属于计量经济学方法论的标准定义，逻辑自洽且无内部矛盾。
