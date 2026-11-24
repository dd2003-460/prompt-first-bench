# N112: 缓存失效期间的回源带宽增量 ΔTraffic_back = R_daily * s_avg * (1-H_peak) - R_daily * s_avg * (

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

缓存失效期间的回源带宽增量 ΔTraffic_back = R_daily * s_avg * (1-H_peak) - R_daily * s_avg * (1-H_steady)，即 2TB * 0.2 - 2TB * 0.1 = 0.2TB = 200GB/日，用于计算额外带宽成本。

## Corrected Claim

缓存失效期间的回源带宽增量 ΔTraffic_back = R_daily * s_avg * (1-H_peak) - R_daily * s_avg * (1-H_steady)，即 2TB * 0.2 - 2TB * 0.1 = 0.2TB = 200GB/日，用于计算额外带宽成本。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 10 column 5 (char 822)
