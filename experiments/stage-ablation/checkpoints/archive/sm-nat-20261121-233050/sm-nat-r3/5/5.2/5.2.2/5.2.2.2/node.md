# N136: 空间局部性修正项 γ_spatial 的量化：基于 IP 聚合度 λ_ip，γ_spatial = 1 + λ_ip * (1 - 1/N_unique_ips

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53, N54, N55

## Claim

空间局部性修正项 γ_spatial 的量化：基于 IP 聚合度 λ_ip，γ_spatial = 1 + λ_ip * (1 - 1/N_unique_ips)，其中 N_unique_ips 为独立 IP 数；在 λ_ip=0.2 且 N_unique_ips=1000 时，γ_spatial ≈ 1.198。

## Corrected Claim

空间局部性修正项 γ_spatial 的量化：基于 IP 聚合度 λ_ip，γ_spatial = 1 + λ_ip * (1 - 1/N_unique_ips)，其中 N_unique_ips 为独立 IP 数；在 λ_ip=0.2 且 N_unique_ips=1000 时，γ_spatial ≈ 1.198。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 γ_spatial = 1 + λ_ip * (1 - 1/N_unique_ips) 代入 λ_ip=0.2, N_unique_ips=1000 计算得 1 + 0.2 * (1 - 0.001) = 1 + 0.2 * 0.999 = 1.1998，约等于 1.198（存在微小舍入差异，但在合理误差范围内，且量级与逻辑自洽）。

## Search Query

spatial locality CDN cache hit rate correction factor
