# N192: 推荐权重截距 β 的确定：为使基准价格 P_median 处的权重 W = 1.0，结合 N118 的 α 值，解得 β = 1.0 - α * P_media

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N60

## Claim

推荐权重截距 β 的确定：为使基准价格 P_median 处的权重 W = 1.0，结合 N118 的 α 值，解得 β = 1.0 - α * P_median，确保基准商品获得标准曝光权重。

## Corrected Claim

推荐权重截距 β 的确定：为使基准价格 P_median 处的权重 W = 1.0，结合 N118 的 α 值，解得 β = 1.0 - α * P_median，确保基准商品获得标准曝光权重。

## Evidence

先验知识/题面给定，逻辑校验通过：线性权重模型 W = αP + β 中，令 P=P_median 时 W=1.0，代数推导得 β = 1.0 - αP_median，符合数学恒等式。
