# N188: 骨干网单跳延迟 L_hop_backbone 的 P99 值约为 20-30ms（受路由收敛和拥塞影响），远高于平均值 5ms；在 P99 计算中，若路径包含 

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N60

## Claim

骨干网单跳延迟 L_hop_backbone 的 P99 值约为 20-30ms（受路由收敛和拥塞影响），远高于平均值 5ms；在 P99 计算中，若路径包含 1 个骨干跳，其贡献权重应使用 P99 值而非均值。

## Corrected Claim

骨干网单跳延迟的P99值通常显著高于平均值，具体数值（如20-30ms）取决于网络拓扑、运营商及拥塞状况，并非固定常数；在P99计算中，若路径包含骨干跳，建议采用该跳的P99延迟值以保守估计尾部风险。

## Evidence

父节点级核验未通过：有冗余（子节点按负载水平（低/中/高）划分，互斥且覆盖了父节点描述的20-30ms范围及成因（拥塞）。然而，三个子节点结构完全相同，仅数值不同，本质上是对同一参数 L_hop_p99 在不同工况下的离散化取值，属于典型的参数枚举冗余。）

## Search Query

backbone network hop latency P99 congestion

## Retrieval Sources

- {'url': 'https://blog.csdn.net/dicky_zhang3/article/details/166795970&rut=68c8483b9391672943f85c2d25675dd7d98dfb8a36ced3fdcd6996efd73d30f3', 'type': 'ddg', 'title': '性能优化战报：核心链路 P99 延迟降低 40% 的全过程-csdn博客'}
- {'url': 'https://blog.csdn.net/lady_mumu/article/details/167701898&rut=f65b7c478c380419b56f57020c4cc2bd28c5e97d4961cabde2d531be59767d7f', 'type': 'ddg', 'title': '大模型评测中的长尾延迟度量：P99.9 尾部延迟归因与 Tcp Ack 延迟确认消解_长尾延时-csdn博客'}
- {'url': 'https://www.lunati.cloud/blog/p99-latency-teardown/&rut=eded0c09425a8550ec24c9adee93f64fc7db764aa8f0cbfa608000569cc6543f', 'type': 'ddg', 'title': '把登录接口的 P99 从 320ms 压到 48ms：一次完整的延迟拆解 · Lunati'}
