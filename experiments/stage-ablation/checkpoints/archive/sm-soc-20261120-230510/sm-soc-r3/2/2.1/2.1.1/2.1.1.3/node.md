# N147: CTR方差 σ²_ctr 的构成分解：σ²_ctr = σ²_intrinsic + σ²_noise，其中 σ²_intrinsic 为商品固有吸引力差异（由

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N44

## Claim

CTR方差 σ²_ctr 的构成分解：σ²_ctr = σ²_intrinsic + σ²_noise，其中 σ²_intrinsic 为商品固有吸引力差异（由图片、描述质量决定），σ²_noise 为用户行为随机性；在二手非标品中，σ_noise 通常占总方差的 60-70%，导致单用户点击行为预测误差较大。

## Corrected Claim

CTR方差 σ²_ctr 的构成分解：σ²_ctr = σ²_intrinsic + σ²_noise，其中 σ²_intrinsic 为商品固有吸引力差异，σ²_noise 为用户行为随机性；在二手非标品中，σ_noise 通常占比较高，导致单用户点击行为预测误差较大。

## Evidence

[质询]60-70%的具体数值缺乏普适性，不同品类、流量规模及用户群体下噪声占比波动极大，该具体区间可能过于绝对或仅适用于特定小样本场景。 | 先验知识/题面给定，逻辑校验通过（方差分解逻辑自洽，但具体数值为经验估计，无来源支持且存在情境依赖性）
