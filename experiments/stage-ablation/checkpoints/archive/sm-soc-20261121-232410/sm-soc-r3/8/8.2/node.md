# N84: 买家点击转化率 CVR 在溢价区间的稳定性量化：定义 CVR(premium) = Clicks(premium) / Impressions(premium)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

买家点击转化率 CVR 在溢价区间的稳定性量化：定义 CVR(premium) = Clicks(premium) / Impressions(premium)，其中 premium ∈ [15%, 25%]；断言 CVR_stable = 0.12 ± 0.02 意味着 95% 置信区间下 CVR 波动范围 [0.08, 0.16]，且该区间不随时间序列发生结构性断裂（Chow test p-value > 0.1）。

## Corrected Claim

买家点击转化率 CVR 在溢价区间的稳定性量化：定义 CVR(premium) = Clicks(premium) / Impressions(premium)，其中 premium ∈ [15%, 25%]；断言 CVR_stable = 0.12 ± 0.02 意味着 95% 置信区间下 CVR 波动范围 [0.08, 0.16]，且该区间不随时间序列发生结构性断裂（Chow test p-value > 0.1）。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点定义中的三个独立维度：统计显著性/置信区间校准（数值验证）、时间序列稳定性（Chow检验）、以及区间内部异质性（分桶检验）。三者关注点不同（精度 vs 时间结构 vs 空间/参数结构），无重叠或矛盾，且共同覆盖了父节点关于CVR稳定性量化的所有关键断言。）

## Search Query

online marketplace click-through rate stability high premium listings 15-25% buyer behavior constant
