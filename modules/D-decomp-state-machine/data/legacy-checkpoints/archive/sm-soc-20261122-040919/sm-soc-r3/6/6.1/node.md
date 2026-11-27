# N109: 宏观‘市场溢价带’宽度 ΔP_band 与个体噪声方差 σ²_noise 的关系式：ΔP_band ≈ 2 * z_{0.975} * σ_noise / sq

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N27

## Claim

宏观‘市场溢价带’宽度 ΔP_band 与个体噪声方差 σ²_noise 的关系式：ΔP_band ≈ 2 * z_{0.975} * σ_noise / sqrt(N_eff)，其中 N_eff 为有效独立卖家数量，z_{0.975}=1.96。若观测 ΔP_band 为 15-25% 的中点 20%，且 N_eff=1000，则反推个体噪声标准差 σ_noise ≈ 20% * sqrt(1000) / (2*1.96) ≈ 32.2%。[待核验]：N_eff 需根据平台活跃卖家数校准。

## Corrected Claim

宏观‘市场溢价带’宽度 ΔP_band 与个体噪声方差 σ²_noise 的关系式：ΔP_band ≈ 2 * z_{0.975} * σ_noise / sqrt(N_eff)，其中 N_eff 为有效独立卖家数量，z_{0.975}=1.96。若观测 ΔP_band 为 15-25% 的中点 20%，且 N_eff=1000，则反推个体噪声标准差 σ_noise ≈ 20% * sqrt(1000) / (2*1.96) ≈ 32.2%。[待核验]：N_eff 需根据平台活跃卖家数校准。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别聚焦于噪声源的定义（微观基础）、有效样本量校准（统计修正）以及宏观观测值的投影修正（结果验证），逻辑上层层递进且互不重叠。子节点2和3虽然都涉及 N_eff 的变化，但前者关注如何计算 N_eff，后者关注 N_eff 变化对反推 σ_noise 的具体数值影响及解释，属于因果链条的不同环节，不构成冗余。）

## Search Query

law of large numbers aggregate noise variance market price band width
