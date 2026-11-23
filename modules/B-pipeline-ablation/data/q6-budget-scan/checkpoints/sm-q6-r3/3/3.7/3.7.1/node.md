# N118: 缓存命中率 H_cache 的具体数值：基于 Zipf 分布 α=1.0 和 N_objects=100,000，H_cache ≈ 0.85-0.90；若 α

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

缓存命中率 H_cache 的具体数值：基于 Zipf 分布 α=1.0 和 N_objects=100,000，H_cache ≈ 0.85-0.90；若 α=0.9，H_cache ≈ 0.75-0.80；具体值需通过实际日志数据校准 [待核验]

## Corrected Claim

在Zipf分布（α=1.0）且对象总数为100,000的场景下，缓存命中率通常较高（具体数值取决于缓存容量与访问模式，需通过实际日志校准，典型高负载场景下可能处于0.8-0.9区间，但非固定值）。

## Evidence

[质询]该陈述给出了基于特定参数（Zipf α=1.0, N=100,000）的具体数值范围（0.85-0.90），这属于经验事实/具体参数值，无法仅从第一性原理严格推出（命中率还强烈依赖于缓存大小、请求频率等未给定的变量），且参考来源均未提供该具体数值的支持。 | 逻辑上，Zipf分布下头部对象集中度高，高命中率在量级上合理，但具体数值0.85-0.90缺乏来源直接支持（来源[1]仅讨论CDN缓存故障排查，未提供Zipf参数下的具体命中率公式或数值；来源[2][3]无关）。根据经验事实排除条款，此类具体参数值若无来源直接支持，应降级。

## Search Query

CDN cache hit rate Zipf distribution alpha 1.0 N=100000

## Retrieval Sources

- {'url': 'https://help.aliyun.com/en/cdn/user-guide/cache-troubleshooting&rut=8bdbd3bf190d3c81a3572448d4787ed0eb120146f83d26ae5e9da197e46ddfef', 'type': 'ddg', 'title': 'What to do when CDN cache does not take effect Cache miss Low cache hit ...'}
- {'url': 'https://www.alphaxiv.org/&rut=27e93f256f16c5d5e1390c68a6573b729a409e7d20166c6dd2eb1401aa7c6a88', 'type': 'ddg', 'title': 'Explore | alphaXiv'}
- {'url': 'https://www.cdnplanet.com/tools/cdnfinder/&rut=bd1f74d87520d3311c526a79bf6cb42785ffdb68a1b32f6026a71a0f159c131a', 'type': 'ddg', 'title': 'CDN Finder - CDN Planet'}
