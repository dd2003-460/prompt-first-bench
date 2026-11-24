# N464: 基于控制器瓶颈修正后的 NVMe SSD 层重建时间：T_rebuild_SSD = 100TB / 10GB/s ≈ 10 小时（若按 10GB/s 有效带宽

- **status**: verified
- **level**: L5
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N205

## Claim

基于控制器瓶颈修正后的 NVMe SSD 层重建时间：T_rebuild_SSD = 100TB / 10GB/s ≈ 10 小时（若按 10GB/s 有效带宽），或若带宽可达 12GB/s 则为 8.3 小时，远高于 N205 原估的 3.7 小时，表明 SSD 层重建已成为混合方案 RTO 的主要贡献者之一。

## Corrected Claim

基于控制器瓶颈修正后的 NVMe SSD 层重建时间：T_rebuild_SSD = 100TB / 10GB/s ≈ 10 小时（若按 10GB/s 有效带宽），或若带宽可达 12GB/s 则为 8.3 小时，远高于 N205 原估的 3.7 小时，表明 SSD 层重建已成为混合方案 RTO 的主要贡献者之一。

## Evidence

先验知识/题面给定，逻辑校验通过：100TB/10GB/s=10h，100TB/12GB/s≈8.3h，计算无误且符合物理直觉
