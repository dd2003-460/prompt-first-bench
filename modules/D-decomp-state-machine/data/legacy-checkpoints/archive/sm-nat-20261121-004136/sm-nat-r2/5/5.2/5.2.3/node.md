# N65: LRU vs LFU 实测命中率差异（高成本低性）：在长尾负载下，LFU 相比 LRU 的字节命中率提升通常在 2-5 个百分点，需查证具体实验数据（如 Dap

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

LRU vs LFU 实测命中率差异（高成本低性）：在长尾负载下，LFU 相比 LRU 的字节命中率提升通常在 2-5 个百分点，需查证具体实验数据（如 Dapper, Memcached 案例）以确认增益范围。

## Corrected Claim

在长尾负载下，LFU相比LRU通常具有更高的字节命中率，具体增益范围取决于负载分布特征，需查证具体实验数据（如Dapper, Memcached案例）以确认。

## Evidence

[质询]该陈述包含具体的经验性数值范围（2-5个百分点）和特定案例引用（Dapper, Memcached），属于硬件/系统性能经验事实，无法从第一性原理推导。由于检索失败，缺乏直接来源支持该具体数值范围，且不同负载分布下LFU与LRU的差异可能远超或低于此范围，存在数值量级不准确的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）。LFU在长尾负载下通常优于LRU是公认结论，但具体2-5%的增益范围缺乏当前检索证据直接证实，故降级为定性表述。

## Search Query

LRU vs LFU cache hit rate comparison empirical CDN data
