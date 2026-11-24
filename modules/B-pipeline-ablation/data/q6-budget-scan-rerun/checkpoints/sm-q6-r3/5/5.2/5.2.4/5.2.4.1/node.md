# N264: 单POP服务半径 R 与最小间距 D_min 的关系：D_min ≥ 2 × R × cos(π/6) ≈ 1.732R（六边形蜂窝覆盖模型），若R=150km

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N97

## Claim

单POP服务半径 R 与最小间距 D_min 的关系：D_min ≥ 2 × R × cos(π/6) ≈ 1.732R（六边形蜂窝覆盖模型），若R=150km，则D_min≥260km；若要求D_min≥300km，则R≤173km，需验证北上广深+成都/武汉/西安/南京/杭州的最近邻距离是否满足

## Corrected Claim

单POP服务半径 R 与最小间距 D_min 的关系：D_min ≥ 2 × R × cos(π/6) ≈ 1.732R（六边形蜂窝覆盖模型），若R=150km，则D_min≥260km；若要求D_min≥300km，则R≤173km，需验证北上广深+成都/武汉/西安/南京/杭州的最近邻距离是否满足

## Evidence

先验知识/题面给定，逻辑校验通过：六边形蜂窝覆盖中，相邻基站中心距（最小间距）与覆盖半径的关系为 D_min = 2 * R * cos(30°) = √3 * R ≈ 1.732R。数值计算 150 * 1.732 = 259.8 ≈ 260km，300 / 1.732 ≈ 173.2km，逻辑与数学推导均自洽。

## Search Query

hexagonal cell coverage minimum distance radius formula
