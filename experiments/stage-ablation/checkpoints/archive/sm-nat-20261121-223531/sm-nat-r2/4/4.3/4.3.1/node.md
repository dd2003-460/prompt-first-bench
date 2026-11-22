# N59: 在写穿透（Write-Through）模式下，有效命中率折损因子 $D_{WT}$ 等于 1，因为更新立即同步至缓存，不存在数据过期（$P_{stale}=0$

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

在写穿透（Write-Through）模式下，有效命中率折损因子 $D_{WT}$ 等于 1，因为更新立即同步至缓存，不存在数据过期（$P_{stale}=0$），但需扣除更新产生的写带宽占用对读缓存容量的挤占效应：$D_{WT} = 1 - \frac{\text{Write BW}_{upd}}{\text{Total BW}_{cap}}$，其中 $\text{Write BW}_{upd} = N_{obj} \times \lambda_{upd} \times E[S]$，若写带宽占比 < 5%，则折损可忽略。

## Corrected Claim

在写穿透（Write-Through）模式下，有效命中率折损因子 $D_{WT}$ 等于 1，因为更新立即同步至缓存，不存在数据过期（$P_{stale}=0$），但需扣除更新产生的写带宽占用对读缓存容量的挤占效应：$D_{WT} = 1 - \frac{\text{Write BW}_{upd}}{\text{Total BW}_{cap}}$，其中 $\text{Write BW}_{upd} = N_{obj} \times \lambda_{upd} \times E[S]$，若写带宽占比 < 5%，则折损可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过
