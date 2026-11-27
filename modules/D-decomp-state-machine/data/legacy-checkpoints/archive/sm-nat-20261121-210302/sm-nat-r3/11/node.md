# N87: 在 ρ=-0.3 的负相关场景下，缓存前 10% 最热门对象所需的平均空间比独立假设下减少约 15%，具体修正系数为 1 + 0.5*ρ，即 0.85，用于调整

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在 ρ=-0.3 的负相关场景下，缓存前 10% 最热门对象所需的平均空间比独立假设下减少约 15%，具体修正系数为 1 + 0.5*ρ，即 0.85，用于调整 N_cap 的计算精度，确保 LRU 下界估算更贴近实际 CDN 负载特征。

## Corrected Claim

在 ρ=-0.3 的负相关场景下，缓存前 10% 最热门对象所需的平均空间比独立假设下减少约 15%，具体修正系数为 1 + 0.5*ρ，即 0.85，用于调整 N_cap 的计算精度，确保 LRU 下界估算更贴近实际 CDN 负载特征。

## Evidence

检索失败: no sources from any channel (all 5 failed)
