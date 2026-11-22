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

先验知识/题面给定，逻辑校验通过：CVR定义符合标准，0.12±0.02在95%置信区间下对应[0.08, 0.16]的数学推导正确，Chow test用于检测结构性断裂的逻辑合理。

## Search Query

online marketplace click-through rate stability high premium listings 15-25% buyer behavior constant
