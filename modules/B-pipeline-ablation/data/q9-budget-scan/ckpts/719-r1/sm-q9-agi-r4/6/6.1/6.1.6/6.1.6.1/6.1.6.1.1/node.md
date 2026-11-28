# N710: V100-SXM2-16GB 在标准 SXM2 模块（被动散热）配置下，官方规格书未明确单一固定的 90°C 节流阈值，实际降频触发温度取决于机箱气流与背板温度

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N261

## Claim

V100-SXM2-16GB 在标准 SXM2 模块（被动散热）配置下，官方规格书未明确单一固定的 90°C 节流阈值，实际降频触发温度取决于机箱气流与背板温度，需查阅具体服务器厂商（如 Dell PowerEdge）的热设计规范以确定确切触发点 [待核验]

## Corrected Claim

V100-SXM2-16GB 在标准 SXM2 模块配置下，其热管理策略通常由服务器厂商定制，官方通用规格书可能未指定统一的固定节流温度，实际降频行为受机箱散热设计影响，建议查阅具体服务器厂商的热设计规范以确认细节。

## Evidence

[质询]该陈述包含具体的硬件行为断言（如‘未明确单一固定90°C阈值’、‘取决于机箱气流’），属于经验事实。由于缺乏官方规格书或权威技术文档的直接引用，无法排除不同固件版本或特定OEM实现中存在固定阈值的可能性，存在将一般性推测当作绝对事实的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法进行外部核验）

## Search Query

Tesla V100 SXM2 passive cooling thermal throttling temperature threshold server spec
