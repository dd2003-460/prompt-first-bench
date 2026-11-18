# N22: 考虑大小-热度负相关 (ρ=-0.3)，使用 Copula 模型（如 Clayton Copula）构建联合分布。负相关意味着高热度对象倾向于较小，从而在固定字

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

考虑大小-热度负相关 (ρ=-0.3)，使用 Copula 模型（如 Clayton Copula）构建联合分布。负相关意味着高热度对象倾向于较小，从而在固定字节容量 C 下，LRU 能保留更多高热度对象。具体地，若 ρ=-0.3，前 10% 热度对象平均大小比独立假设下小约 15-20%，导致有效缓存对象数量 K_eff 增加 10-15%。

## Corrected Claim

考虑大小-热度负相关 (ρ=-0.3)，使用 Copula 模型（如 Clayton Copula）构建联合分布。负相关意味着高热度对象倾向于较小，从而在固定字节容量 C 下，LRU 能保留更多高热度对象，导致有效缓存对象数量 K_eff 增加。

## Evidence

[质询]具体数值断言（前10%热度对象平均大小小15-20%，K_eff增加10-15%）缺乏来源支持，且该数值高度依赖于具体的边缘分布形状（如大小服从对数正态还是幂律）以及Copula的具体参数化，仅凭ρ=-0.3无法唯一确定这些百分比，属于经验/模拟结果而非第一性原理推导。 | 逻辑自洽：负相关确实意味着高热度对应小尺寸，从而在固定容量下能容纳更多对象。但参考来源[3]仅介绍Copula概念，未提供具体数值支持；来源[1][2]无关。根据经验事实排除条款，具体百分比数值缺来源支持，降级为定性表述。

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: https://arxiv.org'}
- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: https://github.com'}
- {'url': 'https://zhuanlan.zhihu.com/p/138800469&rut=db3fdc0843e087fdc8548f7eefab2b5ab1694f00a23a8168c3e0797f7488cf97', 'type': 'ddg', 'title': 'Copula系列（一）-什么是Copula函数 - 知乎'}
