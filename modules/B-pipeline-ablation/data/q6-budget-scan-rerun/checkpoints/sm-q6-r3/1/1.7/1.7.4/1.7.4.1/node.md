# N176: 公有云CDN边缘节点密度增加的边际成本：增加节点密度通常通过购买更高阶套餐（如Cloudflare Enterprise）或阿里云CDN的“加速区域”实现。成本

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N46

## Claim

公有云CDN边缘节点密度增加的边际成本：增加节点密度通常通过购买更高阶套餐（如Cloudflare Enterprise）或阿里云CDN的“加速区域”实现。成本增加比例与节点数量成正比，但延迟降低遵循边际递减规律。每增加10%节点密度，RTT降低约5-10ms，但成本增加10-15%。

## Corrected Claim

公有云CDN边缘节点密度增加通常伴随成本上升和延迟降低，但延迟降低遵循边际递减规律，具体数值因厂商、地域及套餐而异，无统一固定比例。

## Evidence

[质询]具体数值（每增加10%密度RTT降低5-10ms，成本增加10-15%）缺乏通用性，属于特定场景下的经验估算，不同云厂商、地域及业务负载下差异巨大，无法作为普适事实。 | 先验知识/题面给定，逻辑校验通过（边际递减规律符合经济学与网络拓扑直觉），但具体数值为经验事实且无来源支持，故降级。

## Search Query

CDN edge node density cost latency tradeoff
