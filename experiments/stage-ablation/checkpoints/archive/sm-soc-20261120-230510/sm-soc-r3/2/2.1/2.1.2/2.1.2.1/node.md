# N149: 曝光量 Q_exposure 的构成：Q_exposure = Q_base * W_rank * f_trend，其中 Q_base 为平台基础流量池大小，W

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

曝光量 Q_exposure 的构成：Q_exposure = Q_base * W_rank * f_trend，其中 Q_base 为平台基础流量池大小，W_rank 为排序权重（如 N18 中干预后为 0.5），f_trend 为时间趋势因子（如周末效应 ±10%）；需明确 Q_base 的量级以计算绝对曝光损失。

## Corrected Claim

曝光量 Q_exposure 的构成：Q_exposure = Q_base * W_rank * f_trend，其中 Q_base 为平台基础流量池大小，W_rank 为排序权重（如 N18 中干预后为 0.5），f_trend 为时间趋势因子（如周末效应 ±10%）；需明确 Q_base 的量级以计算绝对曝光损失。

## Evidence

先验知识/题面给定，逻辑校验通过
