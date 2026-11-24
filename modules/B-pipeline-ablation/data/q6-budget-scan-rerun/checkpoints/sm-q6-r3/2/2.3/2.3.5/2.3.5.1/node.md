# N217: 公有云 CDN 基础监控包含项与免费额度界定：阿里云 CloudMonitor 基础版免费包含 CPU、内存、网络流量等基础指标，但自定义指标（Custom M

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N74

## Claim

公有云 CDN 基础监控包含项与免费额度界定：阿里云 CloudMonitor 基础版免费包含 CPU、内存、网络流量等基础指标，但自定义指标（Custom Metrics）和告警规则数量有上限（如 100 条规则）。超出部分或启用高级功能（如链路追踪 Tracing Analysis）需付费。需量化基础免费额度是否覆盖 10 个 POP 点的核心 SLA 监控需求，若不足，增量成本约为 ¥5,000-10,000/年。

## Corrected Claim

阿里云 CloudMonitor 基础版提供基础指标监控及有限的免费告警资源（如短信、API调用额度），具体告警规则数量上限及超出后的成本需根据实际配置和最新计费文档确认，10个POP点的核心SLA监控可能涉及额外付费项。

## Evidence

[质询]陈述中关于“100条规则”的具体数值上限以及“¥5,000-10,000/年”的增量成本估算属于具体经验参数，参考来源仅提供了短信和API调用的免费额度（1000条短信/100万次API），未直接证实告警规则的具体数量上限或该特定场景下的成本区间，存在数值口径不匹配风险。 | 来源[1][2][3]证实了阿里云CloudMonitor存在基础免费额度（如短信、API调用），支持了“基础监控包含免费项”的逻辑，但未直接覆盖“100条规则”及具体成本数值，属于经验事实缺直接来源支持。

## Search Query

Aliyun CloudMonitor free tier limits custom metrics pricing

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cms/cloudmonitor-1-0/product-overview/free-quota&rut=042205efa0d9649efffed48a42d3b8611a071a8e2c4c23674c86f32f928e2d5f', 'type': 'ddg', 'title': '基础云监控的免费项与额度说明-云监控-阿里云'}
- {'url': 'https://help.aliyun.com/zh/cms/cloudmonitor-2-0/free-quota&rut=ab5f522eddc2982c76ced0aabf3775d94d0c9056fc89f5eb69ce91cd8328b134', 'type': 'ddg', 'title': '基础云监控免费项与额度-云监控-阿里云'}
- {'url': 'https://www.alibabacloud.com/help/tc/cms/cloudmonitor-2-0/free-quota&rut=0126c704c69fee15a091d61cfc940ab62cb7ec612d819b83bcbf38fab60d957c', 'type': 'ddg', 'title': '瞭解CloudMonitor免費配額和隨用隨付閾值 - CloudMonitor - 阿里雲'}
