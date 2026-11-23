# N121: 缓存命中时的内部带宽成本 p_cache 的具体数值：p_cache 通常为外部带宽成本的 10-30%，即 p_cache ≈ 0.02-0.15 * p_d

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

缓存命中时的内部带宽成本 p_cache 的具体数值：p_cache 通常为外部带宽成本的 10-30%，即 p_cache ≈ 0.02-0.15 * p_download；对于公有云CDN，p_cache ≈ ¥0.02-0.05/GB；对于自建节点，p_cache ≈ ¥0.005-0.01/GB [待核验]

## Corrected Claim

缓存命中时的内部带宽成本 p_cache 通常显著低于外部带宽成本，具体数值需依据特定云服务商或自建集群的定价策略确定，一般经验值为外部成本的10-30%。

## Evidence

[质询]来源主题不匹配：参考来源讨论的是LLM推理中的KV Cache（显存/计算缓存），而事实节点讨论的是CDN/网络传输中的带宽成本（p_cache vs p_download），两者属于完全不同的技术领域，来源无法支持该数值。 | 逻辑上，内部带宽成本低于外部带宽成本符合经济直觉，数值量级（0.02-0.15倍）在工程上合理；但参考来源[1]主题为LLM KV Cache，与CDN带宽成本无关，无法提供外部支持，且该事实为经验参数，适用经验事实排除条款。

## Search Query

CDN internal bandwidth cost vs external bandwidth cost 2024

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2045143515269706934&rut=4f39739a19208dd7d267775467fad48214254b1886e24a5ccc6b52340d28e2b3', 'type': 'ddg', 'title': '一文说清大模型缓存命中机制，同样的token，命中和未命中价格相差120倍!不懂KV Cache的人，每个月都在白烧钱'}
