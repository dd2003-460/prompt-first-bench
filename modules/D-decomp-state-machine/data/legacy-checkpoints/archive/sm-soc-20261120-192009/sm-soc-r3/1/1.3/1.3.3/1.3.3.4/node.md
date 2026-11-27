# N145: 下游投影 2：平台数据清洗阈值。为识别异常挂价，平台设定截断阈值 D_cut = Z_α * (σ_noise / μ)，其中 Z_α 为显著性水平 α（如 0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N43

## Claim

下游投影 2：平台数据清洗阈值。为识别异常挂价，平台设定截断阈值 D_cut = Z_α * (σ_noise / μ)，其中 Z_α 为显著性水平 α（如 0.05）对应的 Z 分数（1.645）；D > D_cut 的商品被标记为‘可疑高价’，触发人工审核或算法降权，该阈值直接决定了‘高挂价’样本的筛选边界。

## Corrected Claim

下游投影 2：平台数据清洗阈值。为识别异常挂价，平台设定截断阈值 D_cut = Z_α * (σ_noise / μ)，其中 Z_α 为显著性水平 α（如 0.05）对应的 Z 分数（1.645）；D > D_cut 的商品被标记为‘可疑高价’，触发人工审核或算法降权，该阈值直接决定了‘高挂价’样本的筛选边界。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

outlier detection threshold price deviation z-score platform data cleaning
