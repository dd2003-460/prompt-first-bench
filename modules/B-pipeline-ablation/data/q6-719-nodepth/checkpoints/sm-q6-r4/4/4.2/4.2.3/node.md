# N106: 用户到自建 POP 的 P99 距离 D_user_pop_p99 (km)，基于 10 个 POP 的地理坐标与用户分布计算，典型值在 100-300km 之

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N26

## Claim

用户到自建 POP 的 P99 距离 D_user_pop_p99 (km)，基于 10 个 POP 的地理坐标与用户分布计算，典型值在 100-300km 之间，由于 POP 数量少，其 P99 距离通常大于公有云 CDN 的 D_user_edge_p99。

## Corrected Claim

用户到自建 POP 的 P99 距离 D_user_pop_p99 (km) 基于地理坐标与用户分布计算，由于 POP 数量少，其 P99 距离通常大于公有云 CDN 的 D_user_edge_p99。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点3（整体计算）逻辑上依赖于子节点1和2，导致概念重叠；且子节点4（RTT转换）超出了父节点“距离定义”的范畴，属于下游指标，破坏了正交性。子节点1和2本质上是同一参数在不同用户群体下的取值，存在结构性冗余。）

## Search Query

self-built CDN POP node coverage radius distance

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1907850060240257948&rut=f8568459f53c969be6c08e9ce6f128269cd34bc1378fc3538a037e0cd1594e62', 'type': 'ddg', 'title': '运维必懂：监控指标中的 P90、P95、P99，到底是个啥？'}
