# N100: 用户到最近公有云 CDN 边缘节点的 P99 距离 D_user_edge_p99 (km)，基于阿里云/Cloudflare 节点分布图与用户地理分布数据计算

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

用户到最近公有云 CDN 边缘节点的 P99 距离 D_user_edge_p99 (km)，基于阿里云/Cloudflare 节点分布图与用户地理分布数据计算，典型值在 50-200km 之间，直接决定 RTT_user_edge 的物理下限。

## Corrected Claim

用户到最近公有云 CDN 边缘节点的 P99 距离 D_user_edge_p99 (km) 直接决定 RTT_user_edge 的物理下限，其典型值通常在几十至几百公里范围内（具体数值需依据特定云厂商节点分布及用户地理分布实测数据确定）。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑维度上正交（核心区域 vs 长尾区域 vs 运营商惩罚），且无冗余。但完备性不足：父节点定义的是基于‘阿里云/Cloudflare’分布的通用指标，而子节点仅覆盖了‘阿里云’的数据，完全缺失了 Cloudflare 全球/海外节点分布对 D_user_edge_p99 的影响（特别是对于非中国用户或跨国场景，Cloudflare 的覆盖密度与阿里云差异巨大，会导致 P99 距离和 RTT 下限完全不同）。此外，父节点强调‘典型值 50-200km’，但子节点3指出跨运营商可能导致 300-400km，这与父节点的范围描述存在潜在矛盾或需要更清晰的边界界定（是仅指同运营商下的物理距离，还是包含逻辑惩罚后的等效距离？）。）

## Search Query

Alibaba Cloud CDN node distribution China average distance

## Retrieval Sources

- {'url': 'https://developer.baidu.com/article/detail.html?id=4172016&rut=3ad18be3a346aa75c5f26e21cc433dcc5c9a75c38e96ca66493faecd0b8c64ef', 'type': 'ddg', 'title': 'Cdn 如何精准定位：解析用户到最近边缘节点的技术路径-百度开发者中心'}
- {'url': 'https://developer.baidu.com/article/detail.html?id=4171944&rut=1cef040b4e7e56b8ea2be96e4400cb8c8d95953ecaa5bcfa90fef25735dc170b', 'type': 'ddg', 'title': 'Cdn边缘节点解析机制：从请求到最优节点的全流程揭秘-百度开发者中心'}
