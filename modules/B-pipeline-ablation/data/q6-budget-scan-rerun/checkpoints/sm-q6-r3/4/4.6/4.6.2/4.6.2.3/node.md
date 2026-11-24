# N239: 公有云CDN SLA赔偿的触发条件门槛：通常要求月度可用性低于99.9%且故障持续时间超过特定阈值（如15分钟），低于该阈值的短暂抖动不计入赔偿，需量化'可赔偿

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N88

## Claim

公有云CDN SLA赔偿的触发条件门槛：通常要求月度可用性低于99.9%且故障持续时间超过特定阈值（如15分钟），低于该阈值的短暂抖动不计入赔偿，需量化'可赔偿故障'与'不可赔偿抖动'的边界

## Corrected Claim

公有云CDN SLA赔偿通常基于月度服务可用性指标，当可用性低于承诺值（常见为99.9%或99.95%）时触发赔偿，具体故障时长排除条款（如短暂抖动不计入）因厂商而异，需查阅具体服务商的SLA文档以确定‘可赔偿故障’的精确边界。

## Evidence

[质询]陈述中提到的具体数值阈值（99.9%、15分钟）属于特定厂商的经验性SLA参数，并非行业通用标准或第一性原理可推导事实；不同云厂商（如阿里云、AWS、Cloudflare）的SLA定义、可用性计算口径及故障排除条款存在显著差异，直接将其概括为“通常要求”存在以偏概全的风险，且参考来源仅提供了百度智能云的赔偿上限，未直接证实该具体阈值组合的普遍性。 | 来源[1]证实了CDN SLA存在基于月度可用性的赔偿机制及赔偿上限（50%），间接支持了“存在赔偿门槛”的逻辑，但未直接提供“99.9%”或“15分钟”的具体阈值数据，属于间接支持；因具体数值为经验事实且缺乏多源一致的直接证据，依据经验事实排除条款降级。

## Search Query

CDN SLA compensation trigger threshold minimum downtime

## Retrieval Sources

- {'url': 'https://intl.cloud.baidu.com/en/doc/CDN/s/ljwvyek8d&rut=b36575539b6add67c2f71cefe654362119d61c56785ab8a83ccc09a2baaae952', 'type': 'ddg', 'title': '产品服务等级协议sla - 内容分发网络cdn | 百度智能云文档'}
