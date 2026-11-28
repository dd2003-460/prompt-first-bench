# N17: 工具调用接口采用MCP（Model Context Protocol）标准，支持文件读写、Python执行、HTTP请求、数据库查询4类基础工具，每次工具调用的

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

工具调用接口采用MCP（Model Context Protocol）标准，支持文件读写、Python执行、HTTP请求、数据库查询4类基础工具，每次工具调用的平均延迟为50-200ms，错误重试机制设置为最多3次，失败率目标<2%。

## Corrected Claim

工具调用接口采用MCP（Model Context Protocol）标准，通常支持文件操作、代码执行、网络请求等基础工具，具体延迟、重试策略及失败率目标取决于具体实现配置。

## Evidence

[质询]该陈述包含具体的工程实现细节（如特定的4类工具列表、精确的延迟范围50-200ms、重试次数3次及失败率目标<2%），这些属于特定系统的设计规格或经验数据，并非MCP协议标准本身定义的通用属性，且缺乏来源佐证其普遍性或准确性。 | source=knowledge，逻辑自洽（MCP确实支持工具调用，延迟和重试机制在工程上合理），但具体数值和工具分类属于特定实现的经验事实，无来源直接支持，依据经验事实排除条款降级。

## Search Query

MCP Model Context Protocol tool call latency
