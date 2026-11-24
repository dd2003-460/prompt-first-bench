# N546: N_POP=10时西部区域实际覆盖半径 R_cov_west 的精确值：基于10个POP点均匀分布假设，理论最小最大覆盖半径 R_cov_theory = D_

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N178

## Claim

N_POP=10时西部区域实际覆盖半径 R_cov_west 的精确值：基于10个POP点均匀分布假设，理论最小最大覆盖半径 R_cov_theory = D_100 / (2 * sqrt(N_POP)) = 5600km / (2 * 3.16) ≈ 887km；但实际由于西部人口密度低，POP点向东部倾斜，西部最近POP距离 D_west ≈ 1500km，故 R_cov_west = 1500km；此值与理论值差异源于人口密度不均，需用Voronoi划分修正。

## Corrected Claim

N_POP=10时，若假设D_100=5600km且西部最近POP距离D_west=1500km，则理论最小最大覆盖半径约为887km，而西部实际覆盖半径为1500km；此差异源于人口密度不均导致的POP点分布倾斜，需通过Voronoi划分进行修正。

## Evidence

[质询]陈述中引用的具体数值（D_100=5600km, D_west=1500km）属于特定场景下的经验数据或假设参数，并非普适的物理或数学常数。若这些数值并非题面给定或公认标准，则缺乏来源支持，存在数值量级或具体取值不准确的风险。 | source=knowledge，逻辑推导自洽（理论值计算正确，实际值与理论值差异归因于人口分布不均符合直觉），但具体数值（5600km, 1500km）为经验事实，无外部来源直接支持，依据经验事实排除条款降级。
