# N97: 对象大小与请求热度负相关（ρ≈-0.3）在缓存容量充足（覆盖全集）时对 LRU 的缓存内容选择无影响，因为所有对象均被缓存；该负相关性仅在缓存容量受限（C < 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对象大小与请求热度负相关（ρ≈-0.3）在缓存容量充足（覆盖全集）时对 LRU 的缓存内容选择无影响，因为所有对象均被缓存；该负相关性仅在缓存容量受限（C < V_total）时通过驱逐策略影响命中率，此时热门小对象优先驻留，提升字节命中率。

## Corrected Claim

对象大小与请求热度负相关（ρ≈-0.3）在缓存容量充足（覆盖全集）时对 LRU 的缓存内容选择无影响，因为所有对象均被缓存；该负相关性仅在缓存容量受限（C < V_total）时通过驱逐策略影响命中率，此时热门小对象优先驻留，提升字节命中率。

## Evidence

检索失败: no sources from any channel (all 5 failed)
