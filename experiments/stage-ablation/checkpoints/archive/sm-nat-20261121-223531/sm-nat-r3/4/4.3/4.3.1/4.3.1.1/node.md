# N165: Write-Through 模式下更新写带宽 Write BW_upd 的具体数值计算：Write BW_upd = N_obj * λ_upd * E[S] 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N59

## Claim

Write-Through 模式下更新写带宽 Write BW_upd 的具体数值计算：Write BW_upd = N_obj * λ_upd * E[S] = 100,000 * 0.01 * 10.5KB ≈ 10.5MB/天，折算为持续带宽约为 0.121 KB/s。

## Corrected Claim

Write-Through 模式下更新写带宽 Write BW_upd 的具体数值计算：Write BW_upd = N_obj * λ_upd * E[S] = 100,000 * 0.01 * 10.5KB ≈ 10.5MB/天，折算为持续带宽约为 0.121 KB/s。

## Evidence

先验知识/题面给定，逻辑校验通过：100,000 * 0.01 * 10.5KB = 10,500KB = 10.5MB；10.5MB / 86400s ≈ 0.121KB/s，计算无误。
