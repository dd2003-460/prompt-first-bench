# N15: Pareto(β=0.9)热度分布下，累计请求占比特征：β<1意味着分布极重尾，头部极少对象占据绝大部分流量。具体地，前0.1%的对象（100个）可能占据>50

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Pareto(β=0.9)热度分布下，累计请求占比特征：β<1意味着分布极重尾，头部极少对象占据绝大部分流量。具体地，前0.1%的对象（100个）可能占据>50%的请求，前1%（1000个）占据>90%。LRU的稳态命中率下界受限于其能否锁定这些头部对象。由于LRU基于时间局部性，而热度是静态偏好的，LRU可能在头部对象间频繁抖动，导致命中率低于基于频率的理论上限。

## Corrected Claim

Pareto(β=0.9)热度分布下，由于β<1，分布呈现极重尾特征，头部极少对象占据绝大部分流量（具体占比需根据分布参数精确计算，通常头部集中度极高）。LRU的稳态命中率受限于其能否锁定这些头部对象。由于LRU基于时间局部性，而热度是静态偏好的，LRU可能在头部对象间频繁抖动，导致命中率低于基于频率的理论上限。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点1和子节点4存在严重冗余，子节点4仅是子节点1中公式在k=0.001时的具体数值实例，且两者都涉及流量占比计算，未体现正交性。此外，子节点1中的数值计算（63.1%）与父节点描述的“>90%”存在潜在矛盾（取决于具体模型定义，但通常Pareto尾部更重，需确认公式适用性），且子节点2和3侧重于LRU机制，与1/4的分布统计特征分离较好，但1和4的重复破坏了整体正交性。）

## Retrieval Sources

- {'url': 'https://www.datacamp.com/zh/tutorial/pareto-distribution&rut=7d516237fe1cc69a2d1adba2d09af33d05af69c49a98f97fb2cf9b2168a21a27', 'type': 'ddg', 'title': '帕累托分布：全面指南 | DataCamp'}
- {'url': 'https://blog.csdn.net/luoganttcc/article/details/154403496&rut=feadc4bf451b9ff376681387e9341b7387def803b82a37989e827acb84a07358', 'type': 'ddg', 'title': '介绍一下帕累托分布 包括概率密度函数，概率分布 和 期望计算与证明_恒盛登陆xk7富3.4.6.5.6杏-CSDN博客'}
- {'url': 'https://cloud.tencent.com/developer/article/2536950&rut=17918e1a2d423f8624116a6d6413af6af418fb42dbdf777d00bfe19e0d3fb15a', 'type': 'ddg', 'title': '数分人必知必会 | 分析方法：帕累托累计-腾讯云开发者社区-腾讯云'}
