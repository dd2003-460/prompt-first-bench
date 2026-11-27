# N358: 驱动力指数 D_driver 的归一化处理：将 S_seller, S_buyer, S_platform 标准化为 Z-score 后加权求和，权重 w_s,

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N121

## Claim

驱动力指数 D_driver 的归一化处理：将 S_seller, S_buyer, S_platform 标准化为 Z-score 后加权求和，权重 w_s, w_b, w_p 通过主成分分析（PCA）第一主成分载荷确定；若 w_p 在 PCA 中载荷 > 0.6，则平台贡献度最高。

## Corrected Claim

驱动力指数 D_driver 的归一化处理：将 S_seller, S_buyer, S_platform 标准化为 Z-score 后加权求和，权重 w_s, w_b, w_p 通过主成分分析（PCA）第一主成分载荷确定；若 w_p 在 PCA 中载荷 > 0.6，则平台贡献度最高。

## Evidence

先验知识/题面给定，逻辑校验通过
