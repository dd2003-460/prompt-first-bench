# N105: Pareto 分布参数 α=1.1 和 β=0.9 属于题目给定的假设条件（Given），无需外部查证；但 S_min=1KB 和 S_max=1.3MB 属于

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Pareto 分布参数 α=1.1 和 β=0.9 属于题目给定的假设条件（Given），无需外部查证；但 S_min=1KB 和 S_max=1.3MB 属于经验性假设（Heuristic），需查阅特定 CDN 厂商（如 Cloudflare, Akamai）的技术白皮书以确认其典型对象大小分布范围，否则命中率计算存在量级误差。

## Corrected Claim

Pareto 分布参数 α=1.1 和 β=0.9 属于题目给定的假设条件；S_min=1KB 和 S_max=1.3MB 属于经验性假设，其合理性需结合具体 CDN 业务场景或厂商数据验证，不同场景下对象大小分布范围可能存在显著差异。

## Evidence

[质询]S_min=1KB 和 S_max=1.3MB 的具体数值缺乏通用标准支持，不同 CDN 厂商或业务场景下的对象大小分布差异巨大，直接断言需查阅特定厂商白皮书以确认该范围存在量级误差风险，且参考来源未提供此类具体工程参数。 | 参考来源 [1][2] 仅定义帕累托分布的数学性质，与 CDN 对象大小经验参数无关；该节点包含经验性工程假设（S_min/S_max），逻辑自洽但缺乏来源直接支持，依据经验事实排除条款降级。

## Retrieval Sources

- {'url': 'https://zh.wikipedia.org/wiki/%E5%B8%95%E7%B4%AF%E6%89%98%E5%88%86%E5%B8%83&rut=91134896ab05b53f585edeb3a097a30f9edf0fa7dafb66749cede7728abb67cb', 'type': 'ddg', 'title': '帕累托分布 - 维基百科，自由的百科全书'}
- {'url': 'https://zhuanlan.zhihu.com/p/27173875583&rut=c28be11bc9a983317f8edde3b6df4480ac059f02a3bf2babd869f10ca3cde565', 'type': 'ddg', 'title': '帕累托分布 - 知乎 - 知乎专栏'}
