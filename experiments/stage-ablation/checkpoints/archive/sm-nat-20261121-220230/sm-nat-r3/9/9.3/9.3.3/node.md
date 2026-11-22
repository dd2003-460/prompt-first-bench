# N285: 二维积分 ∫∫_{s_i * λ_i > threshold} f_{S,H}(s,h) ds dh 的数值计算方法：采用蒙特卡洛积分，生成 100,000 个

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

二维积分 ∫∫_{s_i * λ_i > threshold} f_{S,H}(s,h) ds dh 的数值计算方法：采用蒙特卡洛积分，生成 100,000 个样本点 (s_i, h_i) ~ f_{S,H}(s,h)，统计满足 s_i * λ_i > threshold 的样本比例，该比例即为密度修正因子 Δρ 的估计值，标准误差为 √(p(1-p)/N_sims)。

## Corrected Claim

二维积分 ∫∫_{s_i * λ_i > threshold} f_{S,H}(s,h) ds dh 的数值计算方法：采用蒙特卡洛积分，生成 100,000 个样本点 (s_i, h_i) ~ f_{S,H}(s,h)，统计满足 s_i * λ_i > threshold 的样本比例，该比例即为密度修正因子 Δρ 的估计值，标准误差为 √(p(1-p)/N_sims)。

## Evidence

先验知识/题面给定，逻辑校验通过：蒙特卡洛积分估计二值指示函数期望值的原理正确，标准误差公式符合二项分布性质。
