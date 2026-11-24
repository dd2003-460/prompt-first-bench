# N347: 采样分布的边界条件验证：Dirichlet 采样生成的 geo_share_i 必须满足 0 < geo_share_i < 1 且 Σgeo_share_i 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

采样分布的边界条件验证：Dirichlet 采样生成的 geo_share_i 必须满足 0 < geo_share_i < 1 且 Σgeo_share_i = 1；需验证在 α_0 = 10 时，采样值是否超出业务合理范围（如某省份占比 > 50% 或 < 1%）；若超出，需引入截断重采样（rejection sampling）或调整 α_i 下限（如 α_i ≥ 0.5）以排除极端不均衡场景

## Corrected Claim

采样分布的边界条件验证：Dirichlet 采样生成的 geo_share_i 必须满足 0 < geo_share_i < 1 且 Σgeo_share_i = 1；需验证在 α_0 = 10 时，采样值是否超出业务合理范围（如某省份占比 > 50% 或 < 1%）；若超出，需引入截断重采样（rejection sampling）或调整 α_i 下限（如 α_i ≥ 0.5）以排除极端不均衡场景

## Evidence

先验知识/题面给定，逻辑校验通过：Dirichlet分布生成的样本天然满足和为1且各分量大于0，α0=10时分布相对集中，提出截断重采样或调整α下限以排除极端不均衡场景符合统计学原理及工程实践。
