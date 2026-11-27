# N142: 量化 LFU 在 ρ=-0.3 下的优势工作点 1（高频小对象锁定）：当热对象（Top 10%）平均大小 S_hot_avg ≈ 10KB（基于负相关假设），而

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N46

## Claim

量化 LFU 在 ρ=-0.3 下的优势工作点 1（高频小对象锁定）：当热对象（Top 10%）平均大小 S_hot_avg ≈ 10KB（基于负相关假设），而冷对象平均大小 S_cold_avg ≈ 5MB（基于截断分布估计）时，LFU 通过锁定小热对象，其字节命中率增益 ΔH_ρ ≈ (S_cold_avg / S_total_avg) * (P_cold_access) * 0.5。代入数值估算该工作点的增益约为 0.5-1.5 个百分点。

## Corrected Claim

在假设热对象平均大小约为10KB、冷对象平均大小约为5MB且存在负相关性的条件下，LFU通过锁定小热对象可能带来约0.5-1.5个百分点的字节命中率增益（具体数值依赖于实际工作负载分布）。

## Evidence

[质询]该陈述包含具体的经验性参数（S_hot_avg ≈ 10KB, S_cold_avg ≈ 5MB）和特定的量化模型公式，这些属于经验事实而非第一性原理可推导的数学/物理定律。在缺乏外部来源支持的情况下，无法验证这些具体数值和公式的准确性及适用性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

LFU vs LRU hit rate improvement Zipf workload negative correlation size frequency
