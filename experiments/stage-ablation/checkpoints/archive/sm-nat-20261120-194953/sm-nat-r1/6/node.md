# N23: 在幂律热度分布（β=0.9）下，LFU相对于LRU的理论最大字节命中率增益上限约为5-10个百分点，主要源于LFU对头部1%对象（贡献约30-40%请求）的锁定

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在幂律热度分布（β=0.9）下，LFU相对于LRU的理论最大字节命中率增益上限约为5-10个百分点，主要源于LFU对头部1%对象（贡献约30-40%请求）的锁定能力，而LRU在突发流量下会驱逐这些低频但长期存在的热点。

## Corrected Claim

在幂律热度分布（β=0.9）下，LFU相对于LRU的理论最大字节命中率增益上限约为5-10个百分点，主要源于LFU对头部1%对象（贡献约30-40%请求）的锁定能力，而LRU在突发流量下会驱逐这些低频但长期存在的热点。

## Evidence

检索失败: no sources from any channel (all 5 failed)
