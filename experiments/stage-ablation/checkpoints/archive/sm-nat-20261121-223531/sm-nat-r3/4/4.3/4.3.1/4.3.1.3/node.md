# N167: Write-Through 模式下写带宽占比 R_bw 的量化判断：R_bw = Write BW_upd / Total BW_cap。由于 S_total 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N59

## Claim

Write-Through 模式下写带宽占比 R_bw 的量化判断：R_bw = Write BW_upd / Total BW_cap。由于 S_total (≈1.38MB 或修正后值) 远小于 128GB，且 Hit_Rate 极高，分母 Total BW_cap 极小或为0（若无 Miss），导致该比值在数学上无定义或极大，但物理上因无淘汰，写操作不挤占读缓存空间，故 D_WT 实际为 1.0，原公式在容量非约束场景下失效，需修正为 D_WT = 1.0。

## Corrected Claim

Write-Through 模式下写带宽占比 R_bw 的量化判断：R_bw = Write BW_upd / Total BW_cap。由于 S_total (≈1.38MB 或修正后值) 远小于 128GB，且 Hit_Rate 极高，分母 Total BW_cap 极小或为0（若无 Miss），导致该比值在数学上无定义或极大，但物理上因无淘汰，写操作不挤占读缓存空间，故 D_WT 实际为 1.0，原公式在容量非约束场景下失效，需修正为 D_WT = 1.0。

## Evidence

先验知识/题面给定，逻辑校验通过：Write-Through 模式下写操作直接穿透至主存，不占用缓存空间，因此不存在因写操作导致的缓存容量竞争或淘汰压力，写带宽对读缓存性能的干扰系数 D_WT 在物理上确实为 1.0（即无额外惩罚或干扰），原基于容量占比的公式在此场景下失效是合理的逻辑推导。
