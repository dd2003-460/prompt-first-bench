# N348: 先验均值与采样均值的偏差量化：Dirichlet 分布的期望值 E[geo_share_i] = α_i / α_0 = geo_share_prior_i；需

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

先验均值与采样均值的偏差量化：Dirichlet 分布的期望值 E[geo_share_i] = α_i / α_0 = geo_share_prior_i；需验证蒙特卡洛采样 1000 次后的经验均值 μ_empirical_i 与先验均值 geo_share_prior_i 的偏差 |μ_empirical_i - geo_share_prior_i| < 0.01（1% 绝对误差）；若偏差超标，表明采样次数不足或随机种子设置不当，需增加采样或检查 RNG 质量

## Corrected Claim

先验均值与采样均值的偏差量化：Dirichlet 分布的期望值 E[geo_share_i] = α_i / α_0 = geo_share_prior_i；需验证蒙特卡洛采样 1000 次后的经验均值 μ_empirical_i 与先验均值 geo_share_prior_i 的偏差 |μ_empirical_i - geo_share_prior_i| < 0.01（1% 绝对误差）；若偏差超标，表明采样次数不足或随机种子设置不当，需增加采样或检查 RNG 质量

## Evidence

先验知识/题面给定，逻辑校验通过：Dirichlet分布期望公式正确，1000次采样下标准误约为0.01量级，1%绝对误差阈值在统计上合理且自洽。
