# N165: Cloudflare全球节点分布：280+城市，但中国大陆无直接节点，需通过合作伙伴（如阿里云）接入；国内用户访问Cloudflare节点需跨境，RTT_avg

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N44

## Claim

Cloudflare全球节点分布：280+城市，但中国大陆无直接节点，需通过合作伙伴（如阿里云）接入；国内用户访问Cloudflare节点需跨境，RTT_avg为80-150ms，P99可达200-300ms，远超国内CDN标准

## Corrected Claim

Cloudflare全球节点分布广泛（280+城市），但中国大陆无直接节点，需通过合作伙伴接入；国内用户访问需跨境，通常面临较高的网络延迟（RTT显著高于国内CDN标准），具体延迟数值随网络状况波动。

## Evidence

[质询]RTT数值（80-150ms）和P99延迟（200-300ms）属于具体经验数据，受网络状况、具体接入点及测量时间影响极大，缺乏实时或特定场景下的精确来源支持，存在数值量级偏差的可能。 | 先验知识/题面给定，逻辑校验通过：Cloudflare在中国大陆无直接节点是公认事实，跨境访问导致高延迟符合网络物理规律；但具体RTT数值为经验事实，无来源直接支持，故降级。

## Search Query

Cloudflare China node distribution RTT latency domestic users
