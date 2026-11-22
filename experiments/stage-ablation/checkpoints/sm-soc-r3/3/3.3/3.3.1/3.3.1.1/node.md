# N195: 曝光次数 N_impressions 的分解：N_impressions = N_active_listings × CTR_base × (1 + β_ran

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N63

## Claim

曝光次数 N_impressions 的分解：N_impressions = N_active_listings × CTR_base × (1 + β_rank × Margin)，其中 CTR_base 为基准点击率，β_rank 为排序权重对点击率的弹性系数，需通过 A/B 测试确定 β_rank 的具体数值。

## Corrected Claim

曝光次数 N_impressions 通常由流量池大小、用户活跃度及排序策略决定，不能简单分解为 CTR 与排序权重的乘积。CTR 是点击次数与曝光次数的比值，而非曝光次数的分解项。

## Evidence

[质询]该公式将曝光次数（Impressions）分解为点击率（CTR）与排序权重的乘积，存在严重的量纲和逻辑错误。曝光次数是展示量，而CTR是点击/曝光的比率，两者相乘在物理意义上无法得出曝光次数；此外，曝光次数通常由流量池大小和排序位置决定，而非由CTR直接决定（因果倒置或混淆）。 | 逻辑校验失败：公式量纲不一致（曝光次数 ≠ 列表数 × 比率 × 系数），且违背基本广告/推荐系统逻辑（曝光由排序和流量决定，CTR是结果而非曝光的构成因子）。无外部来源支持。

## Search Query

second hand marketplace CTR elasticity ranking weight margin A/B test
