# N489: 边界条件修正：HDD顺序写带宽受转速和缓存影响，7200rpm CMR硬盘在持续写入>10分钟后，缓存耗尽，带宽从初始200MB/s衰减至稳态150MB/s。计

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N213, N214, N215

## Claim

边界条件修正：HDD顺序写带宽受转速和缓存影响，7200rpm CMR硬盘在持续写入>10分钟后，缓存耗尽，带宽从初始200MB/s衰减至稳态150MB/s。计算RTO时应采用稳态值150MB/s/盘，而非峰值200MB/s，否则重建时间低估25%。

## Corrected Claim

HDD顺序写带宽受转速和缓存影响，7200rpm CMR硬盘在持续写入导致缓存耗尽后，带宽会从初始峰值衰减至较低的稳态值。计算RTO时应采用稳态值而非峰值，以避免重建时间被显著低估。

## Evidence

[质询]具体数值（200MB/s峰值、150MB/s稳态、25%低估）属于特定硬件型号的经验数据，不同品牌/型号的7200rpm CMR硬盘性能差异较大，且‘持续写入>10分钟’这一时间阈值缺乏通用标准，可能因固件策略而异。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

7200rpm CMR HDD sustained write bandwidth after cache exhaustion 150MB/s
