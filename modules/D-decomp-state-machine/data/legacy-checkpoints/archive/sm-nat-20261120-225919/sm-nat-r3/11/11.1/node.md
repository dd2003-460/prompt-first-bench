# N277: Cloudflare 典型对象大小分布：查阅 Cloudflare 技术白皮书，其缓存对象大小中位数约为 50KB，P95 约为 1MB，S_min 通常设为 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N105

## Claim

Cloudflare 典型对象大小分布：查阅 Cloudflare 技术白皮书，其缓存对象大小中位数约为 50KB，P95 约为 1MB，S_min 通常设为 1KB，S_max 截断于 100MB，需验证该范围是否覆盖 99% 的对象。

## Corrected Claim

Cloudflare 缓存对象大小分布的具体数值（中位数、P95等）需查阅其官方技术白皮书或公开数据集验证，当前参考来源未提供具体统计数值，仅能确认其存在对象大小限制机制。

## Evidence

[质询]该陈述包含具体的经验性统计数据（中位数50KB、P95 1MB等），属于硬件/网络流量分布的经验事实，无法从第一性原理推导。参考来源中未包含任何关于Cloudflare缓存对象大小分布的具体数值或白皮书引用，且来源[3]讨论的是DNS缓存内存优化而非对象大小分布，来源[1]和[2]为通用介绍页，均无法提供直接支持。 | 逻辑上量级合理（Web对象通常较小，100MB截断符合CDN常见限制），但作为经验事实，缺乏来源直接支持（来源[1][2][3]均无关或未提供具体数值），依据经验事实排除条款降级。

## Search Query

Cloudflare cache object size distribution median P95

## Retrieval Sources

- {'url': 'https://www.cloudflare.com/zh-cn/architecture/&rut=b9c4e019498dafcb72cd17a6c6aeb48bf8c3d009c2db9da57349b0e8516aaea7', 'type': 'ddg', 'title': '参考架构中心 | Cloudflare'}
- {'url': 'https://www.cloudflare.com/zh-cn/&rut=40c979b12eb38540ad319a6628f8a16f4d7f8533089c963b54a809300aaa2159', 'type': 'ddg', 'title': '随时随地连接、保护和构建 | Cloudflare'}
- {'url': 'https://blog.csdn.net/weixin_30702441/article/details/170894191&rut=37df50cd2e3bbfb034d98707fe8d79543239f2baf476292a107d9cd8d5c621ab', 'type': 'ddg', 'title': 'Cloudflare DNS缓存优化：域名级聚合节省100TB内存-CSDN博客'}
